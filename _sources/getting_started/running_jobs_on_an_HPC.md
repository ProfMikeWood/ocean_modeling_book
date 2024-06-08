# Running jobs on an HPC

High performance computing clusters typically implement a job queue to manage computations submitted by different users. The two most common job managers for HPCs are slurm and pbs. Each is slightly different but the commands to submit and manage jobs work in essentially the same way. 

## Common Commands
The table below lists the common commands for pbs and slurm.
|----------|-----------|-----------|
| Action | pbs | slurm |
| Check jobs currently in the queue | qstat | squeue |
| Check jobs currently in the queue for a given user | qstat -u user | squeue -u user|
| Submit a job script | qsub script_name | sbatch script_name |
| Cancel a job | qdel job_id | scancel job_id |

### pbs Example
Consider a user `mwood` looking to submit a job called `test_job` on a system managed by pbs.
To submit the job, the user would enter the following from the scratch directory:
```
qsub test_job
```

Then, to check the output, the `qstat -u` command could be used to check the status of the job running on the cluster. 

```{code}
qstat -u mwood
Job ID
```

In this output, we can see the following:
- the job ID name ()
- the user name ()
- the job status (R = Running)
- the total time elapse ()
- the number of nodes in user by the user ()

If the user wanted to cancel the job due to an error noticed in the output, they could run
```
qdel job_ID
```

### slurm Example
This example is almost identical to the pbs example above, revised for slurm. A user `mwood` is looking to submit a job called `test_job` on a system managed by slurm.
To submit the job, the user would enter the following from the scratch directory:
```
sbatch test_job
```

Then, to check the output, the `squeue -u` command could be used to check the status of the job running on the cluster. 

```{code}
qstat -u mwood
Job ID
```

In this output, we can see the following:
- the job ID name ()
- the user name ()
- the job status (R = Running)
- the total time elapse ()
- the number of nodes in user by the user ()

If the user wanted to cancel the job due to an error noticed in the output, they could run
```
scancel job_ID
```

## Creating a Job Script
In the section above, we saw that to submit a job, we'll first need to generate a job script. A job script outlines the time and resources required to run the job and other pertinent parameters.

### Determining the number of CPUs and Nodes
When requesting resources, we need to determine how many CPUs are required for the job. Typically, this is implemented in the construction of the code to be parallelized. In the case of MITgcm, the number of CPUs is the total number of processors identified in the SIZE.h file (nPx*nPy). After the CPUs have been determined, next you need to determine the nodes to request for the job - the key component of the job script. The number of nodes for a job is determined by how many CPUs are on each node - a specification which you will find in the documentation for your HPC. For example, a common configuration is to pair 2 Broadwell processors containing 14 CPUs each as a node, resulting in 28 CPUs per node. Then, the total nodes required for your job is given by
$$$
ceil(nunber of cpus/cpus per node)
$$$

### Job Script Format
A job script typically has three components:
1. Header lines passed to the job management system (e.g. pbs or slurm)
2. Pertinent set-up checks (e.g. purging/loading modules, checking files structures)
3. Running the job executable

#### Example job script for pbs

#### Example job script for slurm

## Assessing a job when its complete
