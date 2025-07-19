# Getting Started with MITgcm

## Compiling and Running: A test with a verification experiment

MITgcm comes with a series of verification experiments that serve two purposes. On one hand, the experiments are used to test model codes on a nightly basis to ensure any new updates to the model source code maintain the expected functionality of the model. On the other, the verification experiments serve as a set of tutorials that can be used to familiarize yourself with various aspects of the model. 

Following the [MITgcm documentation](https://mitgcm.readthedocs.io/en/latest/), we'll test the model using the Barotropic Gyre Tutorial. Extensive documentation is provided for this experiment on the [Barotropic Gyre Tutorial](https://mitgcm.readthedocs.io/en/latest/examples/barotropic_gyre/barotropic_gyre.html) MITgcm documentation page so we won't repeat all of the details here. Instead, we'll focus on the steps to compile and run the model, with and without MPI.

Begin by moving into the tutorial directory:
```
cd MITgcm/verification/tutorial_barotropic_gyre
```

### Compiling and Running without MPI

#### Compiling without MPI
By default, the experiment will be ready to compile on a single processor (i.e. without MPI). You can verify this in the `code/SIZE.h` file by examining the number of processors are both set to 1:
```
     &           sNx =  62,
     &           sNy =  62,
     ...
     &           nPx =   1,
     &           nPy =   1,
```
In this configuration, the entire size of the domain, 62 rows and 62 columns, is used for the processing tile.

To compile the experiment, move into the build directory:
```
cd build
```

Next, we'll run the three steps common to compilation: 1) running the `genmake2` program, 2) creating a list of dependencies, and 3) compiling the code. These are completed with the following steps:
```
../../../tools/genmake2 -of ../../../tools/build_options/darwin_amd64_gfortran -mods ../code
make depend
make
```

Note here that I've used the `darwin_amd64_gfortran` optfile I've identified for my machine. Be sure to substitute the optfile identified for your system if it is different than mine.

The above commands will output a lot of lines in your terminal and generate a lot of files in your `build` directory. You can ensure your compilation was successful by looking for the `mitgcmuv` file:
```
ls mitgcmuv
```

```{note}
On Windows, the `mitgcmuv` file will have an executable extention `.exe`. This is the same file indicated above.
```

This command should return `mitgcmuv` (and not "No such file or directory") when the compilation is successful.

#### Running without MPI
Now that you've compiled your code, you can run the tutorial. Begin by moving into the run directory:
```
cd ../run
```

Next, we'll link all of the pertinent files to the run directory:
```
ln -s ../input/* .
ln -s ../build/mitgcmuv .
```

With everything in place, we're ready to run! Execute the `mitgcmuv` executable as follows:
```
./mitgcmuv > output.txt
```

The `mitgcmuv` executable will output a lot of information about the model run - the ` > output.txt` addition writes all of this output into the `output.txt` file rather than terminal.

If you get get the following glorious message:
```
STOP NORMAL END
```
you'll know the run is successful. As you continue in your modeling endeavors, seeing this message will start to bring you a mix of joy and relief. There's so many things that can go awry in both compilation and in running the model - seeing this message gives some sense of comfort that you're on the right track.



### Compiling and Running with MPI

#### Compiling with MPI
To modify the experiment to run with MPI, we'll need to update the `SIZE.h` file in the `code` directory. There's already a size file available for compiling with MPI - let's swap out this file for the one we used before
```
cd ../code
mv SIZE.h SIZE.h_no_mpi
mv SIZE.h_mpi SIZE.h
```

We can take a look in the updated `SIZE.h` file by examining the number of processors are now both set to 2 and each processor will take care of 1/4 of the domain:
```
     &           sNx =  31,
     &           sNy =  31,
     ...
     &           nPx =   2,
     &           nPy =   2,
```
For more information on the grids, see the [Defining the Model Grid](https://profmikewood.github.io/ocean_modeling_book/mitgcm/defining_the_grid.html) page.

```{warning}
conda environments have a tendency to interfere with compilation when using MPI. Be sure that you do not have a conda environment activated in your terminal when compiling with MPI i.e. you should not see `(base)` or other environments at the start of your terminal line. If one is activated, use `conda deactivate` to deactivate it.
```

Now that the `SIZE.h` file is updated, we need to recompile the code. Further, since `SIZE.h` is included in essentially every single script, we need to remove all of the previously compiled code and recompile with the previous steps. 
```
cd ../
rm build/*
cd build
../../../tools/genmake2 -of ../../../tools/build_options/darwin_amd64_gfortran -mods ../code -mpi
make depend
make
```

```{note}
When compiling with MPI, be sure to include the `-mpi` flag in `genmake2`
```

#### Running with MPI
Now that the code is compiled, we'll move back to the run directory. However, to avoid confusion with the previous run, remove all of the files from the run directory generated by the run without MPI.
```
cd ..
rm run/*
cd run
```

Just as before, we'll link all of the pertinent files to the run directory:
```
ln -s ../input/* .
ln -s ../build/mitgcmuv .
```

With everything in place, we're ready to run again. We use the `mpirun` command to run the `mitgcmuv` executable, identifying the 4 processors as follows:
```
mpirun -np 4 mitgcmuv
```

If everything goes to plan, you should receive four of the glorious messages:
```
STOP NORMAL END
STOP NORMAL END
STOP NORMAL END
STOP NORMAL END
```

Woohoo!

