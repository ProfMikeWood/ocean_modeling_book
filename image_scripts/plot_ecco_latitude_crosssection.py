
import numpy as np
import matplotlib.pyplot as plt
import cmocean.cm as cm
import netCDF4 as nc4
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mticker
from matplotlib.patches import Polygon
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import gsw

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import sys

import warnings
warnings.filterwarnings('ignore')

def read_theta(data_folder):
    ds = nc4.Dataset(data_folder+'/Version4/Release4/interp_monthly/THETA/THETA_2015_06.nc')
    longitude = ds.variables['longitude'][:]
    latitude = ds.variables['latitude'][:]
    Theta = ds.variables['THETA'][:]
    ds.close()

    # fill out the bottom to avoid ugly plot
    for row in range(np.shape(Theta)[-2]):
        for col in range(np.shape(Theta)[-1]):
            if np.any(Theta[0, :, row, col] != 0):
                max_index = np.sum(Theta[0, :, row, col] != 0)
                Theta[0, max_index:, row, col] = Theta[0, max_index - 1, row, col]

    Theta[Theta == 0] = np.nan
    return(longitude, latitude, Theta)

def read_salt(data_folder):
    ds = nc4.Dataset(data_folder+'/Version4/Release4/interp_monthly/SALT/SALT_2015_06.nc')
    longitude = ds.variables['longitude'][:]
    latitude = ds.variables['latitude'][:]
    Salt = ds.variables['SALT'][:]
    ds.close()

    # fill out the bottom to avoid ugly plot
    for row in range(np.shape(Salt)[-2]):
        for col in range(np.shape(Salt)[-1]):
            if np.any(Salt[0,:,row,col]!=0):
                max_index = np.sum(Salt[0,:,row,col]!=0)
                Salt[0,max_index:,row,col] = Salt[0,max_index-1,row,col]

    Salt[Salt==0] = np.nan

    return(longitude, latitude, Salt)

def read_grid(data_folder, longitude, latitude, plot_lon):

    for grid_number in range(1,13):
        ds = nc4.Dataset(data_folder + '/Version5/Alpha/nctiles_grid/GRID/GRID.'+'{:04d}'.format(grid_number)+'.nc')
        XC = ds.variables['XC'][:,:]
        YC = ds.variables['YC'][:, :]
        Depth = ds.variables['Depth'][:, :]
        if grid_number==1:
            Z = ds.variables['RC'][:]*-1
            xyz = np.column_stack([XC.ravel(), YC.ravel(), Depth.ravel()])
        else:
            xyz = np.vstack([xyz, np.column_stack([XC.ravel(), YC.ravel(), Depth.ravel()])])
        ds.close()

    lon = np.ones_like(latitude) * plot_lon
    lat = latitude

    depth = np.zeros_like(lon)
    for i in range(len(depth)):
        dist = ((lon[i]-xyz[:,0])**2 + (lat[i]-xyz[:,1])**2)**0.5
        index = np.argmin(dist)
        depth[i]=xyz[index,2]

    return(Z, depth)

