# This exercise mostly focuses with variables 


hello_str = "Hello World"
hello_int = 21
hello_bool = True 
hello_tuple = (21, 32)
hello_list = ["hello,", "this", "is", "a", "list"]

print hello_list

hello_list = list()

hello_list.append("hello")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

print hello_list

hello_dict={"first_name":"Liam",
			"last_name" : "Fraser",
			"eye_color" : "Blue"}

print hello_dict

print hello_list[4]

hello_list[4]+="!"

#the above is the same as
hello_list[4]=hello_list[4] + "!"
print hello_list[4]

print hello_tuple[0]
#the same as
print str(hello_tuple[0])

print hello_dict["first_name"] + " " + hello_dict["last_name"] + " has " + hello_dict["eye_color"] + " eyes."

# does the same but is cleaner

print "{0} {1} has {2} eyes.".format(hello_dict["first_name"], hello_dict["last_name"], hello_dict["eye_color"])




import sys 
int_condition = 10
if int_condition < 6:
	sys.exit("int_condition must be >= 6")
else:
	print "int_condition was >= 6 - continuing"

















