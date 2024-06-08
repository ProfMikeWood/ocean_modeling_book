# Navigating an HPC

This page outline how to navigate a high performance computing environment. 

## Directory Structure

In a typical HPC environment, each user is provided with two main directories -- a home directory and a scratch or directory.

### The Home Directory

The home directory on a cluster is the first directory you will land in when you log into the computing cluster. Typically, many users will have a home directory on the same node with shared -- and therefore limited -- storage. Since storage is limited, your home directory should not be used to store any large files or data. Instead, it should be used to manage configuration files, such as a .bash_profile, or perhaps a small installation of miniconda in the case that Python is not available on your HPC. You may also choose to keep a few simple scripts, such as example scripts for loading modules or submitting jobs. 

```{note}
You should never submit a job from your home directory.
```

### The Scratch Directory

The scratch directory -- sometimes called a nobackup directory -- is used to store code and data, and submit jobs. These directories are connected to large storage systems and you can check your storage allocation which is typically on the order of 1 TB or more. However, since the storage system is large, these directories are not typically backed up so you should be sure to copy inportant files to your local machine to ensure you don't lose any crucial data. In your scratch directory, you are free to upload data and manage codes and files as you see fit. Your scratch directory is yours and can't be edited by other users unless you give them permission.

```{note}
You should never run codes on an HPC without submitting job. Simple tasks are ok - such as moving or zipping files -- but all computations should be managed in a job.
```

