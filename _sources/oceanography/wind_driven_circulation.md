# Wind-Driven Circulation

A large part of the upper-ocean circulation is driven by wind blowing across the ocean surface. The page provides a brief overview of atmospheric circulation and its role in setting up circulation at the ocean surface.


## Synoptic-scale Atmospheric Circulation
The following plots show the annual mean wind speed at 10 m from the ERA5 climatte model:

Plot here

As we can see from the plot above, surface winds fall into three primary cells in each hemisphere: a westward equator-ward flow between 0 and 30 degrees, an eastward poleward flow between 30 and 60 degrees, and a polar flow moving westward. This general flow forms the surface components of the Hadley, Ferrel, and Polar circulation cells, respectively.



## The Coriolis "Force"
Another observation that can be gleaned from the above wind plot is that in the northern hemisphere, equatorward flow is directed to the west and polarward flow is directed to the east. Put another way, the flow is directed to the right of its meridional flow. The situtation is opposite in the southern hemispehre - the meridional flow is deflected to the left.

This effect, known as the **Coriolis Force**, is the apparent deflection of moving objects on the surface of a rotating body. It is describe as a "force" in that it exerts an apparent acceleration on moving objects although it is not an actual force. For this reason, it some sometimes referred to as the *Coriolis effect*.

The magnitude of the Coriolis force can be expressed in terms of the latitude and the angular rotational speed of the planet, i.e.

```{math}
    f = 2\Omega \sin \theta
```

where $\Omega = 10^{-5}$ s$^{-1}$ is the angular rotation of Earth and $\theta$ is the latitude. 


## Wind Stress on the Ocean Surface
As wind blows arcross the ocean surface, friction between the air and ocean generates a shear on the ocoean surface, known as wind stress. Wind stress is found to be roughly propotional to the wind speed as

```{math}
    \tau_{yy} =
```


## Ekman Transport
Much like the atmosphere, the currents induced by wind stress on the ocean surface are subject to the Coriolis force, meaning they are deflected to the right (left) in the northern (southern) hemisphere. The equations describing ocean current components resulting from a northward windstress are

```{math}
u & = V_0 e^{az} sin(\pi /4 − az)\\
v &= V_0 e^{az} cos(\pi /4 − az)
```\end{align}```

where

```{math}
V_0 = \frac{\tau_{yy}}{\rho_w^2 f A_z} \text{ and } a = \sqrt{\frac{f}{2A_z}}
```

These equations were derived by {cite:ts}`ekman1905influence` by assuming that over large horizontal spatial scales and in steady state, the dominant terms in the momentum equation near the ocean surface are the Coriolis force and friction. The equations here are reproduced from Chapter 9 of {cite:ts}`stewart2008introduction` where further information can be found regarding the history and defailts of the derivation.

There are many implications of these observations but for the purposes of the surface ocean where $z=0$, we can see that

```{math}
u & = V_0  \frac{\sqrt{2}}{2}\\
v &= V_0 \frac{\sqrt{2}}{2}
```

In other words, the *surface ocean currents flow at an angle 45$^{\circ}$ relative to the wind stress direction*. This observation is critical in assessing the surface ocean flow relative to that of the atmosphere.


## Synoptic-Scale Ocean Circulation
The above component - atmospheric circulation at the ocean surface, the Coriolis effect, and the resulting Ekman transport - lead to the large-scale circulation patterns in the ocean surface. Below is a plot of the mean surface velocity from the ECCO Version 4 State Estimate:

Plot here

What we see is a rotational circulation pattern in each of the major sub tropical oceans: the North and South Pacific, the North and South Atlantic, and the Indian Ocean. These circulation patterns are the ocean gyres.

Here, I describe the connections that lead to the formation of the North Pacific gyre - the other gyres are similar.



