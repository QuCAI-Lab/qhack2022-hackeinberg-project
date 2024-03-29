[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/presentation.ipynb)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange?style=flat-square)
[![Build Status](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/actions/workflows/tests.yml/badge.svg?branch=dev)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/actions/workflows/tests.yml)
[![License](https://img.shields.io/github/license/QuCAI-Lab/QHack2022.svg?logo=CreativeCommons&style=flat-square)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/LICENSE.md)
[![Release](https://img.shields.io/github/release/QuCAI-Lab/qhack2022-hackeinberg-project.svg)](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/releases)

<div align="center">
  <a href="https://qucai-lab.github.io/"><img src="https://github.com/QuCAI-Lab/qucai-lab.github.io/blob/main/assets/QuCAI-Lab.png" height="500" width="500" /></a>
</div>

<div align="center">
  <h1> <a href="https://qhack.ai/events#hackathon-challenges"> QHack2022 Open Hackaton </a> - Hackeinberg Team Project </h1>
  <h2> Extending Adaptive Methods for Finding an Optimal Circuit Ansatze in VQE Optimization</h2>
</div>
<br>
<div align="center">
  <b>Authors: <a target="_blank" href="https://github.com/camponogaraviera">¹Lucas Camponogara Viera</a> and <a target="_blank" href="https://github.com/zemarchezi">²José Paulo Marchezi</a></b>.
<br>
<b><a target="_blank" href="https://en.ntnu.edu.tw/">¹National Taiwan Normal University - NTNU, Taipei, Taiwan</a></b>.
<br>
<b><a target="_blank" href="https://www.gov.br/inpe/pt-br">²National Institute for Space Research - INPE, São José dos Campos, SP, Brazil</a></b>.
<br>
<b><a target="_blank" href="http://english.nssc.cas.cn/">²State  Key  Laboratory  of  Space  Weather,  National  Space  Science  Center, Chinese  Academy  of  Sciences, China</a></b>.
</div>

<!--  -->

# Dependencies
<a href="https://www.python.org/"><img height="27" src="https://www.python.org/static/img/python-logo.png"></a>
<a href="https://numpy.org/"><img height="27" src="https://numpy.org/images/logo.svg"></a>
<a href="https://matplotlib.org"><img height="27" src="https://matplotlib.org/_static/images/logo2.svg"></a>
<a href="https://pennylane.ai/"><img height="27" src="https://pennylane.ai/img/logo.png"></a>
&nbsp;
<a href="https://qamuy.qunasys.com/docs/en/"><img height="27" src="https://qunasys.com/_nuxt/img/logo_Qunasys.a30187d.svg"></a>
<br>
<br>
  
For specific versions, see the [requirements.txt](requirements.txt) file.

# Preliminary Results

**Get the source code [here](hackeinberg_project/_main/simulation.py).**

Comparison with different approaches can be seen in the [jupyter notebook file](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/presentation.ipynb).

<div align="center">
  <a href="https://raw.githubusercontent.com/QuCAI-Lab/qhack2022-hackeinberg-project/dev/assets/plot.png"><img src="assets/plot.png" height="500" width="500" /></a>
</div>

# Project Description

Most widely considered hardware-efficient and Chemistry-inspired ansatze, although generic, suffer from either barren plateaus [[1](https://www.nature.com/articles/s41467-018-07090-4)] or inconsistency under low-order trotterization steps [[2](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.9b01083)], respectively. In order to circumvent this drawback, different algorithms for optimization of variational quantum circuits, the so-called adaptive circuits, have already been proposed in the literature [[4](https://pennylane.ai/qml/demos/tutorial_adaptive_circuits.html)]. One example is the Adaptive Derivative-Assembled Pseudo-Trotter ansatz Variational Quantum Eigensolver (ADAPT-VQE) [[3](https://www.nature.com/articles/s41467-019-10988-2)]. In a nutshell, the ADAPT-VQE approach is to grow the ansatz by adding fermionic operators one-at-a-time so to preserve the amount of correlation energy. This approach can also be regarded as a particular optimization procedure for Full Configuration Interaction (FCI) VQE.

In this work, we combine some of the existing methods applied to the hybrid quantum-classical Variational Quantum Eigensolver (VQE) [[5](https://doi.org/10.1038/ncomms5213)] algorithm to find the ground state of the LiH molecule. We prioritize the minimization of the [circuit depth](https://qiskit.org/documentation/_images/depth.gif) (total number of gate layers executed in parallel) at the cost of increasing parameter count (total number of parameters to be optimized) given the tradeoff between difficulty in implementation on NISQ devices vs difficulty in optimization on classical computers, respectively. A baseline approach must take into consideration the following features/rule-of-thumbs for designing parameterized circuits to run on NISQ devices:

1. Coherence friendly: the circuit must be shallow, i.e, have a small number of layers (small circuit depth) in order to be executed during a time window shorter than decoherence time.
2. Hardware friendly (qubit routing): gate coupling must be allowed only between nearest-neighbor physical qubits etched into the hardware processor in order to avoid non-trivial transpilation, i.e, the use of SWAP gates (non-native) during qubit routing (mapping from the circuit diagram to a hardware topology).
3. Small number of hyperparameters: the algorithm must seek the minimum number of angles to be optimized in order to avoid classical optimization overhead (when classical computation becomes too expensive).

In the early stages of the project, the goal is to find a quasi-optimal ansatz by restricting the VQE simulation to single and double order excitations only. In the future, the plan is to frame the adaptive circuit approach as a deep reinforcement learning problem in order to learn an optimal circuit ansatz considering higher excitation orders, and to perform the simulation on a real quantum hardware unsing the [Qamuy SDK](https://qamuy.qunasys.com/docs/en/).

## Algorithm Outline

1. With the spin orbitals of the molecule of interest, compute its second-quantized electronic Hamiltonian in the STO-3G basis.

2. Map the fermionic Hamiltonian given in terms of its fermionic operators into a spin qubit-equivalent Hamiltonian using either Bravyi-Kitaev or the inverted Jordan–Wigner transformation. This is required to perform gate-based quantum computation. The Hamiltonian will be used to compute the cost function that evaluates the expectation value of the Hamiltonian, while the number of qubits is required to obtain the electronic excitations and to set up the quantum circuit.

3. Obtain the single and double electronic excitations by acting with the electron annihilation and creation operators on the Hartree-Fock reference state.

4. Define a set with all unique single and double excitations to create the correspondent SO(2) unitary qubit gates (the particular Givens rotations) to each electronic excitation operator in order to build a quantum circuit ansatz of particle-conserving unitary qubit gates.

5. Initialize the qubit state to a reference Hartree-Fock state.

6. Initialize the parameter values of each gate in the ansatz to zero, i.e, initialize the ansatz to the identity matrix in order to compute the gradients with respect to the Hartree-Fock state.

7. Prepare the trial estate with the current ansatz.

8. Define the cost function as the expectation value of the qubit Hamiltonian. Define an optimizer (e.g. SGD).

9. Use the parameter shift rule to compute the gradient of the cost function with respect to its tunable parameters.

10. Identify the operators (gates) with the maximum and minimum gradient in magnitude. Add to the ansatz the gate whose gradient is at maximum magnitude. Remove from the set the gate with the gradient at minimum magnitude if it is smaller than a predefined threshold. Here, we add one gate per iteration while deleting a single gate if it satisfies the above condition.

11. Use the optimizer to update the circuit parameters according to a VQE experiment.

12. Define convergence as the difference between the ground truth and the expected value for the current optimization step. If the convergence tolerance is less than or equal to a pre-defined threshold $\epsilon$, exit the optimization loop and evaluate the cost metric of the final optimized circuit by measuring its circuit depth.

13. Repeat step 9.

# Challenges

- [Quantum Chemistry Challenge](https://github.com/XanaduAI/QHack/blob/master/Open_Hackathon.md#quantum-chemistry-challenge).

# Pip install from git clone

```bash
git clone https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project.git && cd qhack2022-hackeinberg-project
```
```bash
conda env create -f environment.yml && conda activate qhack2022-hackeinberg-project
```
```bash
python -m pip install --no-deps -v -e . && conda list hackeinberg-project
```
  
# Pip install from source
  
Use below command-line if you would like to install the [latest version](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/tags) of the source code (using the setup.py file) in a local anaconda environment named "qhack2022". 
  
**Note:** on Linux, this will install the package in the `~/.local/lib/python3.7/site-packages/` folder.

```bash
conda create -c conda-forge -n qhack2022 python==3.7.12 && conda activate qhack2022
```
```bash
python3 -m pip install --user git+https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project.git#egg=hackeinberg_project
```

For more information, resort to the [Pip Install from Source](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/developers_guide.md#pip-install-from-source) heading in the [**Developer's Guide**](developers_guide.md).

- Flags: 
  - `-m pip` flag: instructs python to run the pip module as a script.
  - The `--no-deps` flag ensures that `setup.py` will not overwrite the conda dependencies that you have already installed using the `environment.yml` file. In this case, the pip-equivalent packages specified in the `requirements.txt` file will not be used.
  - [`--user`](https://pip.pypa.io/en/stable/cli/pip_install/#install-user) flag: sets the package installation only for the current user.
  - `git+address.git`: specifies the Git repository address with ending .git.
  - `#egg=name`: specifies the package [name explicitly](https://pip.pypa.io/en/stable/cli/pip_install/#working-out-the-name-and-version) as `name`.
  - `-v` flag: enables progress display (verbose).
  - `-e` flag: stands for editable mode (recommended for developers). It installs the package without copying any files to the interpreter directory allowing for source code changes to be instantly propagated to the code library without the need of rebuild and reinstall, however, the python process/kernel will need to be restarted. It sets the pacakge info: Build dev_0 and Channel \<develop>. It also creates the `hackeinberg_project.egg-info` file that enables the user to access the package information by: `conda list hackeinberg-project`. For more information, see the setuptools [development mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).
  
# First steps

To stay up-to-date with the latest version of the `hackeinberg-project`, we strongly recommend you to [fork this repository](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/fork). 
  
**Quick test-drive:**
```bash
$ python3 hackeinberg_project/_main/simulation.py
```
**Alternatively, run the package:**
```bash
$ python3
```
```python
>>> import hackeinberg_project as hack
>>> hack.about()
>>> energy, sets, angles, n = hack.penny_simulation(params, H, HF, sets, qubits, conv_tol=1e-04, threshold=1.0e-5)
```
  
# References

\[1] McClean, J.R., Boixo, S., Smelyanskiy, V.N. et al. Barren plateaus in quantum neural network training landscapes. [Nat Commun 9, 4812 (2018)](https://www.nature.com/articles/s41467-018-07090-4). 

\[2] Grimsley, H. R.; Claudino, D.; Economou, S. E.; Barnes, E.; Mayhall, N. J. Is the trotterized uccsd ansatz chemically well-defined? [J. Chem. Theory Comput. 2020, 16, 1](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.9b01083).

[3] Harper R. Grimsley, Sophia E. Economou, Edwin Barnes, Nicholas J. Mayhall, “An adaptive variational algorithm for exact molecular simulations on a quantum computer”. [Nat. Commun. 2019, 10, 3007](https://www.nature.com/articles/s41467-019-10988-2).

[4] PennyLane dev team, "Adaptive circuits for quantum chemistry". [PennyLane, 13 September 2021](https://pennylane.ai/qml/demos/tutorial_adaptive_circuits.html).

[5] Peruzzo, A., McClean, J., Shadbolt, P. et al. A variational eigenvalue solver on a photonic quantum processor. [Nat Commun 5, 4213 (2014)](https://doi.org/10.1038/ncomms5213).
  
# How to Contribute

If you would like to venture off the beaten path and contribute to the `hackeinberg-project` python package as a developer, kindly resort to the [Contribution Guidelines](https://github.com/QuCAI-Lab/qhack2022-hackeinberg-project/blob/dev/developers_guide.md#Contribution) to know more about the current CI/CD pipeline and the how to's for a good bug report/pull request.

# Group distribution

- [Lucas Camponogara Viera](https://github.com/camponogaraviera) (theory and implementation). 
- [José Paulo Marchezi](https://github.com/zemarchezi) (code auditor).

# License

This work is licensed under a [Creative Commons Zero v1.0 Universal](LICENSE.md) license.

<hr>
