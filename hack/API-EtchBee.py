def login(args):
  if len(args) != 1:
    return "Invalid arguments"
  return "logging in as " + args[0]

def runexploit(args):
  return "WT"

def call (cmd):
  tokens = cmd.split (' ')
  if (len(tokens) < 1):
    return "Invalid command"

  cmdTable = {
    "login": login,
    "runexploit": runexploit
  }

  if tokens[0] in cmdTable.keys():
    return cmdTable[tokens[0]](tokens[1:])
  
  return "Unknown command"
