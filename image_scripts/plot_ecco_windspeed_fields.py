


import numpy as np
import matplotlib.pyplot as plt
import cmocean.cm as cm
import cartopy
import cartopy.crs as ccrs
from scipy.interpolate import griddata
import cartopy.feature as cfeature


import sys
sys.path.insert(1,'/Users/mike/Documents/Research/Projects/Ocean_Modeling/Github Repositories')
from eccoseas.ecco import exf
from eccoseas.ecco import grid
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data/Version5/Alpha'

file_prefix_dict = {'UWIND':'EIG_u10m',
                    'VWIND':'EIG_v10m'}

meta_dict = {'UWIND':[-12, 12, cm.balance, 'm/s', 'Zonal Wind'],
             'VWIND':[-12, 12, cm.balance, 'm/s', 'Meridional Wind']}

variable_names = list(file_prefix_dict.keys())


exf_grids = []
year=2008

print('Reading in the data')
for field in variable_names:
    lon,lat,exf_grid = exf.read_ecco_exf_file(data_folder+'/era_xx', file_prefix_dict[field], year)
    exf_grid = np.mean(exf_grid,axis=0)
    exf_grids.append(exf_grid)

exf_grids.append( (exf_grids[0]**2 + exf_grids[1]**2)**0.5 )
meta_dict['WSPD'] = [0, 12, cm.speed_r, 'm/s', 'Wind Speed']
variable_names.append('WSPD')

Lon, Lat = np.meshgrid(lon,lat)

fig = plt.figure(figsize=(8,10))

proj = ccrs.Robinson()
fig,axes = plt.subplots(
    2,2, figsize=(9,4),
    subplot_kw={'projection': proj},#,"aspect": 2
    gridspec_kw = {'wspace':0.1, 'hspace':0.07, 'left':0.11, 'right':0.9, 'top':0.95, 'bottom':0.05},
)

for i in range(len(variable_names)+1):

    plt.subplot(2,2,i+1)

    if i<3:
        print('Plotting ' + variable_names[i])
        C = plt.pcolormesh(lon,lat,exf_grids[i],transform=ccrs.PlateCarree(),
                           vmin=meta_dict[variable_names[i]][0],
                           vmax=meta_dict[variable_names[i]][1],
                           cmap=meta_dict[variable_names[i]][2])
        if i % 2 == 0:
            plt.colorbar(C, label=meta_dict[variable_names[i]][3], location='left', fraction=0.026)
        else:
            plt.colorbar(C, label=meta_dict[variable_names[i]][3], fraction=0.026)
        plt.title(meta_dict[variable_names[i]][4])

        if i<2:
            gl = plt.gca().gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                                 linewidth=1, color='k', alpha=0.5, linestyle='--')
        else:
            gl = plt.gca().gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                                     linewidth=1, color='w', alpha=0.5, linestyle='--')
        gl.xlabels_top = False
        if i % 2 != 0:
            gl.ylabels_right = False
        gl.ylabels_left = False
        gl.xlines = False
        gl.xlabels_bottom = False
        gl.xlocator = mticker.FixedLocator([-60, -30, 0, 30, 60])
        gl.xformatter = LONGITUDE_FORMATTER
        gl.yformatter = LATITUDE_FORMATTER


    else:
        C = plt.pcolormesh(lon, lat, exf_grids[i-1], transform=ccrs.PlateCarree(),
                           vmin=meta_dict[variable_names[i-1]][0],
                           vmax=meta_dict[variable_names[i-1]][1],
                           cmap=meta_dict[variable_names[i-1]][2], alpha=0.2)
        plt.colorbar(C, label=meta_dict[variable_names[i-1]][3], fraction=0.026)
        skip = 10

        plt.quiver(Lon[::skip,::skip],Lat[::skip,::skip],
                   exf_grids[0][::skip,::skip],#/np.abs(exf_grids[0][::skip,::skip]),
                   exf_grids[1][::skip,::skip],#/np.abs(exf_grids[1][::skip,::skip]),
                   transform=ccrs.PlateCarree())
        plt.title('Wind Vectors')

    plt.gca().add_feature(cfeature.LAND, zorder=99, facecolor='silver')
    plt.gca().coastlines()


output_file = '../images/ecco_wind_fields.png'
plt.savefig(output_file,bbox_inches='tight')
plt.close(fig)




