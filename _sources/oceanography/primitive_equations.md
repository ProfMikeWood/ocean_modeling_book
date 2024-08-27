# Primitive Equations

## Overview
Primitive equations refer to the set of complete mathematical equations that describe the heat, salt, mass, and momentum at any given location in the ocean. They are formulated using conservation laws for energy, momentum, and mass. Further, they are linked with the equation of state. Here, the equations are collected in one place to provide a concise overview. The next three subsections for Momentum, Thermodynamics, and Equation of State describe the terms of these equations with some details about how they are derived.

## The Equations

Under Construction.

```{math}
\frac{D\textbf{v}}{Dt} &= - \frac{1}{\rho}\nabla p - 2\boldsymbol\Omega\times\textbf{v} + \textbf{g} + \textbf{F}_r\\
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} &= 0\\
\frac{\partial S}{\partial t} + \textbf{u} \cdot \nabla S &= J_S\\
\frac{\partial \Theta}{\partial t} + \textbf{u} \cdot \nabla \Theta &= \frac{J_H}{\rho C_p}\\
\rho &= f(T,S,p)
```

### Notation
Under Construction.


Here we define the symbology used in the above equations and subsequent sections:

| Symbol | Variable | Typical Units |
| ------ | -------- | ------------- 
| x, y, z  | Cooridinates for zonal, meridional, and veritical directions | meters |
| u, v, w | Fluid velocity in the zonal, meridional, and vertical directions | meters per second |
| $\rho$ | Density | kg/m$^3$ |
| g | Gravitational Acceleration | m/s$^3$ |
| $\Theta$ | Potential Temperature | $^{\circ}$C |
| S | Practical Salinity | psu |

## The Total Derivative
Under Construction.