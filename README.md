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

## Download the tutorials
To run the tutorials locally, we recommend installing [Anaconda](https://www.anaconda.com/).
Anaconda is a high-performance scientific distribution of Python that includes many common packages needed for scientific and engineering work.
Download the installer from their website and run it for the local user.

The easiest way to download the tutorials is to clone this repository.
For this purpuse, make sure, [git](https://git-scm.com/downloads) is installed.

From a `git bash` run 
```
git clone https://github.com/modsim/CADET-Tutorial
```

Then, install all the requirements by running
```
conda install -c conda-forge --file requirements.txt
```

To install [CADET-Python](https://github.com/modsim/CADET-Python) run

```
pip install cadet-python
```

For the tutorials on parameter estimation, you also need to install [CADET-Match](https://github.com/modsim/CADET-Match):

```
pip install cadetmatch
```

## Getting started
Fire up a `jupyter-lab` from `Anaconda Prompt` and navigate to the location of this repository using the file manager on the left.
Then, start by following the instructions in `getting_started.ipynb`.
It includes a check that everything is installed correctly. 

In case you are new to `Python` and `jupyter`, we also included a small tutorial (`00_Introduction_Python`) which covers the necessary basics for the tutorials.


## Fixing potential problems.

- If you get the following error `The code execution cannot proceed because VCRUNTIME140_1.dll was not found. Reinstalling the program may fix this problem.`, please visit https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads and install the latest Microsoft Visual C++ Redistributable.
- Some of the notebooks include interactive graphs. To enable them, please open an Anaconda prompt and run: 
- For JupyterLab 2.0+
  ```
  jupyter labextension install @jupyter-widgets/jupyterlab-manager
  jupyter lab clean
  jupyter lab build
  ```
- For JupyterLab 3.0+: install `ipympl`
