# -*- coding: utf-8 -*-

# This code is part of qhack2022-hackeinberg-project.
#
# (C) Copyright NTNU QuCAI-Lab, 2022.
#
# This code is licensed under the Creative Commons Zero v1.0 Universal License. 
# You may obtain a copy of the License in the root directory of this source tree.

"""Main Module for VQE Simulation of LiH Molecule with Adaptive Circuits"""

def vanilla():
  """Run simulation with PennyLane only"""
  import pennylane as qml
  from pennylane import qchem
  from pennylane import numpy as np
  symbols = ["Li", "H"]
  geometry = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 2.969280527])
  H, qubits = qchem.molecular_hamiltonian(symbols,geometry,active_electrons=2,active_orbitals=5)
  active_electrons = 2
  singles, doubles = qchem.excitations(active_electrons, qubits)
  
def qunasys_qamuy():
  """Run simulation with PennyLane and Qamuy SDK"""
  import qamuy.chemistry as qy
  import qamuy.plot
  from qamuy.client import Client
  input = qy.QamuyChemistryInput()
  email=""
  token=""
  client = Client(email_address=email, password=token)
