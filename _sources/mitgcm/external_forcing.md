# External Forcing

In MITgcm, the primary way to implement external forcing conditions is through the exf package. 

The external forcing conditions are stored in 3-dimensional grids as (time, Ny, Nx) where (Nx, Ny) is the size of the domain.

### data.exf
The data.exf file outlines 4 namelists to assign exf parameters. 

#### Periodicity

#### Temporal Interpolation

#### Spatial Interpolation
There are a few options for spatial interpolation. One straight-forward method is to manually interpolate the conditions onto the model domaim prior to the model run. In this case, specify the interpolation method as 0 in namelist 4.



