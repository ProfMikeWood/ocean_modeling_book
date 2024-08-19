# Diagnosing Issues

There's a lot that can (and will) go sideways when compiling and running MITgcm. This page details a few common errors and some solutions to diagnose the problems.


## Compile-Time Issues

[Under Construction]

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

