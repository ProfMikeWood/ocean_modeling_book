# Installing a compiler with MPI

To run MITgcm, we will need two cruicial components: a fortran compiler and a version of MPI. This page describes how to install these items on MacOS, Windows (using Cygwin), and Linux (Ubuntu).

The compiler is used to translate the fortran MITgcm source code into code that can be run on your machine. Message Passing Interface (MPI) is a framework to allow for the parallelization of the model code, dividing portions of the model across different CPUs.

```{warning}
conda environments have been reported to potentially interfere with the installation of compilers. Be sure that you do not have a conda environment activated in your terminal when following the installation instructions below i.e. you should not see `(base)` or other environments at the start of your terminal line. If one is activated, use `conda deactivate` to deactivate it.
```

## Installation on a Mac

On a Mac, installation of the compiler and MPI are made considerably easier using the homebrew package manager.

### Install Homebrew
If you haven't already done so, install homebrew following the instruction at https://brew.sh/. This will involve copying the command from the main page of homebrew and running it in your Terminal. Then, when the installation is complete, be sure to run the final three lines that are output from the installation script.

### Install gcc
Next, use homebrew to install gcc
```
brew install gcc
```
Then, add the following lines to the `.bash_profile`. 
```
export CC=gcc
export CXX=g++ 
export GDFONPATH=/Library/Fonts
export OS=OSX
export LC_ALL="C"

export LDFLAGS="-L/opt/homebrew/opt/curl/lib"
export CPPFLAGS="-I/opt/homebrew/opt/curl/include"
export C_INCLUDE_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include
export CPLUS_INCLUDE_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include
export LIBRARY_PATH=$LIBRARY_PATH:/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib
```
In newer versions of the MacOS, the terminal uses `zshell` by default. If this is the case then add the following line in the `~/.zschrc` file to source the `.bash_profile` on startup:
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

To determine the location where your `openmpi` is installed, check the head of the path using
```
brew config
```
and looking for the line with
```
HOMEBREW_PREFIX: /opt/homebrew
```


When you have identified your path, you can check the installation with
```
/opt/homebrew/Cellar/open-mpi/5.0.3_1/bin/mpirun --version
```
Note that your path may differ.

Next, using this path, add the `openmpi` paths to your `.bash_profile`:
```
export MPI_INC_DIR="/opt/homebrew/Cellar/open-mpi/5.0.3_1/include"
export PATH="$PATH:/opt/homebrew/Cellar/open-mpi/5.0.3_1/bin"
export PKG_CONFIG_PATH="/opt/homebrew/Cellar/open-mpi/5.0.3_1/lib/pkgconfig"
export MPI_HOME="/opt/homebrew/Cellar/open-mpi/5.0.3_1/lib/"
export TMPDIR="/tmp"
```
 

#### Checking your MPI Installation
To check your MPI installation and your paths, open up a new terminal and use the following command:

```
mpirun -np 4 uname
```

Your terminal should print 4 versions of your operating system, e.g.

```
Darwin
Darwin
Darwin
Darwin
```

## Installation on a Windows (using WSL)
One way to install a fortran compiler on a Windows machine is using the Windows Subsystem for Linux - a Linux distribution for Windows.

