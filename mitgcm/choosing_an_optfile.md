# Choosing an optfile

To compile the MITgcm source code, you'll need an optfile that defines paths to your local libraries.


## Systems

### MacOS
If you are using MacOS with gfortran (recommend), them use the darwin_amd_gfortran file

### Windows with Cygwin
If you are using Windows with a Cygwin installation, them use the [] file

### Copmuting Cluster
The optfile used for compilation on a computing cluster will depend on your cluster's compiler. There are many options available and typically need to be paired with module loaded prior to compiling and running MITgcm.

#### Listing the modules
The key modules to load for MITgcm are the modules for MPI and netcdf/hdf5. The latter modules will depend on your MPI version (MPICH, OPMI, etc)

#### Example 1: [Pleaides]

#### Example 2: [Spartan]

##




