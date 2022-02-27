#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np
from pennylane import qchem
import time

def qunasys_qamuy():
  """Function to run simulation with Qamuy SDK."""
  import qamuy.chemistry as qy
  import qamuy.plot
  from qamuy.client import Client
  input = qy.QamuyChemistryInput()
  email=""
  token=""
  client = Client(email_address=email, password=token)
  
def penny_simulation(params, H, HF, sets, qubits, conv_tol, threshold):
  """Function to run the optimization loop with PennyLane.

  Args:
      - params (tensor): the parameters to be optimized in the ansatz.
      - H: the molecular Hamiltonian of the system in the qubit representation.
      - HF (numpy.ndarray): the Hartree-Fock state vector.
      - sets (list): total spin orbital indices used to build the Givens rotations a.k.a particle-preserving operators (qubit gates).
      - qubits (int): the number of qubits used to build the circuit.

  Returns:
      - energy (list): a list of expected values of each iteration.
      - sets (list): a list of excitations corresponding to the gates used in the final circuit.
      - params (list): a list of optimized parameters.
      - n (int): number of epochs.
  """

  def ansatz(params, wires, to_gates):
    """Function that defines the circuit to be optimized."""
    qml.BasisState(HF, wires=wires) # The reference Hartree-Fock state.
    for i, elem in enumerate(to_gates):
      if len(elem) == 4:
        qml.DoubleExcitation(params[i], wires=elem)
      else:
        qml.SingleExcitation(params[i], wires=elem)
  
  # Step 8.
  opt = qml.GradientDescentOptimizer(stepsize=0.4)  
  dev = qml.device("default.qubit", wires=qubits)
  #@qml.qnode(dev, diff_method="parameter-shift")
  #def cost(params):
    #"""The cost function."""
    #ansatz(params, wires=range(qubits), to_gates=sets)
    #return qml.expval(qml.SparseHamiltonian(H_sparse, wires=range(qubits)))

  cost = qml.ExpvalCost(ansatz, H, dev, optimize=True)
  circuit_gradient = qml.grad(cost, argnum=0)
  epochs = 50
  energy = [cost(params, to_gates=sets)]
  print(f"Epoch = 0,  Energy = {energy[-1]:.8f} Ha, t = 0s")
  print("Number of gates = {}\n".format(len(sets)))

  for n in range(epochs):
    t1 = time.time()

    grads = circuit_gradient(params,to_gates=sets) # Step 9.
    maxpos = np.argmax(grads) # Beginning of Step 10.
    max=sets[maxpos]
    sets.append(max)
    params=np.append(params, 0) # End of step 10.
    
    params, prev_energy = opt.step_and_cost(cost, params, to_gates=sets) # Step 11.
    energy.append(cost(params, to_gates=sets))
    conv = np.abs(-7.8825378193 - prev_energy) # Step 12.
    t2 = time.time()
    print(f"Epoch = {n+1}, Energy = {energy[-1]:.8f} Ha, t = {t2-t1:.2f}s")
    print("Number of gates = {}\n".format(len(sets)))
    if conv <= conv_tol:
      break
  return energy, sets, params

if __name__ == "__main__":
  symbols = ["Li", "H"] # Beginning of step 1.
  geometry = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 2.969280527], dtype=float)
  H, qubits = qml.qchem.molecular_hamiltonian(symbols, geometry, active_electrons=2, active_orbitals=5) # End of step 2.
  electrons = 2
  singles, doubles = qchem.excitations(electrons, qubits) # Step 3.
  sets = singles+doubles # Step 4.
  HF = qml.qchem.hf_state(electrons, qubits) # Step 5.
  params = np.zeros(len(sets), requires_grad=True) # Beginning of step 6.
  conv_tol=1e-04
  energy, sets, angles = optimize(params, H, HF, sets, qubits, conv_tol, threshold=1.0e-4) # Beginning of the optimization loop.
  print("Expected ground-state energy: -7.8825378193.")
  print(f"Simulation = {energy[-1]:.8f} Ha")
