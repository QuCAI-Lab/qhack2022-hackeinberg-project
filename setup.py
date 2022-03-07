# This code is part of qhack2022-hackeinberg-project.
#
# (C) Copyright NTNU QuCAI-Lab, 2022.
#
# This code is licensed under the Creative Commons Zero v1.0 Universal License. 
# You may obtain a copy of the License in the root directory of this source tree.

"""A setuptools based setup configuration module (not Distutils) to specify the package information (metadata, contents, dependencies, etc.).

Since PEP 517, the setup.py file can now be replaced with the setup.cfg configuration file! 

Run this setup.py file using:
    $ python -m pip install -v -e .
    The "python -m pip install ." command is equivalent to the "python -m setup.py install" command.
    The -m flag in "python -m pip" enforce the pip version tied to the active environment (executes pip as the __main__ module).
    
Flags:
    -e, --editable <path/url>
        Install the package without copying any files to the interpreter directory allowing for source code changes to take effect without the use of rebuild and reinstall. 
        It also creates a <package_name>.egg-info file that enables the user to access the package information.
        For more information, see https://setuptools.pypa.io/en/latest/userguide/development_mode.html.
    -v, --verbose
        Enables progress display.

To create a source distribution file (which you can upload to PyPI) in the dist directory, simply run:
    $ python -m build

REFERENCES
[1] Setuptools, at "https://setuptools.pypa.io/en/latest/userguide/quickstart.html".
"""

import setuptools, inspect, os, sys
from pathlib import Path
from setuptools import setup, find_packages

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)
    
here = Path(__file__).parent.absolute()  

with open(here / "README.md", encoding="utf-8") as f:
    long_description = f.read()
    
with open(here / "requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

VERSION_PATH = os.path.join(os.path.dirname(__file__), "hackeinberg_project", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()
    
setup(
    name="hackeinberg_project", # The name for your package, the same name given to the main folder of your File Structure (package tree).
    packages=find_packages(), # A list of packages to be manipulated. 
                              # If there is only one pure python module, set the variable to a list containing a single string value: packages = ["hackeinberg_project"].
                              # This will make Setuptools to look for the hackeinberg_project/__init__.py file that is required so that Python treat the directory as a package. 
                              # One can verify the above is true on https://setuptools.pypa.io/en/latest/userguide/quickstart.html and https://docs.python.org/3/tutorial/modules.html.
    package_data={"": ["_imgs/*.png"]},
    version=VERSION, # Defines the version format for your package.
    description="qhack2022-hackeinberg-project | Extending Adaptive Methods for Finding an Optimal Circuit Ansatze in VQE Optimization",
    long_description=long_description, # Defines the README.md file content as the description of the package.
    long_description_content_type="text/markdown",
    author="Lucas Camponogara Viera & José Paulo Marchezi",
    author_email="vieracamponogara@gmail.com",
    download_url="https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project", # A string specifying the URL to download the package.
    license="Creative Commons v1.0", # One can choose a License template from: https://help.github.com/articles/licensing-a-repository.
    platforms=["Windows", "Linux"], # Defines a list of OS that runs the cross-platform application.
    classifiers=[
        "Development Status :: 1 - Beta", # One can choose between "3 - Alpha", "4 - Beta" or "5 - Production/Stable".
        "Environment :: Console",
        "License :: OSI Approved :: Creative Commons Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7.12",
        "Topic :: Scientific/Engineering",
    ], # Specifies the categories for the package in a list of strings.
    keywords="QHack2022 Hackeinberg Project", # Besides comma-separated string, Keywords can also be specified in a list of strings: keywords = ['keyword1', 'keyword2'].
    python_requires="==3.7.12", # A version specifier used to specify the Requires-Python defined in PEP 345.
    install_requires=requirements, # Specifies the 'requirements.txt' file that contains a list of required package dependencies to be installed.
    project_urls={
        "Bug Tracker": "https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/issues",
        "Documentation": "https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project",
        "Source Code": "https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project",
    },
)