def plot_crosssection(output_file, longitude, latitude, var_grid, Z, depth, plot_lon, plot_metadata):
    lon_index = np.argmin(np.abs(longitude - plot_lon))

    fig = plt.figure(figsize=(10, 10))
    plt.style.use('dark_background')

    gs = GridSpec(3, 15, left=0.09, right=0.95, bottom=0.05, top=0.96,hspace=0.03)

    proj = ccrs.Robinson()
    ax1 = fig.add_subplot(gs[0, :-2], projection=proj)
    ax1.pcolormesh(longitude, latitude, var_grid[0, 0, :, :], transform=ccrs.PlateCarree(),
                   vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    ax1.plot(np.ones_like(latitude) * plot_lon, latitude, 'k-', transform=ccrs.PlateCarree())
    ax1.add_feature(cfeature.LAND, zorder=99, facecolor='silver')
    ax1.coastlines()
    ax1.set_title(plot_metadata['long_name'])
    gl = plt.gca().gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                             linewidth=1, color='k', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_left = False
    gl.xlines = True
    gl.xlabels_bottom = False
    gl.xlocator = mticker.FixedLocator([-60, -30, 0, 30, 60])
    gl.xlocator = mticker.FixedLocator([plot_lon])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    if plot_metadata['long_name']=='Density':
        axc = fig.add_subplot(gs[0, -1])
    else:
        axc = fig.add_subplot(gs[0, -2])
    x = np.array([0, 1])
    y = np.linspace(plot_metadata['vmin'], plot_metadata['vmax'], 100)
    X, Y = np.meshgrid(x, y)
    axc.pcolormesh(X, Y, Y, vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    axc.set_ylabel(plot_metadata['long_name']+' ('+plot_metadata['units']+')')
    axc.set_xticks([])

    top_bathy = np.column_stack([latitude,depth])
    bottom_bathy = np.column_stack([latitude,6500*np.ones_like(depth)])
    bathy_polygon = np.vstack([top_bathy, np.flipud(bottom_bathy)])
    bathy = Polygon(bathy_polygon, facecolor='silver', edgecolor='k', zorder=10)
    bathy_2 = Polygon(bathy_polygon, facecolor='silver', edgecolor='k', zorder=10)

    ax2 = fig.add_subplot(gs[1, :])
    # ax2.pcolormesh(latitude, Z, var_grid[0, :, :, lon_index],
    #                vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    ax2.contourf(latitude, Z, var_grid[0, :, :, lon_index], 100,
                   vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    ax2.contour(latitude, Z, var_grid[0, :, :, lon_index], levels=plot_metadata['contour_ticks'], colors='k', linewidths=0.75,
                 vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'])
    ax2.plot(latitude,depth,'k-')
    ax2.add_patch(bathy)
    ax2.set_ylabel('Depth (m)')
    # ax2.set_xticks([-60, -30, 0, 30, 60])
    ax2.set_ylim([999, 0])

    ax3 = fig.add_subplot(gs[2, :])
    plt.pcolormesh(latitude, Z, var_grid[0, :, :, lon_index],
                   vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    ax3.contourf(latitude, Z, var_grid[0, :, :, lon_index], 100,
                 vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'], cmap=plot_metadata['cmap'])
    ax3.contour(latitude, Z, var_grid[0, :, :, lon_index], levels=plot_metadata['contour_ticks'], colors='k', linewidths=0.75,
                 vmin=plot_metadata['vmin'], vmax=plot_metadata['vmax'])
    ax3.add_patch(bathy_2)
    ax3.set_ylabel('Depth (m)')
    ax3.plot(latitude,depth,'k-')
    ax3.set_ylim([6200,1000])
    ax3.set_xticks([-60, -30, 0, 30, 60])
    ax3.set_xlabel('Latitude')

    plt.savefig(output_file)
    plt.close(fig)

data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data'

plot_lon = -31

var_name = 'Density'

if var_name == 'Theta':
    plot_metadata = {'var_name': 'Theta',
                     'long_name': 'Temperature',
                     'vmin': -2,
                     'vmax': 30,
                     'cmap': 'turbo',
                     'units': '$^{\circ}$C',
                     'contour_ticks': np.arange(5,30,5)}

    longitude, latitude, Theta = read_theta(data_folder)

    Z, depth = read_grid(data_folder, longitude, latitude, plot_lon)

    output_file = '../images/ecco_atlantic_crossection_Theta.png'

    plot_crosssection(output_file, longitude, latitude, Theta, Z, depth, plot_lon, plot_metadata)

if var_name == 'Salt':
    plot_metadata = {'var_name': 'Salt',
                     'long_name': 'Salinity',
                     'vmin': 32,
                     'vmax': 36.5,
                     'cmap': cm.haline,
                     'units': 'psu',
                     'contour_ticks': np.arange(32,36.5,0.5)}

    longitude, latitude, Salt = read_salt(data_folder)

    Z, depth = read_grid(data_folder, longitude, latitude, plot_lon)

    output_file = '../images/ecco_atlantic_crossection_Salt.png'

    plot_crosssection(output_file, longitude, latitude, Salt, Z, depth, plot_lon, plot_metadata)

if var_name == 'Density':
    plot_metadata = {'var_name': 'Density',
                     'long_name': 'Density',
                     'vmin': 1022,
                     'vmax': 1030,
                     'cmap': cm.dense,
                     'units': 'kg/m$^3$',
                     'contour_ticks': np.arange(1022,1030,0.5)}

    print('   - Reading Theta')
    longitude, latitude, Theta = read_theta(data_folder)

    Z, depth = read_grid(data_folder, longitude, latitude, plot_lon)

    print('   - Reading Salt')
    _, _, Salt = read_salt(data_folder)

    print('   - Reading Density')
    Absolute_salinity = gsw.conversions.SA_from_SP(Salt, Z[0], np.mean(longitude), np.mean(latitude))
    Conservative_temperature = gsw.conversions.CT_from_pt(Absolute_salinity, Theta)

    Rho = gsw.density.rho(Absolute_salinity, Conservative_temperature, Z[0])

    print(np.min(Rho), np.max(Rho))

    output_file = '../images/ecco_atlantic_crossection_Density.png'

    plot_crosssection(output_file, longitude, latitude, Rho, Z, depth, plot_lon, plot_metadata)


