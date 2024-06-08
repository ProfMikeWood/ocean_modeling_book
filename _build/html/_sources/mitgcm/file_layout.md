# File Layout


The files for a typical MITgcm model configuration are divided into five main directories -- two directories used at compile time and three directories used at run time.


## Compile Time Directories

### code

The code directory is used to store compile-time files that modify the default code in MITgcm. These files fall into three main types
- packages.conf
    - The packages.conf file stores a list of packages that will be loaded into MITgcm. Common packages in MITgcm include diagnostics, exf, etc.
- header files
    - Header files (with the extension .h) define data used across all model scripts. All MITgcm configurations MUST provide a SIZE.h file appropriate for the configuration. All other header files can be used be default although more are often included to define compile time options. 
- source files
    - Source files (with extension .F) define the model code. There are hundreds of scripts that define how the model grids are constructed, how the equations of motions are integrated through time, etc. No source files are strictly required although specialized configurations often include new scripts that modify the source code in MITgcm.

### build

The build directory is used to store all of the compiled code that will be run for the configuration. No files need to be manually added to this directory - when the model code is compiled with the genmake2 tool, this directory will be filled in. When the model code is compiled in the build directory, the model will generate an mitgcmuv file - this key file is the executable for the model run.

## Run Time Directories

### namelist

The namelist directory is used to store "data" files that define runtime parameters for the model run. These runtime files are as follows:
- data
    - Every configuration must have a data file (no extension) that defines the model grid, time-stepping, etc.
- data.pkg
    - Each configuration also needs a data.pkg file that lists which packages which are used in the particular configuration (it's not recommended, but you can compile a package but leave it inactivated).
- eedata
    - Each configurations needs an eedata file that informs the multi-threading for the division of model computations across cpus.
- data.[package] files
    - Each package that is activated in the data.pkg file requires a data.[package] file in the namelist directory to describe its runtime parameters. For exmaple, the diagnostics package requires a data.diagnostics file which describes which output variables are requested along with their output frequencies.


### input

The input directory is used to store binary files which describe the model initialization and other peritent external information required during the model run. There are no strictly required input files but there most configurations have several input files. Some of the common files in this directory include:
- bathymetry
- initial conditions (either a hydrography file or a pickup file)
- external forcing conditions (e.g. wind speed, atmospheric temperature, etc)
- boundary conditions (in the case that the model is a regional model)


### run

The run directory is where the model will output files during the run. These files include descriptions of the model behavior, requested model output, and model checkpoints. The run directory requires all of the files in the namelist and input directories as well as the mitgcmuv from the compiled code in the bulid directory.




