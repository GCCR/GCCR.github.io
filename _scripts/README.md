# How to update the members map and table

This process requires having a Python installation with quite a few packages, and being a bit confortable with a command line interface.

1. **Installing Python**

To easily install Python and all the necessary packages, we will use **Conda**.
Start by downloading the latest version of **Miniconda** for your operating system [here](https://docs.conda.io/en/latest/miniconda.html).

Install it by following the [instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

Make sure conda is available in your terminal by running the following command: `conda -V`

2. **Installing the Python packages**

Now we will install all the necessary packages in a separate environment called `gccr`. Go to the `_script` folder and type `conda env create -f conda_environment.yml`. This will download all the packages in a specific version and install them in `gccr`.

3. **Running the script**

Before you're able to update the members map and table, you will need to activate the `gccr` environment by typing `conda activate gccr`. You will have to do this everytime you close the current terminal.

To run the update, make sure you are in the `_script` folder, then type `python create_members.py PATH_TO_FILE` where `PATH_TO_FILE` is the location of the Excel file (usually called agreement_signed.xlsx). The output files will automatically go to the appropriate location:
* assets/html/members-map.html
* assets/img/members-map.png
* _data/members.yml