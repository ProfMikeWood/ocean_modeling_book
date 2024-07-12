# Installing gfortran and MPI

To run MITgcm, we will need a FORTRAN compiler. This page describes how to install a common compiler on both MacOS and Windows (using Cygwin)

## Installation on a Mac

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
Note: these need to be checked

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



