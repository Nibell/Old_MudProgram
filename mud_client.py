import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')

# Print list of available methods
print s.system.listMethods()

finished = 0
print "Welcome to simple MUD, the simple dungeon game."
while not finished:
    command = raw_input(': ')
    if command == "quit" or command == "q":
        finished = 1
    else:
        print s.data(command)
s.close()
