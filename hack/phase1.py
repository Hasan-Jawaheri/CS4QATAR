from hack.models import User
import random
import string

def login(args):
  if len(args) != 1:
    return "Invalid arguments"
  if User.objects.filter(user=args[0]).exists():
    U = User.objects.get(user=args[0])
    if U.CH1_stage > 1:
      return "Already logged in "+ args[0]+". Come on!"
    U.CH1_stage = 1
    a = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    U.CH1_Hash_value = a
    U.save()
    return a # strong encryption SharEnc3.0
  return "Invalid login"

def hashBreak(args):
  U = User.objects.get(user=args[0])
  hv = args[1]
  if U.CH1_stage == 0:
    return "You need to log in first."
  elif U.CH1_stage == 1:
    string = ""
    for i in range(len(hv)):
      string += chr(ord(hv[i])+5)
    if(string == U.CH1_Hash_value):
      U.CH1_stage = 2
      U.CH1_Hash_value = 1
      U.save()
      return "Login succeeded. Welcome "+args[0]+"!"
    else:
      return "Hash value is wrong"
  return "Phase already passed"

def logout(args):
  U = User.objects.get(user=args[0])
  if(U.CH1_stage >=1):
    U.CH1_stage = 0
    U.save()
    return "Bye "+args[0]+"!"
  return "You have not logged in"
