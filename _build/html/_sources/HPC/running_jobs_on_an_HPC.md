# Running jobs on an HPC

High performance computing clusters typically implement a job queue to manage computations submitted by different users. The two most common job managers for HPCs are slurm and pbs. Each is slightly different but the commands to submit and manage jobs work in essentially the same way. 

## Creating a Job Script
In the section above, we saw that to submit a job, we'll first need to generate a job script. A job script outlines the time and resources required to run the job and other pertinent parameters.

### Determining the number of CPUs and Nodes
When requesting resources, we need to determine how many CPUs are required for the job. Typically, this is implemented in the construction of the code to be parallelized. In the case of MITgcm, the number of CPUs is the total number of processors identified in the SIZE.h file (`nPx`*`nPy`). After the CPUs have been determined, next you need to determine the nodes to request for the job - the key component of the job script. The number of nodes for a job is determined by how many CPUs are on each node - a specification which you will find in the documentation for your HPC. For example, a common configuration is to pair 2 Broadwell processors containing 14 CPUs each as a node, resulting in 28 CPUs per node. Then, the total nodes required for your job is given by

$
\text{ceiling}\left(\frac{\text{nunber of cpus}}{\text{cpus per node}}\right)
$

### Job Script Format
A job script typically has three components:
1. Header lines passed to the job management system (e.g. pbs or slurm)
2. Pertinent set-up checks (e.g. purging/loading modules, checking files structures)
3. Running the job executable

#### Example job script for slurm for MITgcm
```
> cat test_job
#!/bin/bash
#SBATCH --partition=nodes
#SBATCH --nodes=5
#SBATCH --ntasks=140
#SBATCH --time=120:00:00
#SBATCH --first.last@email.com
#SBATCH --mail-type=ALL

module purge
module load gnu/6.3.0 netcdf/gnu-6.3.0 mpich/gnu-6.3.0 hdf5/gnu-6.3.0
ulimit -s unlimited

mpiexec -np 140 ./mitgcmuv
```


#### Example job script for pbs for MITgcm
```
> cat test_job
#!/bin/csh
#PBS -l select=11:ncpus=28:model=bro
#PBS -l walltime=120:00:00
#PBS -q long
#PBS -j oe
#PBS -m abe
#PBS -W group_list=sXXXX
#PBS -M first.last@email.com

module purge
module load comp-intel mpi-hpe hdf4/4.2.12 hdf5/1.8.18_mpt netcdf/4.4.1.1_mpt

mpiexec -np 307 ./mitgcmuv
```

## Common Commands
The table below lists the common commands for pbs and slurm.
| Action | slurm | pbs |
| ---------- |----------- |----------- |
| Check jobs currently in the queue | squeue | qstat |
| Check jobs currently in the queue for a given user | squeue -u user | qstat -u user | 
| Submit a job script | sbatch script_name | qsub script_name | 
| Cancel a job with ID job_id | scancel job_id | qdel job_id | 

### slurm Example
Consider a user `mwood` looking to submit a job called `test_job` on a system managed by slurm.
To submit the job, the user would enter the following from the scratch directory:
```{code}
sbatch test_job
```

Then, to check the output, the `squeue -u` command could be used to check the status of the job running on the cluster. 

```{code}
qstat -u mwood
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           2545870     nodes test_job    mwood  R      11:18      5 node[17-21]
```

In this output, we can see the following:
- the job ID name (2545870)
- the user name (mwood)
- the job status (R = Running)
- the total time elapsed (11:18)
- the number of nodes in use by the user (5)

If the user wanted to cancel the job due to an error noticed in the output, they could run
```
scancel 2545870
```


### pbs Example
This example is almost identical to the pbs example above, revised for pbs. Now, a user `mwood` is looking to submit three jobs called `test_job_1`, `test_job_2`, and `test_job_3` on a system managed by pbs. To submit the jobs, the user would enter the following from the scratch directory:
```
qsub test_job_1
qsub test_job_2
qsub test_job_3
```

Then, to check the output, the `qstat -u` command could be used to check the status of the job running on the cluster. 

```{code}
qstat -u mwood
                                                   Req'd       Elap
JobID           User   Queue Jobname    TSK Nds    wallt S    wallt Eff
--------------- -----  ----- ---------- --- --- -------- - -------- ---
00000001.pbspl1 mwood  long  test_job_1 308  11 5d+00:00 R    11:18 99%
00000002.pbspl1 mwood  long  test_job_2 308  11 5d+00:00 Q 2d+11:16  --
00000003.pbspl1 mwood  long  test_job_3 280  10 5d+00:00 Q    33:22  --
```

In this output, we can see the following:
- the job IDs  (00000001.pbspl1, 00000002.pbspl1, 00000003.pbspl1)
- the user name (mwood)
- the job status (R = Running, Q = Queued)
- the total time elapsed (e.g. 11:18)
- the number of nodes (Nds) requested by the user (11)

If the user wanted to cancel the job `test_job_1` due to an error noticed in the output, they could run
```
qdel 00000001.pbspl1
```

## Assessing a job when its complete

When a job is complete, the job management system will provide a file that contains all of the output and some summative information on the run.

On slurm, the file will be named `slurm-[jobID].out`. For the example given above, this would be `slurm-2545870.out`. On pbs, the file will be named `[jobname].[jobnumber]`. For the example given above, the file would be named `test_job_1.o00000001`.


