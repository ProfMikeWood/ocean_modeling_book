# Diagnosing Issues

There's a lot that can (and will) go sideways when compiling and running MITgcm. This page details a few common errors and some solutions to diagnose the problems.

[Under Construction]

## Compile-Time Issues

### Missing dylib file

Issue: When running a large model on a system with MacOS, I encountered the following error.
```
dyld[XXXXX]: dyld cache [path] not loaded: syscall to map cache into shared region failed
dyld[XXXXX]: Library not loaded: /usr/lib/libSystem.B.dylib
```
It turned out that the processing tiles were too big for my machine despite the code compiling fine. By reducing the processing tile size, this error was alleviated.

## Run-Time Issues

### Dealing with NaNs
When MITgcm encounters an unexpected NaN in a computation, the NaN will propagate through all fields such that all model output will be NaN. By default, the model will continue running, carrying around all of those NaNs - no good! This behavior can be be suppressed using the `--ieee` flag at compile time, forcing the model to stop running, i.e.

```
../../../tools/genmake2 -of ../../../tools/build_options/darwin_amd64_gfortran -mods ../code -mpi --ieee
```

If desired, the part of the code that triggered the NaN can be discovered by further adding the `--devel` flag at compile time as 

```
../../../tools/genmake2 -of ../../../tools/build_options/darwin_amd64_gfortran -mods ../code -mpi --ieee --devel
```

This functionality will provide a back trace to the location in the code where the NaN was produced, which is very helpful for debugging. Note however that this will slow down the model run considerably, so it's not recommend to compile with this option by default.

### ABNORMAL END: S/R CALC_R_STAR

When using R_STAR coordinates, there is a potential for the model to crash if the layer thickness gets too small or too big. This is particularly prevalent when using sea ice next to the coast.

When this occurs, it's helpful to find where in the model the error occurred in order to adjust the model (e.g. potentially change the topography). The model will print a message where the error occurs, but only in the STDERR file for the tile. To find the tile(s) where the error happened, search for the error with `grep`:

```
grep CALC_R_STAR STDERR*
```
This will show which tiles the error occurred in:
```
STDERR.0112:STOP in CALC_R_STAR : too SMALL rStarFac[C,W,S] !
STDERR.0128:STOP in CALC_R_STAR : too SMALL rStarFac[C,W,S] !
```
Inside the STDERR files, you can see where the error occured, e.g.:
```
fail at i,j=  46   2 ; rStarFacW,H,eta =  0.097682  1.000000E+01 -5.381625E+00 -1.266474E+01
WARNING: r*FacW < hFacInf at       1 pts : bi,bj,Thid,Iter=   1   1   1    241260
STOP in CALC_R_STAR : too SMALL rStarFac[C,W,S] !
```


