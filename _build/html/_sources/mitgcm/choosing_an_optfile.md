# Choosing an optfile

To compile the MITgcm source code, you'll need to defines paths to your local libraries. These tell MITgcm where to find important files for compilation including those for MPI and netcdf. MITgcm comes with a set of common "optfiles" that provide code to search in a number of locations for the right libraries. As all systems are organized differently, the selection of an optfile depends on the system you're using. Here are some examples:


## Systems

### MacOS
If you are using MacOS with the gfortran compiler, following the instructions [HERE](https://profmikewood.github.io/ocean_modeling_book/getting_started/installing_compiler_and_mpi.html#installation-on-a-mac), then use the **darwin_amd_gfortran** file.

### Windows with Cygwin
If you are using Windows with a Cygwin installation, following the instructions [HERE](https://profmikewood.github.io/ocean_modeling_book/getting_started/installing_compiler_and_mpi.html#installation-on-a-windows-using-cygwin), then use the **linux_amd64_gfortran** file.

### Computing Cluster
The optfile used for compilation on a computing cluster will depend on your cluster's compiler options. There are many options available and they typically need to be paired with modules loaded prior to compiling and running MITgcm.

#### Listing the modules
To list the modules available on your cluster, use the following command:
```
module avail
```

The key modules to load for MITgcm are the modules for MPI and netcdf/hdf5. The latter modules will depend on your MPI version (MPICH, OPMI, etc) and typically need to match. Below are two examples for Pleaides and Spartan, showing two ways to import required modules and choose an associated optfile.

#### Example 1: Spartan

Spartan is the HPC cluster at San Jose State University. On Spartan, load the following modules:

```
module load gnu/6.3.0 netcdf/gnu-6.3.0 mpich/gnu-6.3.0 hdf5/gnu-6.3.0
```

Using these modules, the `linux_amd64_gfortran` optfile works well. Note that the MPI path corresponding to the chosen MPI implementation should be exported before running `genmake2` e.g.

```
export MPI_INC_DIR=/act/mpich/gnu-6.3.0/include/
```

#### Example 2: Pleaides

Pleaides is the NASA HPC cluster. On Pleaides, the following modules have been used for a successful compilation of MITgcm:

```
module load comp-intel mpi-hpe hdf4/4.2.12 hdf5/1.8.18_mpt netcdf/4.4.1.1_mpt
```

Using these modules, the `linux_amd64_ifort+mpi_ice_nas` optfile works well.







