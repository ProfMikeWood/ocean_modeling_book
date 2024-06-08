# Choosing an optfile

In this section, you will implement tools to download an environemnt of Python for the class


## Install a Command Line Interface

On windows, use cygwin

On MacOS, use iTerm.


## Miniconda Installation


```{note}
Here is a note
```

Anaconda is a popular distribution of Python and a set of programs built specifically for data science. Miniconda is stripped-down version of Anaconda. We will use Miniconda, and add additional programs manually, so that it does not take up as much space on your computer. Miniconda includes:

Python: Programming language

Conda: Package manager

Conda is a package manager. It maintains the directories (folder pathways) and versions of external (non-default) python packages. A package is a set of Python tools designed for a specific purpose. Some of these are included with Python, but others have to be downloaded from an external source.

If you have Anaconda or Miniconda already installed on your computer, follow the steps below. If not, move on to Miniconda installation.

First run Python and check which version you have. The version number is displayed when Python starts up.

To maintain consistency, we will be using Python version 3.10 in this class. Previous versions of Python 3.x will work most of the time in classroom demonstrations and other course materials, but you may run into a few cases where certain commands are invalid or not available. Python 2.x is completely incompatible with this course material. If your version is already 3.10, and you are fine with installing additional packages to your existing version, proceed to installing additional tools.

If you have a different version of Python, you have two options:

Uninstall the previous installation. Note that option 2 below may be better if you already have Python code that you want to keep running on the same version of Python. If you choose option 1, find the uninstall instructions for your operating system at https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation. For Mac and Windows installations, be sure to remove the Miniconda or Anaconda directory from your home folder. Restart your terminal and proceed with the Miniconda installation steps below.

Advanced: Create a new environment for this class.

Option 2 will allow you to use the same Python version and packages used in the course material, without altering your existing setup. For more information on environments, see https://conda.io/docs/user-guide/tasks/manage-environments.html

Open a terminal (Mac) or Anaconda prompt (Windows) and type:

conda create --name ms263-23 python=3.10
You can replace ms263-23 with any name you like for your environment. To enter the new environment, type:

conda activate ms263-23
Note

To access the environment you just created at later time, you will have to repeat this command whenever you start a new terminal or Anaconda prompt.

Keep this window open and proceed to Installing additional tools

Miniconda installation
Go to: https://conda.io/miniconda.html

Select Python 3.10 version. Download the appropriate installer for your operating system and run. The default options will be fine.

Windows: Select 32-bit or 64-bit. Chances are, with a newer computer, your operating system is 64-bit. If you do not know, try 64-bit and the installer will tell you if you made the wrong choice. Click on the installer file to download it.

Mac: There are different options for installers. Download the .pkg installer for the processor on your Mac (Intel for older Macs and Apple M1 for newer Macs) and click on it. If you don’t know what type of processor you have, see this guide.

