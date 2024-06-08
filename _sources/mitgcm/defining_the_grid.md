# Defining the Model Grid

To model grid for a simulation needs to be configured in be configured at both compile time and run time. There are two main options for configuring grids -- regular grids and more complex grids using the exch2 package.

## Rectangular Grids

The key compile time file for generating the model grid is the `SIZE.h` file. A custom `SIZE.h` file must be created for each model configuration otherwise the model will not compile.

### Compile time files for regular grids
When using a rectangular grid, the total grid shape will be (Nr, Ny, Nx) where Nr is the number of depth cells, Ny is the number of rows in the model grid, and Nx is the number of columns. In the SIZE.h file, Nr is specified directly. However, Nx and Ny are a function of how the grid is paritioned for parallelization. If the model is only going to be run on one CPU, then set sNx = Nx and sNy = Ny in the SIZE.h file.

When partitioning the grid to be run in parallel, the domain is divided into tiles of size (sNy, sNy) where sNy is the number of rows in the tile and sNx is the number of columns. Each tile will be run on a separate CPU with Px processors in the x direction and Py in the y direction. In this case, `Nx = sNx*Px` and `Ny = sNy*Py`. There is also an option for multi-threading but this is not commonly used, particularly on computing clusters when multiprocessing is used.

### Runtime files for regular grids
There are several options for generating a regular model grid. Most options are specified in the `data` file.

#### Evenly-spaced grids
When using a simple evenly-spaced grid, ...
PARM04
```
usingCartesianGrid=.TRUE.,
delX=62*20.E3,
delY=62*20.E3,
xgOrigin=-20.E3,
ygOrigin=-20.E3,
```

## Grids with exch2

### Compile time files for exch2
The exch2 package offers a more flexible way to construct model grids, allowing for the partitioning of a model grid into model "faces". This option is commonly used for large global models, such as the Lat-Lon-Cap grid used in the ECCO State Estimates. One major upshot of the exch2 package is that it allows for the use of "blank tiles" - tiles that are in the model grid but should not be included in the procssing. This is most common when there are no wet cells in the particular tile.  

When using exch2, the tile sizes are specified in sNx and sNy just like the rectangular grid case. However, in the exch2 geometry, all of the tiles are stacked in the x-direction - Px is set as the number of non-blank tiles and Py is set to 1. Nr is still the number of vertical levels in the model.

Note that when using the exch2 package, exch2 must be added to the list of packages in the packages.conf file.




