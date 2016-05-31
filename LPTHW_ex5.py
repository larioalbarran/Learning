# page 28 of Learn Python the Hard way. Doing it because of the variables
# and printing 


my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

rand_Thing = 3.4


print "Let's talk about %s." % my_name
# %s for string
print "He's %d inches tall." % my_height
# %d for decimal and I'm pretty sure %f for a float 
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "if I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Printing this too %r" %rand_Thing
# can't print a tuple 