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
 conda env create -n gccr -f _scripts/environment.yml
```
This will download all the packages in a specific version and install them in the `gccr` conda environment.

You also need to install firefox for the PNG of the members map to be generated. For Ubuntu: `sudo apt-get install firefox`

3. **Running the scripts**

Make sure the `gccr` environment is active (if not, type `conda activate gccr`).

Download the file named `github_tokens.sh` from the Google Drive, place it in the `_scripts` folder

Run the following commands:

```bash
source _scripts/github_tokens.sh
python _scripts/make_members_data.py
python _scripts/make_committees_data.py
python _scripts/zotero_to_yml.py
```