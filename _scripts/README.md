# How to update the members map and table

This process is automated on the website and runs everyday, but if you wish to try it locally, follow this guide. Using the script requires a specific python installation detailed below, and being a bit confortable with a command line interface.

1. **Installing Python**

To easily install Python and all the necessary packages, we will use **Conda**.
Start by downloading the latest version of **Miniconda** for your operating system [here](https://docs.conda.io/en/latest/miniconda.html).

Install it by following the [instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

Make sure conda is available in your terminal by running the following command: `conda -V`

2. **Installing the Python packages**

Now we will install all the necessary packages in a separate environment called `gccr`. In your terminal, run the following commands:

```bash
 conda create -n gccr python=3.8.5 --yes
 conda activate gccr
 pip install -r _scripts/requirements.txt
```
This will download all the packages in a specific version and install them in the `gccr` conda environment.

You also need to install firefox for the PNG of the members map to be generated. For Ubuntu: `sudo apt-get install firefox`

3. **Running the script**

Make sure the `gccr` environment is active (if not, type `conda activate gccr`).

Type `python _scripts/make_members_data.py PATH_TO_FILE` where `PATH_TO_FILE` is the location of the Excel file (usually called members-{{date}}.xlsx). The output files will automatically go to the appropriate location:
* assets/html/members-map.html
* assets/img/members-map.png
* assets/data/members-summary.xlsx
* _data/members.yml