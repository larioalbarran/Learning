# putting the comma at the end makes the input be on the same line
# so it looks like this:
# How old are you? (cursor)
# instead of this:
# How old are you?
# (cursor)

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)