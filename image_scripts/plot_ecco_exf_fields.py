


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


data_folder = '/Users/mike/Documents/Teaching/Courses/CS 185C/Data/Version5/Alpha'

file_prefix_dict = {'ATEMP':'EIG_tmp2m_degC_plus_ECCO_v4r1_ctrl',
             'AQH':'EIG_spfh2m_plus_ECCO_v4r1_ctrl',
             'SWDOWN':'EIG_dsw_plus_ECCO_v4r1_ctrl',
             'LWDOWN':'EIG_dlw_plus_ECCO_v4r1_ctrl',
             'UWIND':'EIG_u10m',
             'VWIND':'EIG_v10m',
             'PRECIP':'EIG_rain_plus_ECCO_v4r1_ctrl',
             'RUNOFF':'runoff-2d-Fekete-1deg-mon-V4-SMOOTH.bin'}

meta_dict = {'ATEMP':[-60, 30, cm.thermal, '$^{\circ}$C'],
             'AQH':[0, 0.025, cm.tempo, 'kg/kg'],
             'PRECIP':[0, 1e-6, cm.tempo, 'm/s'],
             'SWDOWN':[-1000, 100,cm.solar,'W/m$^2$'],
             'LWDOWN':[-500, 100,cm.solar,'W/m$^2$'],
             'UWIND':[-20, 20, cm.balance, 'm/s'],
             'VWIND':[-20, 20, cm.balance, 'm/s'],
             'RUNOFF':[0, 2e-8, cm.tempo, 'm/s']}

variable_names = list(file_prefix_dict.keys())


exf_grids = []
year=2008

print('Reading in the data')
for field in variable_names:
    if field!='RUNOFF':
        lon,lat,exf_grid = exf.read_ecco_exf_file(data_folder+'/era_xx', file_prefix_dict[field], year)
        exf_grids.append(exf_grid[15*4+2,:,:])

XC = grid.read_ecco_field_to_faces(data_folder+'/grid/XC.data',llc=270,dim=2)
YC = grid.read_ecco_field_to_faces(data_folder+'/grid/YC.data',llc=270,dim=2)
runoff = grid.read_ecco_field_to_faces(data_folder+'/era_xx/runoff-2d-Fekete-1deg-mon-V4-SMOOTH.bin',llc=270,dim=2)

for i in range(1,6):
    if i==1:
        points = np.column_stack([XC[i].ravel(), YC[i].ravel()])
        values = np.reshape(runoff[i],(np.size(runoff[i]),1))
    else:
        points = np.vstack([points, np.column_stack([XC[i].ravel(), YC[i].ravel()])])
        values = np.vstack([values, np.reshape(runoff[i], (np.size(runoff[i]),1))])

Lon,Lat = np.meshgrid(lon,lat)
runoff_interp = griddata(points,values.ravel(),(Lon,Lat),method='nearest')
exf_grids.append(runoff_interp)
print(np.max(runoff_interp))


fig = plt.figure(figsize=(8,10))

proj = ccrs.Robinson()
fig,axes = plt.subplots(
    4,2, figsize=(8,10),
    subplot_kw={'projection': proj},#,"aspect": 2
    gridspec_kw = {'wspace':0.03, 'hspace':0.03, 'left':0.11, 'right':0.9, 'top':0.95, 'bottom':0.05},
)

for i in range(len(variable_names)):
    print('Plotting '+variable_names[i])
    plt.subplot(4,2,i+1)

    C = plt.pcolormesh(lon,lat,exf_grids[i],transform=ccrs.PlateCarree(),
                       vmin=meta_dict[variable_names[i]][0],
                       vmax=meta_dict[variable_names[i]][1],
                       cmap=meta_dict[variable_names[i]][2])
    if i%2==0:
        plt.colorbar(C, label=meta_dict[variable_names[i]][3],location='left',fraction=0.026)
    else:
        plt.colorbar(C, label=meta_dict[variable_names[i]][3],fraction=0.026)
    plt.title(variable_names[i])

    plt.gca().add_feature(cfeature.LAND, zorder=99, facecolor='silver')
    plt.gca().coastlines()

output_file = '../images/ecco_exf_fields.png'
plt.savefig(output_file,bbox_inches='tight')
plt.close(fig)




