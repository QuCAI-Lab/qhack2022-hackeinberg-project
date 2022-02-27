![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/graphs/commit-activity)
[![Build Status](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/actions/workflows/tests.yml/badge.svg?branch=dev)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/release/QuCAI-Lab/qhack2022-hackeinberg-project.svg)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/releases)
[![commit](https://img.shields.io/github/last-commit/QuCAI-Lab/qhack2022-hackeinberg-project)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/commits)
[![Forks](https://img.shields.io/github/forks/QuCAI-Lab/qhack2022-hackeinberg-project)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork)

<div align="center">
  <a href="https://qucai-lab.github.io/"><img src="https://github.com/QuCAI-Lab/qucai-lab.github.io/blob/main/assets/QuCAI-Lab.png" height="500" width="500" /></a>
</div>

<div align="center">
  <h1> <a href="https://qhack.ai/events#hackathon-challenges"> QHack2022 Open Hackaton </a> - Hackeinberg Team Project </h1>
  <h2> Extending Adaptive Methods for Finding an Optimal Circuit Ansatze in VQE Optimization</h2>
</div>
<br>

<div align="center">
<b>Authors: ¹Lucas Camponogara Viera, ²José Paulo Marchezi</b>
<br>
<b><a target="_blank" href="https://en.ntnu.edu.tw/">¹National Taiwan Normal University - NTNU, Taipei, Taiwan</a></b>.
<br>
<b><a target="_blank" href="https://www.gov.br/inpe/pt-br">²National Institute for Space Research - INPE, São José dos Campos, SP, Brazil.</a></b>.
<br>
<b><a target="_blank" href="http://english.nssc.cas.cn/">²State  Key  Laboratory  of  Space  Weather,  National  Space  Science  Center, Chinese  Academy  of  Sciences, China</a></b>.
</div>

<!--  -->

# Dependencies

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Qamuy](https://img.shields.io/badge/Qamuy-%233F4F75.svg?style=for-the-badge&logo=Qamuy&logoColor=white)](https://qamuy.qunasys.com/docs/en/)
[![PennyLane](https://img.shields.io/badge/PennyLane-%233F4F75.svg?style=for-the-badge&logo=PennyLane&logoColor=white)](https://pennylane.ai/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

For specific versions, see the [requirements.txt](requirements.txt) file.

# First Steps

Primarily results can be seen in the [jupyter notebook file](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/notebook.ipynb).

To stay up-to-date with the latest version of `qhack2022-hackeinberg-project`, we strongly recommend you to [fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork). If you would like to install the source code from scratch using your conda environment on-prem, please resort to the `Installation Instructions` heading on the [**Developer's Guide**](developers_guide.md).

```bash
cd <gitclone_directory> && conda env create -n <env_name> environment.yml
conda activate <env_name> && python -m pip install --no-deps -v -e .
conda list qhack2022-hackeinberg-project
```
Quick test-drive:
```bash
>>> python hackeinberg_project/main/simulation.py
```
Alternatively, run the package:
```bash
$ python
```
```python
>>> import hackeinberg_project as hack
>>> hack.about()
>>> hack.penny_simulation(params, H, HF, sets, qubits, conv_tol, threshold)
```


# Project Description:

Most widely considered hardware-efficient and Chemistry-inspired ansatze, although generic, suffer from either barren plateaus [[1](https://www.nature.com/articles/s41467-018-07090-4)] or inconsistency under low-order trotterization steps [[2](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.9b01083)], respectively. To circumvent this drawback, different algorithms for optimization of variational quantum circuits (VQA), the so-called adaptive circuits, have already been proposed in the literature [[4](https://pennylane.ai/qml/demos/tutorial_adaptive_circuits.html)]. One example is the Adaptive Derivative-Assembled Pseudo-Trotter ansatz Variational Quantum Eigensolver (ADAPT-VQE) [[3](https://www.nature.com/articles/s41467-019-10988-2)]. In a nutshell, the ADAPT-VQE approach is to grow the ansatz by adding fermionic operators one-at-a-time so to preserve the amount of correlation energy. This approach can also be regarded as a particular optimization procedure for Full Configuration Interaction (FCI) VQE.

In this work, we combine some of the existing methods applied to the hybrid quantum-classical VQE [[5](https://doi.org/10.1038/ncomms5213)] algorithm for the particular case of the ground state of the LiH molecule. We prioritize the minimization of the circuit depth (the longest sequence of gates acting on a qubit register) at the cost of increasing parameter count (the number of parameters to be optimized) given the tradeoff between difficulty in implementation on NISQ devices vs difficulty in optimization on classical computers, respectively. The baseline approach took into consideration the following features for a good ansatz:

1. Coherence friendly: the circuit must be shallow, i.e, have a small number of layers in order to be computed during a time window smaller than the decoherence time.
2. Hardware friendly (qubit routing): gate coupling allowed only between nearest-neighbor qubits to avoid SWAP gates during qubit routing (mapping from the circuit diagram to a hardware topology).
3. Small number of hyperparameters: we seek the minimum amount of angles to be optimized in order to avoid classical optimization overhead (when classical computation becomes too expensive).

In the early stages of the project, the goal is to find a quasi-optimal ansatz by restricting the VQE simulation to single and double order excitations only. For the future, we plan to use a deep reinforcement learning approach to learn an exact circuit ansatz considering higher excitation orders and the [Qamuy SDK](https://qamuy.qunasys.com/docs/en/).

## Algorithm outline

1. With the spin orbitals of the molecule of interest, compute its second-quantized electronic Hamiltonian in the STO-3G basis.

2. Map the fermionic Hamiltonian given in terms of its fermionic operators into a spin qubit-equivalent Hamiltonian using either Bravyi-Kitaev or the inverted Jordan–Wigner transformation. This is required to perform gate-based quantum computation. The Hamiltonian will be used to compute the cost function that evaluate the expectation value of the Hamiltonian, while the number of qubits is required to obtain the electronic excitations and to set up the quantum circuit.

3. Obtain the single and double electronic excitations by acting with the electron annihilation and creation operators on the Hartree-Fock reference state.

4. Define a set with all unique single and double excitations to create the correspondent SO(2) unitary qubit gates (the particular Givens rotations) to each electronic excitation operator in order to build a quantum circuit ansatz of particle-conserving unitary qubit gates.

5. Initialize the qubit state to a reference Hartree-Fock state.

6. Initialize the parameter values of each gate in the ansatz to zero, i.e, initialize the ansatz to the identity matrix in order to compute the gradients with respect to the Hartree-Fock state.

7. Prepare the trial estate with the current ansatz.

8. Define the cost function as the expectation value of the qubit Hamiltonian. Define an optimizer (e.g. SGD).

9. Use the parameter shift rule to compute the gradient of the cost function with respect to its tunable parameters.

10. Identify the operators (gates) with the largest gradient. Add to the ansatz the gate whose gradient is the largest. Remove gates whose gradient are smaller than a pre-defined threshold.

11. Use the optimizer to update the circuit parameters according to a VQE experiment.

12. Define the convergence as the difference between the previous and the next expected value for the current optimization step. If the convergence tolerance is less than or equal to a pre-defined threshold $\epsilon$, exit the optimization loop and evaluate the cost metric of the final optimized circuit by measuring its circuit depth.

13. Repeat step 9.

# Challenges:

- [Quantum Chemistry Challenge](https://github.com/XanaduAI/QHack/blob/master/Open_Hackathon.md#quantum-chemistry-challenge).
- [Science Challenge](https://github.com/XanaduAI/QHack/blob/master/Open_Hackathon.md#science-challenge).

# References

\[1] McClean, J.R., Boixo, S., Smelyanskiy, V.N. et al. Barren plateaus in quantum neural network training landscapes. [Nat Commun 9, 4812 (2018)](https://www.nature.com/articles/s41467-018-07090-4). 

\[2] Grimsley, H. R.; Claudino, D.; Economou, S. E.; Barnes, E.; Mayhall, N. J. Is the trotterized uccsd ansatz chemically well-defined? [J. Chem. Theory Comput. 2020, 16, 1](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.9b01083).

[3] Harper R. Grimsley, Sophia E. Economou, Edwin Barnes, Nicholas J. Mayhall, “An adaptive variational algorithm for exact molecular simulations on a quantum computer”. [Nat. Commun. 2019, 10, 3007](https://www.nature.com/articles/s41467-019-10988-2).

[4] PennyLane dev team, "Adaptive circuits for quantum chemistry". [PennyLane, 13 September 2021](https://pennylane.ai/qml/demos/tutorial_adaptive_circuits.html).

[5] Peruzzo, A., McClean, J., Shadbolt, P. et al. A variational eigenvalue solver on a photonic quantum processor. [Nat Commun 5, 4213 (2014)](https://doi.org/10.1038/ncomms5213).

# Developers

Conceived and developed by [@camponogaraviera](https://github.com/camponogaraviera) and [@zemarchezi](https://github.com/zemarchezi).

# License

This work is licensed under a [Creative Commons Zero v1.0 Universal](LICENSE.md) license.

<hr>

Created and maintained by [@camponogaraviera][1].

[1]: https://github.com/camponogaraviera
[2]: https://github.com/zemarchezi
