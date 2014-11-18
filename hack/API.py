from hack.models import User

"""
IMPORT PHASES HERE
PLASE DO NOT DO "from hack.phaseX import *", but do
"import hack.phaseX" rather. And then use phaseX.stuff
"""
import hack.phase1
import hack.portHandle

# RUN EXPLOIT CODE FROM USER
# exploit code is generated by concatinating the args
# and adding spaces in between
# DONT allow users to import cuz thats harmful
def runexploit(args):
  code = ""
  for i in args:
    code += i + " "
  if "import" in code: # no importing is allowed for the users
    return "Illegal code: Don't import modules!"
  
  # TODO: run the code
  return "Code has been injected."


# this function calls other API functions
# dont change this!
def call (cmd):
  tokens = cmd.split (' ')
  if (len(tokens) < 1):
    return "Invalid command"
  # this table maps a string from input (such as "login x y z")
  # and calls a corresponding function in our API. The table
  # is basically a mapping between the input string and the
  # python function.
  # Arguments are automatically parsed and managed
  cmdTable = {
    "runexploit": runexploit,

    "openPort": hack.portHandle.openPort,    # to open a port

    "createPort": hack.portHandle.createPort,  # to create a new port

    "getPorts": hack.portHandle.getPorts,  # to get available closed ports

    "closePort": hack.portHandle.closePort_h,  # to close a port

    # phase 1
    "login": hack.phase1.login,
    "hash": hack.phase1.hashBreak,
    "logout": hack.phase1.logout,

    #phase 2 ...
  }


  # In case a cmd was run without its arguments, to prevent it from crashing
  try:
    if tokens[0] in cmdTable.keys():
      return cmdTable[tokens[0]](tokens[1:])
  except:
    return "Arguments Expected"

  return "Unknown command"
