<div align="center">
  <h1> QHack2022 Hackeinberg Team Project</h1>
  <h2> Developer's Guide</h2>
</div>
<br>

# Table of Contents
- **[CI/CD](#cicd)**
- **[File Structure](#tree)**
- **[Pip Install from Source](#pipsource)**
- **[Pip install with Conda](#pipconda)**
- **[Installation Instructions](#Installation)**
- **[First Steps](#Steps)**
- **[Local Update](#Update)**
- **[Contribution Guidelines](#Contribution)**
- **[For die-hard Jupyter Notebook users](#Jupyter)**

# CI/CD<a name="cicd" />  

The current [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) tool is [GitHub actions](https://docs.github.com/en/actions) used to automate the software development workflow. The CD hub is this upstream codebase repository, unless you are reading from a forked one. 

We are slowly adding a [test suite](https://www.ibm.com/docs/en/elm/7.0.0?topic=scripts-test-cases-test-suites), check back sometime.


# File Structure (package tree)<a name="tree" />  

```
qhack2022-hackeinberg-project
├── .github
│   ├── workflows
│       ├── greetings.yml
│       └── tests.yml
├── assets
│   ├── plot.png
├── hackeinberg_project
│   ├── main
│       └── simulation.py
│   ├── VERSION.txt
│   ├── __init__.py
│   └── sanity.py 
├── .gitignore
├── LICENSE.md
├── README.md
├── developers_guide.md
├── environment.yml
├── presentation.ipynb
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
└── setup.py
```

# Pip Install from Source<a name="pipsource" />  

>Linux users using the system Python without a virtual environment, should work with the `python3` and `python3 -m pip --user` commands. 
>Windows users should replace the above commands with `python` and `python -m pip`, respectively.

One can install the [v0.0.2](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/releases/tag/0.0.2) release of `hackeinberg-project` on-prem via pip (a python package manager):

1. First, check the installed python version on a command-line interface (CLI):
```bash
python --version
```
Note: **If your system's python version on-prem differs from that of the package, fastforward to section [Pip install with Conda](#pipconda)**.

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
pip3 --version 
```
To list installed packages:
```bash
pip list
```
3. Install Git via pip:
```bash
python3 -m pip install --user git
```
4. To install the pre-release of `hackeinberg-project` from source, simply run:
```bash
python3 -m pip install --user git+https://github.com/QuCai-Lab/qhack2022-hackeinberg-project.git@0.0.2
```
To install a specific release, run:
```bash
python3 -m pip install --user git+https://github.com/QuCai-Lab/qhack2022-hackeinberg-project.git@<tag_number>
```
- Get your password (access token) at: `Settings` >> `Developer settings` >> `Personal access tokens` >> `Generate new token` >> `Select scopes (repo)`.


## Pip install with Conda<a name="pipconda" />  

Follow this instructions to pip install from source in a Conda environment.

1. Download [Anaconda](https://www.anaconda.com/products/individual).

2. Navigate to the file directory and grant execute permission ([Unix-like terminal](https://github.com/QuCAI-Lab/educational-resources/tree/main/Linux_Essentials)): 
```bash
cd <dir> && chmod +x <filename>.sh
```
3. Install Anaconda via terminal (Ubuntu users):
```bash
./<filename>.sh
```
4. Create a Conda env. with the required python version:
```bash
conda create -c conda-forge -n <env_name> python==3.7.12 && conda activate <env_name> 
```
5. Install from source:
```bash
python3 -m pip install --user git+https://github.com/QuCai-Lab/qhack2022-hackeinberg-project.git@0.0.2
```

# Installation Instructions (Conda env.)<a name="Installation" />  

**Follow these steps to install the `hackeinberg-project` package from scratch in a local [Anaconda environment](https://github.com/QuCAI-Lab/educational-resources/tree/main/Conda_Essentials).**

1. Install Git via pip:
```bash
python3 -m pip install git
```

2. [Fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork).


3. Set up a git linkage by cloning this repository in a custom folder of your local machine:

```sh
mkdir <folder_name> && cd <folder_name> && git clone https://github.com/<your_githubusername>/qhack2022-hackeinberg-project.git
```

4. Create a brand new conda environment with all the necessary package dependencies.

```sh
cd qhack2022-hackeinberg-project && conda env create -n <env_name> environment.yml
```

5. Activate the new env. and install the `hackeinberg-project` package:

```sh
conda activate <env_name> && python3 -m pip install --no-deps -v -e .
```

The `python3 -m pip install .` command is equivalent to the `python3 -m setup.py install` command.

- Flags: 
  - The -m flag in `python3 -m pip` enforce the pip version tied to the active environment (executes pip as the __main__ module).
  - The `--no-deps` flag ensures that `setup.py` will not overwrite the conda dependencies that you have already installed using the `environment.yml` file. In this case, the pip-equivalent packages specified in the `requirements.txt` file will not be used.
  - The -e flag Install the package without copying any files to the interpreter directory allowing for source code changes to take effect without the use of rebuild and reinstall. It also creates a `hackeinberg_project.egg-info` file that enables the user to access the package information by: `conda list hackeinberg-project`. For more information, see the setuptools [development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
  - The -v flag enables progress display.

# First Steps<a name="Steps" />  

Verifying the current installed version of `hackeinberg-project` in your local anaconda environment:

```sh
conda activate <env_name> && conda list hackeinberg-project
```

Quick test-drive:
```sh
$ python
```
```python
>>> import hackeinberg_project as hack
>>> hack.about()
>>> energy, sets, angles, n = hack.penny_simulation(params, H, HF, sets, qubits, conv_tol=1e-04, threshold=1.0e-5)
```

# Local Update<a name="Update" />  

Follow these instructions to sync your forked repository with the upstream repository.

- From the web UI:

  - Before pull (fetch and merge): "This branch is N commit(s) behind QuCAI-Lab:dev."

  1. Click on `Fetch upstream`: "Fetch and merge N upstream commit(s) from QuCAI-Lab:dev."

  2. Click on `Fetch and merge`. "Output message should be: This branch is up to date with QuCAI-Lab:dev."

- From the command line:

1. [Sync](https://docs.github.com/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) both your local (cloned) copy and your remote forked repo:

```sh
cd <repo-name> # If you have already forked the repo. Otherwise, run 'git init' to initialize an empty one. 
git remote -v # To list the current configured remote repository for your fork.
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY # Assigning "upstream" as the remote repository that will be synced with the fork.

git fetch upstream # To retrieve all the new remote-tracking branches and tags updates from the upstream repository.
git checkout <branch-name> # To switch to the existing remote-tracking branch (i.e., the branch fetched from the remote repository) named "<branch-name>".

git merge upstream/<branch-name> # To merge the specified upstream branch with your local (cloned) branch without losing your local changes.
                                 # If the local branch didn't have any commits, GIT will fast-forward the cloned repo.
                                     
git push -u origin <branch-name> # Finally, we push the local changes in order to also update your remote forked repository.
```

Alternatively, one can choose to use `$ git pull`, a shortcut for completing both `$ git fetch` and `$ git merge` in the same command. 
The full process using an empty directory becomes:
```sh
cd <dir-name>
git init # For an empty directory.
git remote add upstream <orig_repo_url> # Remote of the the original repo.
git remote add origin <forked_repo_url> # Remote of the forked repo.
git pull upstream <branch-name> # To fetch updates and merge them with your local (cloned) repository.
git add --all
git commit -m '<commit_message>'
git branch -M <branch-name>
git push -u origin <branch-name> # To update your remote forked repository.
```

Make sure to commit all new changes made in your local work before running the pull command to avoid a [merge conflict](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line).

2. Update `conda`:

```sh
conda update -n base conda -y && conda --version
```

3. [Update](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=prune#updating-an-environment) your existing conda environment and install `hackeinberg-project`:

```sh
conda env update -n <env_name_exist> --file environment.yml --prune && conda activate <env_name_exist> && python3 -m pip install --no-deps -e -v .
```

# Contribution Guidelines<a name="Contribution" />  

- **Issue Tracker**: If you would like to report a bug, kindly open an issue in the [Issue Tracker](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/issues).

- **Pull request**: If you would like to contribute to the source code, please [fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork) and push commits to a [pull request](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/pulls) from your forked repository to the [dev](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/branches) branch of `qhack2022-hackeinberg-project`. Make sure to run a test suite locally before all pushes so that your pull request can be successfully merged.

## Submitting a bug report or a feature request

Follow this template to submit a good bug report or a feature request.

```
<!--- Title of your Bug Report -->
- **hackeinberg-project version**:
- **list of requirements**:
- **Operating system type and version number**:
- **Bug description**:
- **Steps to reproduce the problem**:
- **Expected behavior**:
- **Suggested solution(s)**:
```

## Submitting a Pull Request

`This branch is 1 commit ahead of <QuCAI-Lab>:dev.`

Follow these instructions to submit a good pull request from the command line.

1 - [Fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork).

2 - Clone your forked repository to your local machine:

```sh
git clone https://github.com/<yourgithubusername>/qhack2022-hackeinberg-project.git
```

3 - Create a new branch for pull request and check out:

```sh
cd qhack2022-hackeinberg-project
git checkout -b <yourgithubusername>-pull-request 
```

4 - Check your changes before commit:

```sh
git status
git diff
```

5 - Set "upstream" as the original remote repository that will be synced with the fork:

```sh
git remote add upstream https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project
git remote -v
```

6 - Set your Local Git Identity:

```sh
git config user.name "<yourgithubusername>"
git config user.email "youremail@mail.com"
git config --list
```

7 - Push changes from your local shell/Anaconda Prompt, as follows:

```sh
git add --all
git commit -m "<topic of your pull request>"
git push -u upstream <yourgithubusername>-pull-request
```

8 - On the web UI, click the `Compare & pull request` button.

9 - Finally, click on `Create pull request`.

The admin or CI/CD tool of the upstream (original) repository will review the pull request and merge (or ignore) your proposed changes.


# For die-hard Jupyter Notebook users<a name="Jupyter" />

**Q: jupyter notebook/lab throws an error** ``ModuleNotFoundError: No module named 'hackeinberg_project'``.

**A:** You are running ``Jupyter notebook`` outside the ``hackeinberg_project`` environment. To circumvent the issue, assign your conda environment containing the ``hackeinberg_project`` module to your local jupyter notebook from within the Anaconda command-line interpreter, as follows:

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

If the problem persists, please re-install ``hackeinberg_project`` in a fresh conda environment (create a new one from scratch). 
The ``environment.yml`` file already instructs ``conda`` to install ``Jupyter`` inside the conda environment.


# Contributors 

Created and maintained by [@camponogaraviera][1].

[1]: https://github.com/camponogaraviera
