

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import cmocean.cm as cm

def plot_3D_spiral():
    # didnt end up using this but keeping it here just in case
    ax = plt.figure().add_subplot(projection='3d')

    for i in range(len(z)):
        # a = Arrow3D([0, u[i]], [0, v[i]],
        #             [z[i], z[i]], mutation_scale=20,
        #             lw=3, arrowstyle="-|>", color="r")
        # ax.add_artist(a)
        ax.plot([0, u[i]], [0, v[i]], zs=-1 * z[i], zdir='z', color='dodgerblue')

        angle = np.deg2rad(135)
        ax.plot([u[i], v[i]],
                [u[i] + 0.1 * (np.cos(angle) * u[i] - np.sin(angle) * v[i]),
                 v[i] + 0.1 * (np.sin(angle) * u[i] + np.cos(angle) * v[i])],
                zs=-1 * z[i],
                zdir='z', color='dodgerblue')

        # angle = np.deg2rad(225)
        # ax.plot([u[i], v[i]],
        #         [u[i] + 0.1 * (np.cos(angle) * u[i] - np.sin(angle) * v[i]),
        #          v[i] + 0.1 * (np.sin(angle) * u[i] + np.cos(angle) * v[i])],
        #         zs=-1 * z[i],
        #         zdir='z', color='dodgerblue')

    ax.plot([0, u[i]], [0, v[i]], zs=-1 * z[i], zdir='z', color='dodgerblue', label='Current Speed')

    ax.plot([0, 0], [0, 1.2 * v[0]], zs=0, zdir='z', color='k', label='Wind Stress Direction')
    angle = np.deg2rad(135)
    tu = 0
    tv = 1.2 * v[0]
    ax.plot([tu, tv],
            [tu + 0.1 * (np.cos(angle) * tu - np.sin(angle) * tv),
             tv + 0.1 * (np.sin(angle) * tu + np.cos(angle) * tv)],
            zs=0,
            zdir='z', color='k')

    angle = np.deg2rad(225)
    ax.plot([tu, tv],
            [tu + 0.1 * (np.cos(angle) * tu - np.sin(angle) * tv),
             tv + 0.1 * (np.sin(angle) * tu + np.cos(angle) * tv)],
            zs=0,
            zdir='z', color='k')

    plt.legend()

    ax.set_xlim([0, 0.25])
    ax.set_ylim([-0.05, 0.25])
    ax.set_zlim([100, 0])
    # plt.gca().invert_zaxis()

    ax.set_xlabel('u (m/s)')
    ax.set_ylabel('v (m/s)')
    ax.set_zlabel('Depth (m)')

    plt.show()

def plot_2D_spiral(z, u, v):
    fig = plt.figure()

    xf = np.linspace(np.min(np.abs(z))+1, np.max(np.abs(z)),100)
    yf = xf
    XF, YF = np.meshgrid(xf, yf)
    C = plt.pcolormesh(XF,YF,XF, cmap=cm.deep)
    cbar = plt.colorbar(C, label='Depth (m)')
    cbar.ax.invert_yaxis()

    for i in range(len(z)):
        normalized_depth = -1*(np.abs(z[i]) - np.abs(np.min(z)))/(np.max(np.abs(z))-np.min(np.abs(z)))
        color = cm.deep_r(normalized_depth)
        plt.arrow(0, 0, u[i], v[i], color='k', width=0.004)
        plt.arrow(0, 0, u[i], v[i], color=color, width=0.0033)
        # plt.text(u[i]+0.01, v[i], 'z = '+str(round(z[i]))+' m',
        #          ha='left',va='center')

    plt.arrow(0.04,0.08, 0, 0.10, color='k', width = 0.03,
              head_width = 0.06, head_length = 0.06)
    plt.text(0.04,0.08,'Wind Speed', rotation=90, rotation_mode='anchor',
             ha='left', va = 'center')

    plt.gca().set_xlim([0, 0.25])
    plt.gca().set_ylim([-0.05, 0.25])

    plt.gca().set_xlabel('u (m/s)')
    plt.gca().set_ylabel('v (m/s)')

    plt.savefig('../images/ekman_spiral.png')


windspeed = 20
latitude = 45

V_0 = windspeed*0.0127/np.sqrt(np.sin(latitude))

f=2*7.29e-5*np.sin(latitude)
Az = 0.1
a = np.sqrt(f/(2*Az))

z = -1*np.arange(0,101,10)

u = V_0 * np.exp(a*z)*np.sin(np.pi/4 - a*z)
v = V_0 * np.exp(a*z)*np.cos(np.pi/4 - a*z)

plot_2D_spiral(z, u, v)













