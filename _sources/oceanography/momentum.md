# Momentum

This section is aimed at describing the main terms in the momentum equations which are key for numerical modeling. For derivations of these equations, see one of the sources in the references, such as Chapter 7 of {cite:ts}`stewart2008introduction`.

## Momentum Overview
In ocean modeling, momentum equations describe how the velocity of seawater changes over time due to various forces. These equations are fundamental for simulating ocean circulation patterns, including currents, eddies, and large-scale gyres. They account for forces such as pressure gradients, Earth's rotation (Coriolis force), gravity, and frictional effects. Understanding and accurately representing these forces are crucial for realistic ocean models.

## The Momentum Equations
The momentum equations describe how momentum changes at any given location in the ocean given the forces that act on it. They can be written succintly in vector notation as: 

```{math}
\frac{D\textbf{v}}{Dt} = - \frac{1}{\rho}\nabla p - 2\boldsymbol\Omega\times\textbf{v} + \textbf{g} + \textbf{F}_r
```

In this equation, known as the *Navier-Stokes* equation, the left-hand side is the total derivative of $\textbf{v}$, and the right-hand side terms are the pressure gradient force ($-1/\rho \nabla p$), the Coriolis force ($2\boldsymbol\Omega\times\textbf{v}$), gravity ($\textbf{g}$), and frictional forces (i.e. viscosity, $\textbf{F}_r$). Each of these terms is describe in the following subsections.

The vector notation for these equations can be expanded as

```{math}
\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial x} - 2\Omega v \text{sin}\theta + F_x\\
\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x} + v\frac{\partial v}{\partial y} + w\frac{\partial v}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial y} - 2\Omega u \text{sin}\theta + F_y\\
\frac{\partial w}{\partial t} + u\frac{\partial w}{\partial x} + v\frac{\partial w}{\partial y} + w\frac{\partial w}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial z} + F_z\\
```
Note that the small vertical component of the Coriolis has been removed from ...

### The Pressure Gradient Force
The pressure gradient force arises from spatial variations in pressure within the ocean. It drives fluid from regions of high pressure to low pressure and is a primary mechanism for initiating and maintaining ocean currents. Mathematically, it's represented as:

$$
- \frac{1}{\rho}\nabla p
$$

​
where $\rho$ is the density of seawater and $\nabla p$ is the pressure gradient. This force is essential for modeling geostrophic flows where there is a balance between pressure gradients and Coriolis forces in large-scale ocean circulation.

### The Coriolis Force
Due to Earth's rotation, moving fluids experience an apparent force known as the Coriolis force (or Coriolis "effect"). This force causes moving water to deflect to the right in the Northern Hemisphere and to the left in the Southern Hemisphere, influencing the direction of ocean currents. The Coriolis force is given by:

$$
- 2\boldsymbol\Omega\times\textbf{v}
$$

where $\boldsymbol\Omega$ is Earth's angular velocity vector and $\textbf{v}$ is the velocity of the fluid. In ocean models, incorporating the Coriolis force is important for simulating realistic current patterns and understanding phenomena like the formation of gyres and the behavior of large-scale circulation systems.

### Frictional Forces
Frictional forces in the ocean arise from the viscosity of seawater and interactions with boundaries such as the seafloor and coastlines. These forces act to slow down water movement and dissipate energy, playing a significant role in boundary layers and mixing processes. In ocean modeling, frictional forces are often parameterized using eddy viscosity concepts to represent the effects of turbulence and small-scale mixing that cannot be directly resolved. Accurate parameterization of frictional forces is crucial for modeling vertical mixing, energy dissipation, and the overall momentum balance in the ocean.

## The Boussinesq Approximation 
The Boussinesq approximation for momentum is that sea water is, in effect, incompressible. Put into symbols, this means that

```{math}
\frac{1}{\rho} \frac{D \rho}{D t}  = 0
```

This Boussinesq approximation is often used when constructing numerical ocean models with fixed grids because the grid cells will not change volume due to changes in density. This is an important consideration because in the real ocean, variations in density *do* have a measureable effect on ocean volume. In fact, changes in density resulting primarily from increased ocean heat content are a major contributor to contempory sea level rise {cite:p}`frederikse2020causes`. In effect, hen computing density-driven variations in sea level from ocean state estimates, it's necessary to apply a correction *a posteriori* {cite:p}`greatbatch1994note`.

## The Continuity Equation
Applying the conservation equation to momentum (i.e. the conservation of mass in a given volume) results in:

```{math}
\frac{\partial \rho}{\partial t} + \frac{\partial (\rho u)}{\partial x} + \frac{\partial (\rho v)}{\partial y} + \frac{\partial (\rho w)}{\partial z} = 0
```

This equation is known as the *continuity equation*.

Under the Boussinesq approximation, this is simplified to:

```{math}
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0
```

Or, put another way, the flow into a given region but be equal to the flow out.


