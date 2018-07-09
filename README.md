# MagnetometerLogParser
Parses .log and .csv files to extract magnetometer readings and analyze results.

# Installation
_These instructions are for installing Python 3.7 on Windows 10._

### Install Python 3
Download the installer for the latest version of Python3 from their [downloads page](https://www.python.org/downloads/release/python-370/).

Scroll down to the __Files__ section.

Select ```Windows x86-64 executable installer``` from the __Version__ column.

Once the file finishes downloading, open it to begin installation.

Select ```Add Python 3 to PATH``` to use python in the command prompt from any directory.

Follow instructions for the rest of the installation.

On the final step of the installer, select ```Disable path length limit``` and close the installer.

Check that python is installed by typing ```python``` in a command prompt.

If python was successfully installed, you should see the python shell ready for input.

### Install PIP
PIP is used to install/import modules that are necessary for creating charts from the data.

Open up a command prompt and navigate to the directory of this repo.

Then install pip with ```get-pip.py``` by running ```python install get-pip.py```.

### Install bokeh
Bokeh is the library used to create the charts from the data files.

To install, open a command prompt and navigate to the directory of this repository.

Install bokeh by typing ```pip install bokeh```.

The installer should run in the terminal.

### Troubleshooting
If you are having problems with installing python or pip, visit [this](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation) site for help. Even though it is showing how to install Python 2, it may help resolve most issues.


# Usage
Data files from the beacon or devkit must be named in alphabetical order for the Plotter to create accurate charts. The data files should be named in such a way that the first file is the one closest to the lowest power line.

Save the files to the folders within this directory according to the configuration they were measured for (```DISTANCE/``` directory means that all phases are on the entire time).

Once the files are appropriately named and stored in their designated folder, run ```python Plotter.py``` to output the `.html` file with the charts.