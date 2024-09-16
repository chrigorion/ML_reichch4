![Source: Adobe Stock (865008368), modified](./data/doc/theme.jpg)



This Git project provides the materials used in the “Machine Learning” course of the ADLS study program, offered in the 3<sup>rd</sup> semester. The material includes slides, handouts, Jupyter notebooks and exemplary data.



## Edition 2024

* **Contributors**:
  * Norman Juchler ([norman.juchler@zhaw.ch](mailto:norman.juchler@zhaw.ch))
  * David Graber ([david.graber@zhaw.ch](mailto:david.graber@zhaw.ch))
* **Moodle**: [Link](https://moodle.zhaw.ch/course/view.php?id=21179)
* **Course description**: [Link](https://eventoweb.zhaw.ch/Evt_Pages/Brn_ModulDetailAZ.aspx?node=2901247e-aa27-4f84-a5d6-d6b33b234dbd&IDAnlass=1745797)





# Requirements

The below instructions assume that you have the following tools available on your computer:

* Visual Studio Code (also known as: VS Code, or VSC): [Link](https://code.visualstudio.com/)
* Git or a Git client (see for example [GitHub Desktop](https://github.com/apps/desktop))
* An initial installation of Python
* A functional bash terminal
  * Recommended tool for Window users: [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
  * MacOS and Linux distributions always come with a bash terminal



# Instructions

Here, setup instructions are provided for 

* [...students using Visual Studio Code](#setup-visual-studio-code)
* [...students working with a general Python setup](#setup-general)



## Setup (Visual Studio Code)

Below you find the main steps to clone (copy) this Git repository locally to your computer. 

1. If you are not yet familiar with git and Visual Studio yet, you may want to study this [tutorial](https://code.visualstudio.com/docs/sourcecontrol/overview).
2. Open the command palette (Ctrl+Shift+P, Mac: Cmd+Shift+P).
3. Type: Git clone $\rightarrow$ Clone from Github.
4. Enter the following URL [git@github.zhaw.ch:ADLS-Data-Science-and-Computation/Maschinelles-Lernen-HS24.git]()
5. Choose the target folder where the repository will be copied to.



Then, create a new virtual Python environment. Current versions of Visual Studio Code offer support for virtual environments using [`venv`](https://docs.python.org/3/library/venv.html) or [`conda`](https://www.anaconda.com/). Follow the instructions below to set up a new Jupyter Kernel in VS Code:

1. Add the folder containing this git repository to the workspace:
   * In VS Code, go to the Explorer panel (Ctrl+Shift+E, Mac: Cmd+Shift+E).
   * Right-click $\rightarrow$ Add Folder to Workspace.
2. Open the command palette (Ctrl+Shift+P, Mac: Cmd+Shift+P).
3. Enter: Notebook: Select Notebook Kernel.
4. Choose: Select Another Kernel.
5. Choose: Python Environments.
6. Choose: Create Python Environment.
7. Choose: Venv or Conda
8. Choose the workspace directory containing this git repository.
9. Select an available Python installation, please use Python 3.10 or newer.
10. Now, a list of available requirements.txt files are shown. Choose the one in this git repository. (Use requirements-conda.txt if you use Anaconda.)
11. Hit enter. Now the virtual environment is created and the kernel is ready to use.

After this initial effort, you will be able to select the kernel when opening a notebook in VS Code. The virtual environment resides in a (hidden) folder .venv of the workspace directory you have selected above. If you want, you can rename that folder to venv-ml-hs24 or similar for better readability.



## Setup (general)

For the course materials to run properly, clone this project and install the required packages. The code has been tested for **Python 3.11**, but most of the code will run also on other versions.

```bash
# Clone this repository
git clone https://github.zhaw.ch/ADLS-Data-Science-and-Computation/Maschinelles-Lernen-HS24.git

# Move inside the downloaded folder
cd Image-and-Signal-Processing
```



If you are using Python directly (not recommended), you can install the required packages as follows:

```bash
# First upgrade pip
python -m pip install pip --upgrade

# Install the required packages
python -m pip install -r requirements.txt
```



If you are familiar with a Python version management tool (like [venv](https://docs.python.org/3/library/venv.html) or [anaconda](https://www.anaconda.com/)), it is recommended to create a local environment first. This helps to avoid interfering with other Python environments.



```bash
#######################
#    Option: VENV     #
#######################

# Create a local environment
python -m venv venv

# Activate environment (Mac / Linux)
source venv/bin/activate
# Activate environment (Win)
venv\scripts\activate

# Update pip
python -m pip install pip --upgrade

# Install the requirements
python -m pip install -r requirements.txt
```



```bash
########################
#   Option: ANACONDA   #
########################

# Update conda
conda update conda

# Create new environment
conda create -n env-py310-isp python=3.10

# Activate new environment
conda activate env-py310-isp

# Install the requirements
conda install --file requirements-conda.txt
```



## Run Jupyter notebooks

An easy way to work with Jupyter notebooks is to open them in [**Visual Studio Code**](https://code.visualstudio.com/). Make sure you are using the correct Jupyter kernel (you will be prompted to select a kernel when opening a notebook). Alternatively, you can read and edit Jupyter notebooks in your default web browser. For this, run the following line in a terminal:

```bash 
jupyter notebook ./
```



## Update the repository

The contents of this repository may change in the course of this semester. To update the repository, use the following command. 

```bash 
git pull
```



**:warning:  Important**: If a file was updated by the tutor in the git project, and at the same time, you modified the local copy of that file, you may run into a situation called *merge conflict*. Seek help with your favorite tutor to recover from this.



# License

The Jupyter notebooks and codes are licensed under the clause BSD-3-Clause license.

Other course materials are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
