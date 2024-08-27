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
    var_grid = var_grid[0, 0, :, :]
    return(lon, Lat, var_grid)

def plot_ecco_velocity_fields(data_folder):

    Lon, Lat, EVEL = read_eccov4_field(data_folder, 'EVEL', month=12)
    _, _, NVEL = read_eccov4_field(data_folder, 'NVEL', month=12)

    exf_grids = [EVEL, NVEL]
    variable_names = ['Zonal Velocity', 'Meridional Velocity']
    meta_dict = {'Zonal Velocity': [-0.5, 0.5, cm.balance, 'm/s'],
                 'Meridional Velocity': [-0.5, 0.5, cm.balance, 'm/s']}

    proj = ccrs.Robinson()
    fig, axes = plt.subplots(
        1, 2, figsize=(8, 4),
        subplot_kw={'projection': proj},  # ,"aspect": 2
        gridspec_kw={'wspace': 0.03, 'hspace': 0.03, 'left': 0.11, 'right': 0.9, 'top': 0.95, 'bottom': 0.05},
    )
    # plt.style.use('dark_background')

    for i in range(len(variable_names)):
        print('Plotting ' + variable_names[i], np.min(exf_grids[i]), np.max(exf_grids[i]))
        plt.subplot(1, 2, i + 1)

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

    output_file = '../images/ecco_velocity_fields.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close(fig)


data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data/Version4/Release4/interp_monthly'


plot_ecco_velocity_fields(data_folder)




