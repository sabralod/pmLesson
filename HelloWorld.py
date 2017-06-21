#name = "Simon"

file = open("name.txt", "r")
for line in file:
    print("Hello, %s" % line)

#print("Hello, %s!" % name)
