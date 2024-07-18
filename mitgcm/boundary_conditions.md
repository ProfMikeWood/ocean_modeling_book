# Boundary Conditions

Boundary conditions are model state parameters that are applied at the edges of a regional domain. As typical domains are square, the sides of the domain are denoted "north", "south", "east" and "west" corresponding to the top, bottom, right, and left boundaries. However, it should be noted that these directions do not necessarily correspond to the cardinal directions in the model. 

The typical boundary conditions required in a regional model are outlined in the following table:

| Variable | Descrition |
| -------- | ---------- |
| `THETA` | Potential Temperature |
| `SALT` | Salinity |
| `UVEL` | Velocity in the model x-direction |
| `VVEL` | Velocity in the model y-direction |

Note that velocity may still be applied on boundaries when the velocity component is parallel. For example, `UVEL` can still be applied on the southern boundary even though it is parallel to the boundary.

In the case that the model also contains seaice, the following conditions are additionally applied:

| Variable | Descrition |
| -------- | ---------- |
| `AREA` | Sea ice concentration |
| `HEFF` | Effective sea ice thickness |
| `HSNOW` | Effective thickness of snow on sea ice |
| `UICE` | Sea ice velocity in the model x-direction |
| `VICE` | Sea ice velocity in the model y-direction |

## Boundary Condition Options

### Option 1: Global Model
The default behavior for boundary conditions in MITgcm is that the conditions are periodic. In other words, the right side is connected to the left side, and the top is connected to the bottom.

If you would like to generate an enclosed regional model, the most assured way to suppress the periodic behavior is to generate a bathymetry that has 0 depth on all four boundaries. This approach is used in the [MITgcm Barotropic Gyre](https://mitgcm.readthedocs.io/en/latest/examples/barotropic_gyre/barotropic_gyre.html) tutorial.


### Option 2: The OBCS Package
In the case that a regional model is desired, the Open Boundary ConditionS (OBCS) package can be used.

#### `obcs` Compile-Time Considerations
To enable the `obcs` package for compilation, add a line for `obcs` in the `packages.conf` files. 

```{note}
While the `obcs` package does not strictly require the use of the `exf` package, the designation of condition time-stepping is provided in the `data.exf` package and its funtionality was built around tools from the `cal` package. With this in mind, most regional models that use `obcs` also enable the `exf` and `cal` packages by adding these to the `packages.conf` file.
```
By default, the [OBCS_OPTIONS.h](https://github.com/MITgcm/MITgcm/blob/master/pkg/obcs/OBCS_OPTIONS.h) file will allow for the presciption of boundary conditions on all four sides of the model. If you model has fewer boundaries (e.g. one or more is on land), then consider turning off one or more of these options to save time in running the model. For example, if your model does not have an eastern boundary, then consider deactivating this code using the following:
```
#undef ALLOW_OBCS_WEST
```

In addition, the `obcs` package does not activate code for a boundary "sponge" by default. If you would like to add a sponge to your boundaries (see below), then consider including this code in the `OBCS_OPTIONS.h` by modifying the sponge line as follows:
```
#define ALLOW_OBCS_SPONGE
```

#### `obcs` Run-Time Considerations
The data.obcs file is a required file when using the boundary condition package. There is one main parameter list in this file (`&OBCS_PARM01`) which contains the majority of the periment information.

| Namelist | Purpose | 
| -------- | :------ |
| `OBCS_PARM01` | Set parameters for reading and applying boundary conditions |
| `OBCS_PARM02` | Used to provide Orlankski boundary conditions. Not required when Orlanski conditions are turned off. |
| `OBCS_PARM03` | Used to provide sponge parameters. Not required when the sponge code is turned off.  |
| `OBCS_PARM04` | Used to provide Stevens boundary conditions. Not required when Stevens conditions are turned off. |

##### Assigning Boundary Locations
The boundary location assignment is typically provided at the top of the `&OBCS_PARM01` namelist. For each of the boundaries used in the regional model, an array of indices equal to the length of the boundary must be provided. For example, consider a regional domain with 240 columns and 360 rows with open boundaries on the north, south, and west sides of the domain but a closed east side on land. In the case that the bottom row is the southern boundary, the left column is the west boundary, and the top row is north boundary, the locations of the boundaries would be provided as:

```
  OB_Jsouth =   240*1,
  OB_Iwest  =   360*1,
  OB_Jnorth =   240*360,
```

This situation is most common for regional model although there is a lot of flexibility in how the conditions may be applied. For more information, see the [obcs documentation](https://mitgcm.readthedocs.io/en/latest/phys_pkgs/obcs.html).

##### Assigning File Names
The `&OBCS_PARM01` namelist also contains the list of files that will be provided on each boundary. The file names are specified with the letters "OB" then a capital letter corresponding to the boundary, and then a letter or letters corresponding to the vairables, followed by the word file. For example, `OBNtFile` and `OBWsFile` would correspond to the files for `THETA` (t) on the northern (n) boundary and `SALT` (s) on the western (W) boundary. The full list of variable letters is as follows:

| Variable | Letter for file assignment |
| -------- | ---------- |
| `THETA` | t |
| `SALT` | s |
| `UVEL` | u |
| `VVEL` | v |
| `AREA` | a |
| `HEFF` | h |
| `HSNOW` | sn |
| `UICE` | uice |
| `VICE` | vice |

With this convention, the files are identified in the namelist. For example, the files for theta on the northern, southern, and western boundaries may be listed as:
```
 OBNtFile='Theta_north.bin'
 OBStFile='Theta_south.bin'
 OBWtFile='Theta_west.bin'
```
These lines would repeat for each variable being prescribed with boundary conditions in the given file.

##### Balancing Boundary Conditions
One convenient option provided by the `obcs` package is the ability to balance flow through each of the boundaries. While every attempt should be made to balance the conditions when the files are formulated, often differences can arise. The balancing option ensures that no mass is loss or gained in the domain. To run the balancing script, provide the following lines in the `&OBCS_PARM01` namelist:

```
useOBCSbalance = .TRUE.,
```

```{warning}
Mass additions into the domain such as those from precipitation or runoff will not be included in the balancing code by default. In effect, if your mass additions are not equal to your mass loss (e.g. precipitation > evaporation), this will change the volume in your domain and will likely lead to issues. This can be averted by setting `OBCSbalanceSurf = .TRUE.` in `&OBCS_PARM01`.
```

##### Assigning Sponge Parameters

Under construction.

##### Assigning Periodicity

Under construction.

#### Preparing Boundary Condition Fields

Under construction.


