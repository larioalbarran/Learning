# This exercise focuses on accepting user input. There's also formatting 
# involved and some for/while loops at the bottom 
# 
# things to lookup: try and except, .format, 
#

import sys

target_int=raw_input("How many integers?")

try: 
	target_int=int(target_int)
except ValueError:
	sys.exit("You must enter an integer")


ints = list()

count = 0

while count < target_int:
	new_int = raw_input("Please enter integer {0}:".format(count + 1))
	print new_int
	isint = False 
	try:
		new_int = int(new_int)

	except:
		print "You must enter an integer"

	if isint == False:
		ints.append(new_int)
		count += 1


print "Using a for loop"
for value in ints: 
	print str(value)

print "Using a while loop"

total = len(ints)
count = 0
while count < total:
	print str(ints[count])
	count += 1