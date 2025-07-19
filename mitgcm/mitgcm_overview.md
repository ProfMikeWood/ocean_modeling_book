# Overview

## Model Description

The MIT General Circulation Model (MITgcm) is a numerical modeling framework developed at the Massachusetts Institute of Technology to simulate ocean and atmosphere dynamics. It solves the three-dimensional [primitive equations](https://profmikewood.github.io/ocean_modeling_book/oceanography/primitive_equations.html) that govern fluid motion on a rotating sphere, enabling the study of both small- and large-scale dynamics. The model is "ultra" versatile (as referenced in the name of its executable, as we will see) and can be configured to represent a wide range of physical domains, from idealized process studies to realistic simulations of the global ocean or atmosphere. It can also handle nonhydrostatic dynamics, allowing it to resolve fine-scale processes such as convection and mixing.

MITgcm can be used on a variety of coordinate systems, including Cartesian and spherical geometries, and uses an Arakawa C-grid for numerical accuracy and conservation properties. It includes both implicit and explicit time-stepping schemes. It is designed for parallel computing on computing clusters, making it suitable for high-performance simulations on large-scale computing systems. The model is widely used in the scientific community for oceanographic and climate research, including studies on ocean circulation, sea ice dynamics, and coupled ocean-atmosphere interactions.


## Model Development
The development of MITgcm began in the 1990s - you can even look back at the [commit list](https://github.com/MITgcm/MITgcm/commits/master/) on Github to see some of the early development at this time! As indicated above, MITgcm was originally created as a research tool to study ocean dynamics and large-scale circulation using a flexible, high-resolution model framework. Early versions focused on ocean-only configurations, with an emphasis on numerical accuracy and the ability to handle realistic boundary conditions and complex geometries. However, early on, the model was designed to support simulations constrained by observational data, particularly for ocean state estimation efforts (that later become [ECCO](https://profmikewood.github.io/ocean_modeling_book/ecco/ecco_overview.html)). Even today, MITgcm is undergoing constant improvements with new features and packages added all the time. If you're using MITgcm consistently, be sure to stay up-to-date on the latest commits - they come quick!


## "Downloading" MITgcm
To use MITgcm, begin by opening up a terminal window and navigating to a location on your computer where you will keep a copy of the model. For example, `~/Documents/Projects/Ocean_Modeling`.

Then, clone the MITgcm source code from the Github repository:
```
git clone https://github.com/MITgcm/MITgcm
```

## Prepping your machine to compile code
Once you have MITgcm on your machine, there's a few steps required to get your machine set up.

At the least, you'll need to have a fortran compiler to compile the model code. In addition, you will likely want to install MPI to parallelize your model across CPUs and a netcdf library for storing output into netCDF files. The set up for each of these components will depend on your system. [HERE](https://profmikewood.github.io/ocean_modeling_book/getting_started/installing_compiler_and_mpi.html), I've provided walk-throughs for possible installations on a variety of systems. These steps worked in my test cases but you may choose to install differently depending on your system.

Once your installations are complete, you'll need to identify an "optfile" that passes information to your compiler. Details for selecting an optfile are available [HERE](https://profmikewood.github.io/ocean_modeling_book/mitgcm/choosing_an_optfile.html). For example, on my system (MacOS with gfortran), I will use the `darwin_amd64_gfortran` optfile.

After these steps are tackled, you're ready to start modeling! We'll see how to compile code and run a model using a tutorial experiment provided with MITgcm in the next notebook. Let's go!




