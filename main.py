#!/usr/bin/env python3

import os
from os import system

pnt   = print
inpt  = input

if os.name == 'nt':
  print('Nope')
  exit(1)
  
def clr():
  system('clear')

while True:
  print('Coming soon')
