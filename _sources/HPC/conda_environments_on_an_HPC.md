# conda Environments

On our local machines, we used conda environments to manage Python and various versions of packages for our work. In this case, conda is installed on our machine and usable anywhere. However, that's not going to be the case for HPCs where the modules are created for all users - it wouldn't make much sense to install a conda environment for each individual user on the main HPC. This page explains how to create a conda environment on our head node and use it in our jobs submitted to the compute nodes.

Note that the first part of this page comes from Ryan Abernathy's medium post [HERE](https://rabernat.medium.com/custom-conda-environments-for-data-science-on-hpc-clusters-32d58c63aa95).

## Installing Miniconda
Just as we did for our [local machines](https://profmikewood.github.io/ocean_modeling_book/getting_started/setting_up_python_and_jupyter.html), we can use the slimmed-down version of miniconda for installation in our home directory. Using miniconda is particularly advantageous here since we don't want to store large amounts of data or files in our home directory. Following the post linked above, we can download miniconda with

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
```

and install it with the shell script:

```
bash miniconda.sh -b -p $HOME/miniconda export 
```

## Create a conda Environment
Now that miniconda is installed, we can create our conda environment. First, let's make sure that miniconda is on our path:

```
PATH="$HOME/miniconda/bin:$PATH"
```

Next, create en environment file called `environment.yml` with the name of the environment and the packages you need. For example, a version of the cs185c environment used for this book might be:

```
>cat environment.yml
name: cs185c
dependencies:
  - python == 3.10
  - numpy
  - scipy
  - xarray
  - netcdf4
  - matplotlib
```

When you have this file ready, you can create the environment with the following line:

```
conda env create --file environment.yml
```

## Using a conda environment in a job
Now that the conda environment is created, you can use it in a job. For example, consider that you have a script called `postprocessing.py` that you would like to run on just a single CPU. If you're using `slurm`, an example job script might be:

```
#!/bin/bash
#SBATCH --partition=nodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00

export PATH="$HOME/miniconda/bin:$PATH"

source activate cs185c

python3 postprocessing.py
```

Note that the script ensures that miniconda is on the path and that the conda environment is activated before the python script is run.

