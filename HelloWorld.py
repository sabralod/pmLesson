#name = "Simon"

file = open("name.txt", "r")
for line in file:
    print("Hello, %s!" % line.rstrip('\n'))

#print("Hello, %s!" % name)
