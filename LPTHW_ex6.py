# strings and text


# formatting a decimal into a string into a variable
x = "There are %d types of people." % 10

# saving strings into variables and using them to format 
# into larger string
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x 
print y 

# printing strings that have been formatted earlier
print "I said: %r." % x
print "I also said: %s." % y

# formatting booleans through variables
hilariou = False 
joke_eval = "Isn't that joke so funny!? %r"

print joke_eval % hilariou

w = "this is the left side of..."
e = "a string with a right side."

print w + e 