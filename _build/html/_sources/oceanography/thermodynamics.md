# Thermodynamics

This section is aimed at describing the main terms in the equations for heat and salt which are key for numerical modeling. 

## Thermodynamics Overview
Under Construction.

## A General Conservation Equation
Heat and salt can both be considered "tracers" in the ocean. At any given location, tracer concentrations $C$ can be described by 

```{math}
\frac{\partial(\rho C)}{\partial t} + \nabla \cdot (\rho C \textbf{u}) = \rho J
```

where $J$ is a local source term. See Chapter 2 of {cite:ts}`mcwilliams2006fundamentals` for further details.

Under the [Boussinesq approximation](https://profmikewood.github.io/ocean_modeling_book/oceanography/momentum.html#the-boussinesq-approximation), the density variations can be removed from the above equation as

```{math}
\frac{\partial C}{\partial t} + \textbf{u} \cdot \nabla C = J
```

## Conservation of Salt
The above conservation equation can be applied to salinity $S$ (kg/m$^3$) in the ocean as 

```{math}
\frac{\partial S}{\partial t} + \textbf{u} \cdot \nabla S = J_S
```

where here, $J_S$ represents sources and sinks of salinity. At the surface of the ocean, salinity can increase as a result of evaporation or brine rejection during the process of sea ice formation. Salinity can also decrease as a result of precipitation, runoff from rivers and ice sheets, and the melting of sea ice. 


## Conservation of Heat
The above conservation equation can also be applied to heat concentration $H$ (J/m$^3$) as 

```{math}
\frac{\partial H}{\partial t} + \textbf{u} \cdot \nabla H = J_H
```

Often, it is advantageous to express heat in terms of temperature $H = \rho C_p \Theta$ where $C_p = 4186$ J kg$^{-1}$ C$^{\circ-1}$. In this case, the conservation equation is expressed as 

```{math}
\frac{\partial \Theta}{\partial t} + \textbf{u} \cdot \nabla \Theta = \frac{J_H}{\rho C_p}
```

At the surface of the ocean, there are various sources and sinks of heat including upwelling and downwelling radiation, and latent and sensible heat fluxes with the atmosphere and sea ice. In addition, geothermal heat provides a source of heat on the ocean floor, primarily near mid-ocean ridges.

### Potential Temperature
In the above conservation equation, temperature ($t$) is expressed as *potential temperature* ($\Theta$) - the temperature of the water parcel if it were moved to the surface without exchanging any heat with its surroundings. It is advantangeous to use potential temperature rather than in situ temperature when building numerical models (and assessing oceanographic conditions in general) because water gains and loses heat as it moves down and up in the water column. This occurs because water compresses under pressure, which induces thermodynamic work on the water parcel. Formulating temperature as potential temperature circumvents this issue.

