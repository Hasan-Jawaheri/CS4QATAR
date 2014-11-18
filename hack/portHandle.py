
from models import Port

# close all the opened Ports to be run in the beginning, to make sure
# all ports are closed
def resetPorts():
	p = Ports.objects.filter(opened=True)
	for i in range(0, len(p)):
		p[i].opened = False
	p.save()


# It takes a portNo and create a new port in the port table
# returns 1 if the port is added or 0 if the portNo already exist
def addPort(portNo):
	if (Port.objects.filter(portNo=portNo).exists()):
		return 0

	p = Port(portNo=portNo, lastUser=0,  opened=False, history="")   # the initial data for the different fields
	p.save()

	return 1


# A temporary function for testing addingports,
# This function being called by the createPort command
# takes as argument the port number and call addPort with the portNo
def createPort(args):
	portNo = args[0]
	r = addPort(portNo)
	if (r == 1):
		return "Port Added"
	else:
		return "Port Already Exist"

		

# takes the portNo as input and check if the port exist in the port Table
# if it exists and isn't opened it set the opened field for that port to true (the port is now opened)

####### STILL NEED TO ADD WHICH USER IS ON IT ######

def openPort(args):
	portNo = args[0]
    
	if (Port.objects.filter(portNo=portNo).exists()):
		print("EXISTS")
		p = Port.objects.get(portNo=portNo)
		if(p.opened==False):
			s = "Port " + portNo + " is now opened"
			p.opened=True
			p.save()
			return s
		else:
			return "Port is opened by another user"   # the opened field is True which means it is already opened
	else:
		return "Wrong Port Number"   # The portNo doesn't exist
    



# close a port given the portNo
# After checking that it exist and that it is opened
# We will use it with exitting from the port

#### STILL NEED TO UPDATE THE LAST AND HISTORY FIELD FOR THAT PORT #######

def closePort(portNo):
	if (Port.objects.filter(portNo=portNo).exists()):
		p = Port.objects.get(portNo=portNo)
		if(p.opened == False):
			return "Port is not Opened"
		else:
			s = "Closing Port " + portNo
			p.opened = False
			p.save()
			return s
	else:
		return "Wrong Port Number"


# an exit-from-port like function, 
# it run with the command closePort and closes the port 
# that is given as argument. 
# It uses the closePort function.
def closePort_h(args):
	portNo = args[0]
	return closePort(portNo)
	


# It prints all the available closed ports from the portsTable
# We will use it to get the Ports that can be used
def getAvailablePorts():
	p = Port.objects.filter(opened=False)
	if (len(p) == 0):
		return "No Available Ports"

	s = ""
	for i in range(0, len(p)):
		s += str(p[i].portNo) + " "
	
	print (s)

	return s

# there are no args -> just there for being consistent with the commands functions
def getPorts(args):
	return getAvailablePorts()


