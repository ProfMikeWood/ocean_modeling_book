# Initial Conditions

When starting up an ocean model, the model needs to know where to start from. The initial conditions typically include the following fields:
- Temperature
- Salinity
- Zonal and Meridional Velocity
- Sea Surface Height

Additionally, the model will also need information about other additional fields implemented in the model configuration, such as sea ice, passive tracers, or other fields for the model run.

## Prescribing Initial Conditions

There are three main ways to prescribe initial conditions in MITgcm:
1. Reference Conditions
2. Hydrography Conditions
3. Pickup Files

The first two options are used when the model is initialized at `nIter=0`; otherwise, the third option must be used.

### Option 1: Reference Condition
When `nIter=0` and no conditions are provided, the model will be initialized with the conditions specified as `tRef` and `sRef` provided in the `&PARM01` namelist of the `data` file. `tRef` and `sRef` are a list of temperatures and salinities with length `Nr`, the number of the depth levels in the model. In this case, the model will initialize the velocity as zero and the sea surface height as 0.

### Option 2: Hydrography Conditions
To specify initial conditions when `nIter=0`, the user can generate 3D fields and provide the file names in the `&PARM05` namelist of the data file. Specifically, the following variable names can be specified:

| Variable | File Name |
|----------|-----------|
| Temperature (THETA) | `hydrogTheta` |
| Salinity (SALT) | `hydrogSaltFile` |
| Zonal Velocity (UVEL) | `uVelInitFile` |
| Meridional Velocity (VVEL) | `vVelInitFile` |
| Sea Surface Height (ETAN) | `pSurfInitFile` |

If any of the above files are not specified, the model will default to option 1.

Each file should store a single binary grid of size (Nr, Ny, Nx), here written in Pythonic ordering (i.e. if the grid were a numpy array, then np.shape would return (Nr, Ny, Nx)). The only exception is the sea surface height field, which has a shape of (1, Ny, Nx).

### Option 3: Pickup Files
When `nIter1` is not 0, then the model is interpreted as coming into the simulation in the middle of a run and will look for a pickup file. A pickup file has the 5 standard fields mentioned above plus 5 more for tendencies. In commonly-used configurations, the pickup fields are stacked in the following order: UVEL, VVEL, THETA, SALT, GUM1, GVM1, GUM2, GVM2, ETAH, DETAHDT, ETAN. Here, G represents the tendencies of U and V at the previous 2 timesteps before the pickup iteration (M1 and M2). If you would like to start a model at a different iteration than 0 (possibly to initialize the model at a given date when working with the cal package), then these fields can be constructed and stacked into a pickup file. The grids are stacked along the depth dimension so that the total grid has a size (8*Nr+3, Ny, Nx). 


