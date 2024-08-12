


import numpy as np
import matplotlib.pyplot as plt
import cmocean.cm as cm
import netCDF4 as nc4
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import sys


data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data/Version4/Release4/interp_monthly'

ds = nc4.Dataset(data_folder+'/THETA/THETA_2015_06.nc')
longitude = ds.variables['longitude'][:]
latitude = ds.variables['latitude'][:]
Theta = ds.variables['THETA'][:]
ds.close()


plot_lon_1 = -150
lon_index_1 = np.argmin(np.abs(longitude-plot_lon_1))

plot_lon_2 = -31
lon_index_2 = np.argmin(np.abs(longitude-plot_lon_2))


# plt.show()
vmin = -2
vmax = 30
cmap = 'turbo'

fig = plt.figure(figsize=(10,12))

gs = GridSpec(3,12, left=0.09, right=0.95, bottom=0.08, top=0.93)

proj = ccrs.Robinson()
ax1 = fig.add_subplot(gs[0, :-2], projection = proj)
ax1.pcolormesh(longitude,latitude,Theta[0,0,:,:],transform=ccrs.PlateCarree(),
               vmin = vmin, vmax = vmax, cmap = cmap)
ax1.plot(np.ones_like(latitude)*plot_lon_1, latitude, 'k-',transform=ccrs.PlateCarree())
ax1.plot(np.ones_like(latitude)*plot_lon_2, latitude, 'k-',transform=ccrs.PlateCarree())
ax1.add_feature(cfeature.LAND, zorder=99, facecolor='silver')
ax1.coastlines()
ax1.set_title('Temperature')
gl = plt.gca().gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                         linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = False
gl.xlines = True
gl.xlabels_bottom = True
gl.xlocator = mticker.FixedLocator([-60, -30, 0, 30, 60])
gl.xlocator = mticker.FixedLocator([plot_lon_1, plot_lon_2])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

axc = fig.add_subplot(gs[0, -1])
x = np.array([0,1])
y = np.linspace(vmin,vmax,100)
X,Y = np.meshgrid(x,y)
axc.pcolormesh(X,Y,Y,vmin=vmin, vmax=vmax,cmap=cmap)
axc.set_ylabel('Temperature ($^{\circ}$C)')
axc.set_xticks([])

ax2 = fig.add_subplot(gs[1, :])
ax2.pcolormesh(latitude, np.arange(50), Theta[0,:,:, lon_index_1],
               vmin = vmin, vmax = vmax, cmap = cmap)
ax2.set_xticks([-60, -30, 0, 30, 60])
ax2.invert_yaxis()

ax3 = fig.add_subplot(gs[2, :])
plt.pcolormesh(latitude, np.arange(50), Theta[0,:,:, lon_index_2],
               vmin = vmin, vmax = vmax, cmap = cmap)
ax3.invert_yaxis()
ax3.set_xticks([-60, -30, 0, 30, 60])
ax3.set_xlabel('Latitude')

output_file = '../images/ecco_atlantic_crossection.png'
plt.savefig(output_file)
plt.close(fig)




