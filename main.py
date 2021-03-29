#!/usr/bin/env python3

import os
from os import system

if os.name == 'nt':
  print('Nope')
  exit(1)
  
def clr():
  system('clear')