To install WSL, follow the instructions [HERE](https://learn.microsoft.com/en-us/windows/wsl/install), opening a Powershell terminal from your start menu and running the following command:

```
wsl --install
```

Note that you can install different Linux distributions but the default will be Ubuntu (recommended). After the installation has completed, you will be able to open your Linux distribution from the start menu (e.g. search for Ubuntu if you used the default wsl installation). Note that you will need to make a new "user" for Ubuntu with a password - this is separate from your windows user name and password. Its recommended that you create your username without spaces to avoid issues with your path.

Once you have your terminal open, use the Linux instructions below corresponding to your installation. For example, if you used the Ubuntu distribution, then follow the [instructions for Ubuntu](https://profmikewood.github.io/ocean_modeling_book/getting_started/installing_compiler_and_mpi.html#installation-on-linux-ubuntu) below. 

```{admonition} WSL Note
When opening your Ubuntu terminal, you will be in your `$HOME` directory i.e. something of the form `/home/mwood`. To change directories from this directory to your `C:` drive, you can use `cd $HOME/../../mnt/c`.
```


## Installation on a Windows (using Cygwin)
One way to install a fortran compiler on a Windows machine is using the Cygwin terminal. 

### Install Cygwin with required packages
If you haven't already done so, install Cygwin by running the executable on the [Cygwin installation page](https://www.cygwin.com/install.html). All of the default installation options are typically fine. 

For the mirroring site, choose a site near where you are located. I chose mirrors.kernels.org because it is located in California but you may like to choose a different option depending on your location.

When it comes to the package selection screen, add the list of packages in the following table. The version numbers were the most recent up-to-date files when attemped in Fall 2024.

| Package | Version |
| ------- | ------- |
| gcc-fortran | 12.4.0-3 |
| libnetcdf-fortran-devel | 4.6.1-1 |
| netcdf | 4.6.1-1 |
| netcdf-fortran-debuginfo | 4.6.1-1 |
| openmpi | 4.1.6-1 |
| git | 2.45.1-1 |
| tsch | 6.24.10-1 |
| gcc-g++ | 12.4.0-3 |
| vim | 9.0.2155-2 |
| nano | 4.9-1 |
| make | 4.4.1-2 |
| makedepend | 1.0.9-1 |
| pkg-config | 2.2.0-1 |
| dos2unix | 7.5.2-1 |

To add a package to the installation list, choose "Full" from the drop-down in the upper-left corner. Then, use the search feature to find the package. If the line for the package says "Skip", use drop-down to choose the most recent (non-Test) version. After you have selected the packages, they should all show up under the "Pending" tab. After verifying all packages will be installed, choose next and continue clicking through the installation.

At this point, you will be able to run MITgcm without MPI.


```{admonition} Cygwin Note 1
Compiling MITgcm on Windows using Cygwin is considerably slower than compiling on a native linux machine. Use this option as a back-up in case the WSL option above is not working. 
```

```{admonition} Cygwin Note 2
When opening your Cygwin terminal, you will be in your `$HOME` directory i.e. something of the form `/home/mwood`. To change directories from this directory to your `C:` drive, you can use `cd $HOME/../../cygdrive/c`.
```


### Configuring MPI on Cygwin
Under construction.

## Installation on Linux (Ubuntu)
On Ubuntu, the installation is straight-forward using `apt`.

### Install the Compiler
To install the compiler tools, use the following:
```
sudo apt install gcc 
sudo apt install gfortran
sudo apt install build-essential
```

### Install MPI
To install the MPI tools, use the following:
```
sudo apt-get install openmpi-bin openmpi-doc libopenmpi-dev
```

## Installation on Linux (Arch Linux or Arch-based distros)

On Arch-based Linux distributions, the installation is straight-forward using the `pacman` package manager. However, on Arch-based systems, the installation is a bit more involved. Here are the steps to install MITgcm on Arch-based systems.

### Install Compiler

To compile MITgcm, you need a Fortran compiler. Download the GNU Compiler Collection package [
`gcc`](https://archlinux.org/packages/?name=gcc) and the Fortran front-end [
`gcc-fortran`](https://archlinux.org/packages/?name=gcc-fortran).

```shell
sudo pacman -S gcc gcc-fortran
```

### Install NetCDF

MITgcm uses the NetCDF library to read and write data. Download the NetCDF package [
`netcdf`](https://archlinux.org/packages/?name=netcdf), the Fortran interface [
`netcdf-fortran`](https://archlinux.org/packages/?name=netcdf-fortran), and the HDF5 library [
`hdf5`](https://archlinux.org/packages/?name=hdf5).

```shell
sudo pacman -S netcdf netcdf-fortran hdf5
```

### Install OpenMPI

MITgcm uses the OpenMPI library for parallel computing. Download the OpenMPI package [
`openmpi`](https://archlinux.org/packages/?name=openmpi).

```shell
sudo pacman -S openmpi 
```

#### Checking your MPI Installation

To check your MPI installation and your paths, open up a new terminal and use the following command:

```shell
mpirun -np 4 uname
```

Your terminal should print 4 versions of your operating system, e.g.

```shell
Linux
Linux
Linux
Linux
```
