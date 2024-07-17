# Installing a compiler with MPI

To run MITgcm, we will need two cruicial components: a fortran compiler and a version of MPI. This page describes how to install these items on both MacOS and Windows (using Cygwin).

The compiler is used to translate the fortran MITgcm source code into code that can be run on your machine. Message Passing Interface (MPI) is a framework to allow for the parallelization of the model code, dividing portions of the model across different CPUs.

## Installation on a Mac

On a Mac, installation of the compiler and MPI are made considerably easier using the homebrew package manager.

### Install Homebrew
If you haven't already done so, install homebrew following the instruction at https://brew.sh/.

### Install gcc
Next, use homebrew to install gcc
```
brew install gcc
```
Then, add the following lines to the .bash_profile. 
```
export CC=gcc
export CXX=g++ 
export GDFONPATH=/Library/Fonts
export OS=OSX
export LC_ALL="C"
```
In newer versions of the MacOS, the terminal uses `zshell` by default. If this is the case then add the following line in the ~/.zschrc file to source the bash_profile on startup:
```
source ~/.bash_profile
```

### Install NetCDF
```
brew install hdf5
brew install netcdf
```

### Install OMPI
Next, we will install MPI to leverage multiple CPUs to run our model. Again, we can use the distribution via homebrew:
```
brew install openmpi
```
You can check the installation with your 
```
/opt/homebrew/Cellar/open-mpi/5.0.3_1/bin/mpirun --version
```
Next, add the openmpi paths to the bash_profile
```
export MPI_INC_DIR="/opt/homebrew/Cellar/open-mpi/5.0.3_1/include"
export PATH="$PATH:/opt/homebrew/Cellar/open-mpi/5.0.3_1/bin"
export PKG_CONFIG_PATH="/opt/homebrew/Cellar/open-mpi/5.0.3_1/lib/pkgconfig"
export MPI_HOME="/opt/homebrew/Cellar/open-mpi/5.0.3_1/lib/"
export TMPDIR="/tmp"
```
Note that your homebrew path may differ. You can check the head of the path suing
```
brew config
```
and looking for the line with
```
HOMEBREW_PREFIX: /opt/homebrew
```

### Format the bash profile
Finally, we will add some additional paths to the ~/.bash_profile file:
```
export LDFLAGS="-L/opt/homebrew/opt/curl/lib"
export CPPFLAGS="-I/opt/homebrew/opt/curl/include"
export C_INCLUDE_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include
export CPLUS_INCLUDE_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include
export LIBRARY_PATH=$LIBRARY_PATH:/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib
```


## Installation on a Windows (using Cygwin)
One way to install a fortran compiler on a Windows machine is using the Cygwin terminal. 

### Install Cygwin with required packages
If you haven't already done so, install Cygwin by running the executable on the [Cygwin installation page](https://www.cygwin.com/install.html). All of the default installation options are typically fine. 

For the mirroring site, choose a site near where you are located. I chose mirrors.kernels.org because it is located in California but you may like to choose a different option depending on your location.

When it comes to the package selection screen, add the list of packages in the following table. The version numbers were the most recent up-to-date files when I 

| Package | Version |
| ------- | ------- |
| gcc-fortran | X.X |
| netcdf | X.X |
| openmpi | X.X |
| git | X.X |
| tsch | X.X |
| gcc-g++ | X.X |
| vim | X.X |
| make | X.X |
| pkg-config | 2.2.0-1 |

To add a package to the installation list, choose "Full" from the drop-down in the upper-left corner. Then, use the search feature to find the package. If the line for the package says "Skip", use drop-down to choose the most recent (non-Test) version. After you have selected the packages, they should all show up under the "Pending" tab. After verifying all packages will be installed, choose next and continue clicking through the installation.

At this point, you will be able to run MITgcm without MPI. To use MIT, continue on to the following step.

### Configuring MPI


```{note}
Compiling MITgcm on Windows using Cygwin is considerably slower than compiling on a native linux machine. I have provided these notes as *a* possible way the MITgcm could be used on Windows. If you have discovered a quicker way, please let me know by raising an issue on the [Github repository](https://github.com/ProfMikeWood/ocean_modeling_book) for this site to explain how you did it!
```
