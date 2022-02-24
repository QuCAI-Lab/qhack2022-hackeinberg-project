# -*- coding: utf-8 -*-

# This code is part of qhack2022-hackeinberg-project.
#
# (C) Copyright NTNU QuCAI-Lab, 2022.
#
# This code is licensed under the Creative Commons Zero v1.0 Universal License. 
# You may obtain a copy of the License in the root directory of this source tree.

"""NTNU QuCAI-Lab qhack2022-hackeinberg-project 2022"""
__version__ = "0.0.1-dev"
__license__ = "Creative Commons v1.0"
__copyright__ = "Copyright QuCAI-Lab 2022"
__author__ = "Lucas Camponogara Viera & José Paulo Marchezi"
__status__ = "Development"

###########################################################################

# Sanity Check 
from . import sanity 

# Dependencies 
import sys
import pennylane as qml
import qamuy

# About
def about():
  """Function to display the Hackeinberg project information."""
  print(" \
    ###################################\n \
    HACKEINBERG PROJECT INFORMATION:\n \
    >> Extending Adaptive Methods for Finding an Optimal Circuit Ansatze in VQE Optimization.\n \
    ###################################\n"
     )
  print(f"Python version: {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")
  print(f"Package version: {__version__}")
  print(f"Package license: {__license__}")
  print(f"Package status: {__status__}")
  print(f"Package authors: {__author__}")
  print(f"PennyLane version: {qml.__version__}")
  print("Qamuy Client SDK version: 0.28.0")
  
# Simulation
from .main.simulation import vanilla, qunasys_qamuy
