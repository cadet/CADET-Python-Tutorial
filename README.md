[![CC BY NC SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by-nc-sa].

[![CC BY 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY%20NC%20SA%204.0-lightgrey.svg

# CADET Tutorials

This is a repository for introductory examples and tutorials of the [CADET](https://github.com/modsim/cadet/) software for modelling and simulating chromatographic processes.

For more information, see also:
- **Website (including documentation):** https://cadet.github.io
- **Forum:** https://forum.cadet-web.de
- **Source:** https://github.com/modsim/cadet
- **Bug reports:** https://github.com/modsim/cadet/issues

## Prerequisites

### Install CADET
First you need to make sure, a recent version of CADET (>= 4.1) is installed as explained in the [installation guide](https://cadet.github.io/getting_started/installation.html#installation).

Please ensure that the cadet binaries are available at the following locations:
    - Windows: `C:\Users\<username>\cadet\bin`
    - Linux: `~/cadet/bin`

If you have downloaded the pre-built cadet binaries, just extracting the archive to `C:\Users\<username>` or `~` should do the trick. 

Alternatively, you can set `cadet_bin_path` to the location of the cadet binaries in `utils.ipynb`. Please note that this will be overwritten upon updating the tutorials using `getting_started.ipynb`. 

### CADET-Python

In this tutorial, we will use [CADET-Python](https://github.com/modsim/CADET-python) to interface CADET.
It is a file based frontend for CADET which almost exactly maps to the documented CADET file format.
The package includes a Cadet class which serves as a generic HDF5 frontend.

For installing CADET-Python, we recommend installing [Anaconda](https://www.anaconda.com/).
Anaconda is a high-performance scientific distribution of Python that includes many common packages needed for scientific and engineering work.
Download the installer from their website and run it for the local user.

The tutorials are written using jupyter notebooks and require some additional packages.
Open an `Anaconda Prompt` and run:

```
conda install numpy scipy matplotlib gitpython jupyterlab ipywidgets
conda install -c conda-forge jupyter_contrib_nbextensions jupyter_nbextensions_configurator
```

Moreover, we need to allow some additional channels for installing `CADET-Python`:

```
conda config --add channels anaconda-fusion
conda config --add channels conda-forge
```

Then, to install CADET-Python run:

```
conda install -c immudzen cadet-python
```

For the tutorials on parameter estimation, you also need to install [CADET-Match](https://github.com/modsim/CADET-Match):

```
conda install -c immudzen cadetmatch
```


## Download the tutorials

The easiest way to download the tutorials is to clone this repository.
For this purpuse, make sure, [git](https://git-scm.com/downloads) is installed.

From a `git bash` run `git clone https://github.com/modsim/CADET-Tutorial`.

Fire up a `jupyter-lab` from `Anaconda Prompt` and navigate to the location of this repository using the file manager on the left.
Then, start by following the instructions in `getting_started.ipynb`.
It includes a check that everything is installed correctly. 

In case you are new to `Python` and `jupyter`, we also included a small tutorial (`00_Introduction_Python`) which covers the necessary basics for the tutorials.

## Fixing potential problems.

- If you get the following error `The code execution cannot proceed because VCRUNTIME140_1.dll was not found. Reinstalling the program may fix this problem.`, please visit https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads and install the latest Microsoft Visual C++ Redistributable.
- Some of the notebooks include interactive graphs. To enable them, please open an Anaconda prompt and run: 
  ```
  jupyter labextension install @jupyter-widgets/jupyterlab-manager
  jupyter lab clean
  jupyter lab build
  ```
