# Getting Started with MITgcm


### Downloading MITgcm
To use MITgcm, begin by cloning the repository from Github:
```
git clone mitgcm
```

### Prepping you machine to compile code
Once you have MITgcm on your machine, there's a few steps required to get your machine set up.

At the least, you'll need to have a fortran compiler to compile the model code.

In addition, you will likely want to install MPI to pralleloze your model across CPUs and a netcdf library for storing output into netCDF files.

The set up for each of these components will depend on your system. Here, I've provided two walk-throughs for possible installations for MacOS and Windows. These steps worked in my test cases but you may choose to install differently depending on your system.

Depending on your installation, youll need to select an optfile that passes information to your compiler. 


#### Compiling and Running a Model








