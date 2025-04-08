ecco
====

This page describes the modules available in the ecco package.

exf
---
The exf modules is designed to read and write external forcing files.

read_ecco_exf_file
^^^^^^^^^^^^^^^^^^

Read an external forcing field used in ECCO Version 5 Alpha.
(e.g. EIG_dsw_plus_ECCO_v4r1_ctrl_2008)

Parameters
""""""""""
data_dir : str
   A file path to the directory where the exf files are stored.
file_prefix : float
   The prefix of the file omitting the year (e.g. EIG_dsw_plus_ECCO_v4r1_ctrl)
year : int
   The year of the file (e.g. 2008)

Returns
"""""""
lon : 1-d numpy array
   An array of longitude values corresponding to the geometry of the grid.
lat : 1-d numpy array
   An array of latitude values corresponding to the geometry of the grid.
lon : 3-d numpy array
   An array of external forcing values corresponding to file requested.

