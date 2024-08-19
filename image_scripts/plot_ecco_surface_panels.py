import os
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4
import cmocean.cm as cm
import cartopy
import cartopy.crs as ccrs
# from scipy.interpolate import griddata
import cartopy.feature as cfeature


def read_eccov4_field(data_folder, var_name, year = 2015, month = 6):

    file_name = os.path.join(data_folder,var_name,var_name+'_'+str(year)+'_'+'{:02d}'.format(month)+'.nc')
    ds = nc4.Dataset(file_name)
    lon = ds.variables['longitude'][:]
    lat = ds.variables['latitude'][:]
    var_grid = ds.variables[var_name][:, :, :]
    ds.close()

    Lon, Lat = np.meshgrid(lon, lat)
    var_grid = var_grid[0, :, :]
    return(lon, Lat, var_grid)

def plot_ecco_EPR_fields(data_folder):

    Lon, Lat, EmPmR = read_eccov4_field(data_folder, 'EXFempmr')
    _, _, Evap = read_eccov4_field(data_folder, 'EXFevap')
    _, _, Preci = read_eccov4_field(data_folder, 'EXFpreci')
    _, _, Roff = read_eccov4_field(data_folder, 'EXFroff')

    exf_grids = [Evap, Preci, Roff, EmPmR]
    variable_names = ['Evaporation ($E$)', 'Precipitation ($P$)', 'Runoff ($R$)', '$E - P - R$']
    meta_dict = {'Evaporation ($E$)': [0, 1e-7, cm.solar, 'm/s'],
                 'Precipitation ($P$)': [0, 1e-7, cm.tempo, 'm/s'],
                 'Runoff ($R$)': [0, 1e-7, cm.tempo, 'm/s'],
                 '$E - P - R$': [-1e-7, 1e-7, cm.balance, 'm/s']}

    proj = ccrs.Robinson()
    fig, axes = plt.subplots(
        2, 2, figsize=(8, 5),
        subplot_kw={'projection': proj},  # ,"aspect": 2
        gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
    )
    # plt.style.use('dark_background')

    for i in range(len(variable_names)):
        print('Plotting ' + variable_names[i], np.min(exf_grids[i]), np.max(exf_grids[i]))
        plt.subplot(2, 2, i + 1)

        C = plt.pcolormesh(Lon, Lat, exf_grids[i], transform=ccrs.PlateCarree(),
                           vmin=meta_dict[variable_names[i]][0],
                           vmax=meta_dict[variable_names[i]][1],
                           cmap=meta_dict[variable_names[i]][2])
        if i % 2 == 0:
            plt.colorbar(C, label=meta_dict[variable_names[i]][3], location='left', fraction=0.026)
        else:
            plt.colorbar(C, label=meta_dict[variable_names[i]][3], fraction=0.026)
        plt.title(variable_names[i])

        plt.gca().add_feature(cfeature.LAND, zorder=99, facecolor='silver')
        plt.gca().coastlines()

    output_file = '../images/ecco_EPR_fields.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)

def plot_ecco_Qnet(data_folder):

    Lon, Lat, Qnet = read_eccov4_field(data_folder, 'oceQnet', month=9)

    meta_dict = {'Qnet': [-180,180, cm.balance, 'W/m$^2$']}

    proj = ccrs.Robinson()
    fig, axes = plt.subplots(
        1,1, figsize=(8, 5),
        subplot_kw={'projection': proj},  # ,"aspect": 2
        gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
    )
    # plt.style.use('dark_background')

    print('Plotting Qnet', np.min(Qnet), np.max(Qnet))

    C = plt.pcolormesh(Lon, Lat, Qnet, transform=ccrs.PlateCarree(),
                       vmin=meta_dict['Qnet'][0],
                       vmax=meta_dict['Qnet'][1],
                       cmap=meta_dict['Qnet'][2])

    plt.colorbar(C, label=meta_dict['Qnet'][3], fraction=0.026)

    plt.gca().add_feature(cfeature.LAND, zorder=99, facecolor='silver')
    plt.gca().coastlines()

    plt.title('Net Ocean Heat Uptake')

    output_file = '../images/ecco_Qnet_field.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)

def plot_ecco_Seaice(data_folder):

    Lon, Lat, SIarea = read_eccov4_field(data_folder, 'SIarea')
    SIarea*=100

    meta_dict = {'Sea Ice Concentration': [0,100, cm.ice, '%']}

    proj = ccrs.Robinson()
    fig, axes = plt.subplots(
        1,1, figsize=(8, 5),
        subplot_kw={'projection': proj},  # ,"aspect": 2
        gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
    )
    # plt.style.use('dark_background')

    print('Plotting Sea Ice Concentration', np.min(SIarea), np.max(SIarea))

    C = plt.pcolormesh(Lon, Lat, SIarea, transform=ccrs.PlateCarree(),
                       vmin=meta_dict['Sea Ice Concentration'][0],
                       vmax=meta_dict['Sea Ice Concentration'][1],
                       cmap=meta_dict['Sea Ice Concentration'][2])

    plt.colorbar(C, label=meta_dict['Sea Ice Concentration'][3], fraction=0.026)

    plt.gca().add_feature(cfeature.LAND, zorder=99, facecolor='silver')
    plt.gca().coastlines()

    plt.title('Sea Ice Concentraion')

    output_file = '../images/ecco_SIarea_field.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)


data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data/Version4/Release4/interp_monthly'


# plot_ecco_EPR_fields(data_folder)

# plot_ecco_Qnet(data_folder)

plot_ecco_Seaice(data_folder)




