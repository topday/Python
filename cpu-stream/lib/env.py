#!/usr/bin/python3
import sys

class Schema():
  debug = 0
  help = 0
  action = 0
  proc = 'CPU'

  def __init__(self, schema):
    schema

def init(schema = {}):

  inst = Schema(schema)

  if (len(sys.argv) > 1):

    for arg in sys.argv:

      bound = arg.split('=')

      if (arg == 'help'): inst.help = 1

      if (len(bound) == 2):
        if (bound[0] == 'debug'): inst.debug = bound[1]
        if (bound[0] == 'action'): inst.action = bound[1]
        if (bound[0] == 'proc'): inst.action = bound[1]

  if (inst.help == 1):
    print(vars(inst))

  return inst
