# -*- coding: utf-8 -*-

# This code is part of qhack2022-hackeinberg-project.
#
# (C) Copyright NTNU QuCAI-Lab, 2022.
#
# This code is licensed under the Creative Commons Zero v1.0 Universal License. 
# You may obtain a copy of the License in the root directory of this source tree.

"""Check for installed dependencies"""

###########################################################################
import os
if os.name == 'nt':
  try:
      import pyscf
  except ImportError:
    print(" \
        ###################################\n \
        WARNING:\n \
        >> This package depends on PySCF.\n \
        >> PySCF has no support for native windows platform.\n \
        >> Install PySCF on a Linux distribution: $ python -m pip install pyscf --user.\n \
        ###################################\n"
         )
    raise
try:
  import pennylane
except ImportError:
  print(" \
      ###################################\n \
      WARNING:\n \
      >> This package depends on PennyLane.\n \
      >> Install PennyLane as per the documentation instructions at https://pennylane.readthedocs.io/en/stable/development/guide/installation.html.\n \
      ###################################\n"
       )
try:
  from pennylane import qchem
except ImportError:
  print(" \
      ###################################\n \
      WARNING:\n \
      >> This package depends on pennylane-qchem\n \
      >> To install, run: $ python -m pip install pennylane-qchem.\n \
      ###################################\n"
       )
try:
  import qamuy
  #from qamuy.client import Client
  #email='' # Fill in your e-mail address.
  #token='' # Fill in your password.
  #client = Client(email_address=email, password=token)      
except ImportError:
  print(" \
      ###################################\n \
      WARNING:\n \
      >> One last installation step. \n \
      >> This package depends on Qamuy Client SDK.\n \
      >> To install qamuy, run: $ python -m pip install -U qamuy-client --extra-index-url https://download.qamuy.qunasys.com/simple/\n \
      ###################################\n"
       )
  raise
