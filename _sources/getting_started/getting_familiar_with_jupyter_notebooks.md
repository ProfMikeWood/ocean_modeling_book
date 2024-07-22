# Getting Familiar with Jupyter Notebooks
Jupyter notebooks were designed as a convenient way to store both text and code together in the same place. They were created primarily with the coding languages **Ju**lia, **Pyt**hon, and **R** in mind although there are some plugins for other languages as well.

## Opening a Jupyter Notebook
A straight-forward way to open a Jupyter notebook is through the terminal. If you are using a Mac, you can open the default Terminal application. If you are on a Windows machine, then you can launch the Anaconda Prompt, found under the Start menu.

When you open the terminal, activate a conda environment with jupyter installed. If you followed the Installing Python and Jupyter instructions, your `cs185c` environment will be set up correctly. Activate it in the terminal:
```
conda activate cs185c
```

Now, you can launch your Jupyter notebook with the simple command:
```
jupyter notebook
```

Note that your notebook will open in your default web browser. Jupyter leverages the web brower interface but it is not online.

With Jupyter open, you can navigate through your file system, open existing notebooks, and create new ones using the option in the upper right hand side of the screen.

## Jupyter Notebook Basics
There are two key components to familiarize yourself with in a Jupyter notebook - the kernel and the notebook cells. These are described in the next two sections.

### The Jupyter Kernel
The kernel of a notebook is running in the background of a notebook and supports the compilation and running of code. If you configured your conda environment to be accessible in a Jupyter notebook, you can use your environment for the kernel. This will allow you to use all of the packages installed in your environment in the notebook.

### Jupyter Cells
There are two main types of cells in a Jupyter notebook: Code cells and Markdown cells. Code cells are used to run Python code blocks. Markdown cells store formatted text such as headers, tables, equations, and other types of text. The page HERE provides a convenient reference on formatting Markdown text.

To run a cell, you can use the play button on the top bar of the notebook. Alternatively, you can use the hot key `Shift + Enter`. When a coding cell is running, the bracket next to the cell will have a astericks (`[*]`) and when it completes, it will contain a number (`[17]`). The numbers will show the order you have run the cells and they do not need to be run from top to bottom.

```{note}
When data is stored into variables in a notebook, it is stored in memory for use in subsequent cells. Use caution when storing large arrays into new variables throughout the notebook.
```

By default, a new cell will start as a Code cell but the cell type can be changed using dropdown found in the header bar of the notebook.





