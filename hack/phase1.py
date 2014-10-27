
def login(args):
  if len(args) != 1:
    return "Invalid arguments"
  if args[0] == "sharjeel2":
    U = User.objects.get(user="aliaa")
    if U.CH1_stage > 1:
      return "Already logged in, sharjeel. Come on!"
    U.CH1_stage = 1
    U.save()
    return "<5SFKTRC2>" # strong encryption SharEnc3.0
  return "Invalid login"

def hashBreak(args):
  U = User.objects.get(user="aliaa")
  if U.CH1_stage == 0:
    return "You need to log in first."
  elif U.CH1_stage == 1:
    U.CH1_stage = 2
    U.save()
    return "Login succeeded. Welcome Sharjeel!"
  return "Phase already passed"
