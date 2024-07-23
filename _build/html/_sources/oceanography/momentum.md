# Momentum

This section is aimed at describing the main terms in the momentum equations which are key for numerical modeling. For derivations of these equations, see one of the sources in the references, such as Chapter 7 of {cite:ts}`stewart2008introduction`.

## Momentum Overview
Under construction

## The Momentum Equations
The momentum equations describe how momentum change at any given location in the ocean given the forces that act on it. They can be written succintly in vector notation as: 

```{math}
\frac{D\textbf{v}}{Dt} = - \frac{1}{\rho}\nabla p - 2\boldsymbol\Omega\times\textbf{v} + \textbf{g} + \textbf{F}_r
```

In this equation, the left-hand side is the total derivative of $\textbf{v}$, and the right-hand side terms are the pressure gradient force ($-1/\rho \nabla p$), the Coriolis force ($2\boldsymbol\Omega\times\textbf{v}$), gravity ($\textbf{g}$), and frictional forces (i.e. viscosity, $\textbf{F}_r$). Each of these terms is describe in the following subsections.

The vector notation for these equations can be expanded as

```{math}
\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial x} - 2\Omega v \text{sin}\theta + F_x\\
\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x} + v\frac{\partial v}{\partial y} + w\frac{\partial v}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial y} - 2\Omega u \text{sin}\theta + F_y\\
\frac{\partial w}{\partial t} + u\frac{\partial w}{\partial x} + v\frac{\partial w}{\partial y} + w\frac{\partial w}{\partial z} &= - \frac{1}{\rho}\frac{\partial p}{\partial z} + F_z\\
```
Note that the small vertical component of the Coriolis has been removed from ...

### The Total Derivative of Momentum
Under construction

### The Pressure Gradient Force
Under construction

### The Coriolis Force
Under construction

### Frictional Forces
Under construction

## The Boussinesque Approximation
Under construction

## The Continuity Equation
Under construction