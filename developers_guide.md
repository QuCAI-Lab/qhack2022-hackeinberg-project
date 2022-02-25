<div align="center">
  <h1> QHack2022 Hackeinberg Team Project</h1>
  <h2> Developer's Guide</h2>
</div>
<br>

# CI/CD

The current [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) tool is [GitHub actions](https://docs.github.com/en/actions) used to automate the software development workflow. The CD hub is this upstream codebase repository, unless you are reading from a forked one.

# Pip Install from Source

>Linux users using the system Python without a virtual environment, should work with the `python3` and `python3 -m pip --user` commands. 
>Windows users should replace the above commands with `python` and `python -m pip`, respectively.

One can install the [pre-release](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/releases/tag/0.0.1) of `qhack2022-hackeinberg-project` via pip (a python package manager):

1. First, check the installed python version on a command-line interface (CLI):
```bash
python --version
```
2. Install `pip` on Linux with the Python 3 migration:
```bash
sudo apt update && apt install python3-pip
```
To upgrade pip, run:
```bash
python3 -m pip install --user --upgrade pip
```
To show pip version:
```bash
python3 -m pip --version 
```
To list installed packages:
```bash
pip list
```
3. Install Git via pip:
```bash
python3 -m pip install --user git
```
4. To install the pre-release of `qhack2022-hackeinberg-project` from source, simply run:
```bash
python3 -m pip install --user git+https://github.com/QuCai-Lab/qhack2022-hackeinberg-project.git@0.0.1#egg=pre
```
To install a specific release, run:
```bash
python3 -m pip install --user git+https://github.com/QuCai-Lab/qhack2022-hackeinberg-project.git@<tag_number>
```
- Get your password (access token) at: `Settings` >> `Developer settings` >> `Personal access tokens` >> `Generate new token` >> `Select scopes (repo)`.

# Installation Instructions (virtual environment)

**Follow these steps to install `qhack2022-hackeinberg-project` from scratch in a local [Anaconda environment](https://github.com/QuCAI-Lab/educational-resources/tree/main/Conda_Essentials).**

1. Download [Anaconda](https://www.anaconda.com/products/individual).

2. Navigate to the file directory and grant execute permission ([Unix-like terminal](https://github.com/QuCAI-Lab/educational-resources/tree/main/Linux_Essentials)): 
```bash
cd <dir> && chmod +x <filename>.sh
```

3. Install Anaconda via terminal (Ubuntu users):
```bash
./<filename>.sh
```

4. Install Git via pip:
```bash
python3 -m pip install git
```

5. [Fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork).


6. Set up a git linkage by cloning this repository in a custom folder of your local machine:

```sh
mkdir <folder_name> && cd <folder_name> && git clone https://github.com/<your_githubusername>/qhack2022-hackeinberg-project.git
```

7. Create a brand new conda environment with all the necessary package dependencies.

```sh
cd qhack2022-hackeinberg-project && conda env create -n <env_name> environment.yml
```

8. Activate the new env. and install `qhack2022-hackeinberg-project`:

```sh
conda activate <env_name> && python3 -m pip install --no-deps -v -e .
```

The `python3 -m pip install .` command is equivalent to the `python3 -m setup.py install` command.

- Flags: 
  - The -m flag in `python3 -m pip` enforce the pip version tied to the active environment (executes pip as the __main__ module).
  - The `--no-deps` flag ensures that `setup.py` will not overwrite the conda dependencies that you have already installed using the `environment.yml` file. In this case, the pip-equivalent packages specified in the `requirements.txt` file will not be used.
  - The -e flag Install the package without copying any files to the interpreter directory allowing for source code changes to take effect without the use of rebuild and reinstall. It also creates a `hackeinberg_project.egg-info` file that enables the user to access the package information by: `conda list qhack2022-hackeinberg-project`. For more information, see the setuptools [development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
  - The -v flag enables progress display.

# First Steps

Verifying the current installed version of `qhack2022-hackeinberg-project` in your local anaconda environment:

```sh
conda activate <env_name> && conda list qhack2022-hackeinberg-project
```

Quick test-drive:
```sh
$ python
```
```python
>>> import hackeinberg_project as hack
>>> hack.about()
>>> hack.run()
```

# Local Update

Follow these instructions to sync your forked repository with the upstream repository.

- From the web UI:

  - Before pull (fetch and merge): "This branch is N commit(s) behind QuCAI-Lab:dev."

  1. Click on `Fetch upstream`: "Fetch and merge N upstream commit(s) from QuCAI-Lab:dev."

  2. Click on `Fetch and merge`. "Output message should be: This branch is up to date with QuCAI-Lab:dev."

- To sync both your local (cloned) copy and your remote forked repository from the command line:

```sh
cd <repo-name>
git remote -v # To list the current configured remote repository for your fork.
git remote add upstream https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project # Assigning "upstream" as the original remote repository that will be synced with the fork.

git fetch upstream # To retrieve all the new remote-tracking branches and tags updates from the upstream repository.
git checkout dev # To switch to the existing remote-tracking branch (i.e., the branch fetched from the remote repository) named "dev".

git merge upstream/dev # To merge the "dev" upstream branch with your local (cloned) branch without losing your local changes.
                       # If the local branch didn't have any commits, GIT will fast-forward the cloned repo.
                                     
git push -u origin dev # Finally, we push the local changes in order to also update your remote forked repository on the GitHub server.
```

One can also choose to use `$ git pull`, a shortcut for completing both git fetch and git merge in the same command: 
  
```sh
git pull upstream dev # To fetch updates and merge them with your local (cloned) repository.
git push -u origin dev # To update your remote forked repository.
```

Make sure to commit all new changes made in your local work before running the pull command to avoid a [merge conflict](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line).

2. Update `conda`:

```sh
conda update -n base conda -y && conda --version
```

3. [Update](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=prune#updating-an-environment) your existing conda environment and install `qhack2022-hackeinberg-project`:

```sh
conda env update -n <env_name_exist> --file environment.yml --prune && conda activate <env_name_exist> && python3 -m pip install --no-deps -e -v .
```

# For die-hard Jupyter Notebook users

1. Assign your conda environment to jupyter notebook:

```sh
conda activate <env_name> && conda install ipykernel && ipython kernel install --user --name=<name_for_kernel>
```

- To list available jupyter kernels:

```sh
jupyter kernelspec list 
```

- To uninstall a jupyter kernel:

```sh
jupyter kernelspec uninstall <name_for_kernel>
```

- To open `jupyter notebook`:

```sh
jupyter notebook
```

With open jupyter notebook in your local web browser, choose the kernel you have just created.
