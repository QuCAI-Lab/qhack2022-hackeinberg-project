# -*- coding: utf-8 -*-

# This code is part of qhack2022-hackeinberg-project.
#
# (C) Copyright NTNU QuCAI-Lab, 2022.
#
# This code is licensed under the Creative Commons Zero v1.0 Universal License. 
# You may obtain a copy of the License in the root directory of this source tree.

"""Main Module for VQE Simulation of LiH Molecule with Adaptive Circuits"""

  
def qunasys_qamuy():
  """Run simulation with PennyLane and Qamuy SDK"""
  import qamuy.chemistry as qy
  import qamuy.plot
  from qamuy.client import Client
  input = qy.QamuyChemistryInput()
  email=""
  token=""
  client = Client(email_address=email, password=token)
  
#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np
from pennylane import qchem
import matplotlib.pyplot as plt

def vanilla(params, H, HF, sets):
  """Main function to run the optimization loop.

  Args:
      - params (np.ndarray): the parameters to be optimized in the ansatz.

  Returns:
      - energy (np.ndarray): the expected value of the final (optmized) ansatz.
  """

  # Step 7.
  opt = qml.GradientDescentOptimizer(stepsize=0.4)  
  dev = qml.device("default.qubit", wires=qubits)
  
  # Step 8. 
  def ansatz(params, wires, to_gates):
    """Function that defines the circuit to be optimized."""
    qml.BasisState(HF, wires=wires) # Reference Hartree-Fock state.
    for i, elem in enumerate(to_gates):
      if len(elem) == 4:
        qml.DoubleExcitation(params[i], wires=elem)
      else:
        qml.SingleExcitation(params[i], wires=elem)

  cost = qml.ExpvalCost(ansatz, H, dev, optimize=True)
  energy = [cost(params, to_gates=sets)]
  epochs = 20
  conv_tol = 1e-07

  for n in range(epochs):
    circuit_gradient = qml.grad(cost, argnum=0)
    grads = circuit_gradient(params, to_gates=sets) # Step 9.
    if len(grads) == len(sets):
      maxpos = np.argmax(grads)
      minpos = np.argmin(grads)
      sets[minpos] = sets[maxpos]
    sets = [sets[i] for i in range(len(sets)) if abs(grads[i]) > 1.0e-5] # Step 10.
    np.append(sets, sets[maxpos])
    params, prev_energy = opt.step_and_cost(cost, params, to_gates=sets) # Step 11.
    energy.append(cost(params, to_gates=sets))
    conv = np.abs(energy[-1] - prev_energy) # Step 12.
    print(f"Epoch = {n},  Energy = {energy[-1]:.8f} Ha")
    if conv <= conv_tol:
      break

  print("\n" f"Optimized ground-state energy = {energy[-1]:.8f} Ha")

if __name__ == "__main__":
  #global qubits
  symbols = ["Li", "H"] # Begin of step 1.
  geometry = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 2.969280527], dtype=float)
  H, qubits = qml.qchem.molecular_hamiltonian(symbols, geometry, active_electrons=2, active_orbitals=5) # End of step 2.
  electrons = 2
  singles, doubles = qchem.excitations(electrons, qubits) # Step 3.
  sets = singles+doubles # Step 4.
  HF = qml.qchem.hf_state(electrons, qubits) # Step 5.
  params = np.zeros(len(sets), requires_grad=True) # Step 6.
  vanilla(params, H, HF, sets) # Begin the optimization loop.
