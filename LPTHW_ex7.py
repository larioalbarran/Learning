print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 
# does this really multiple the print? 
# does it work for like "repeat" * 10?
# print "repeat" * 10  - YES it does

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# if comma at the end is removed it is treated as two different lines
# (This is 46 characters, longer than 80 is bad style)
# comma makes it one line                    V  
print end1 + end2 + end3 + end4 + end5 + end6,  
print end7 + end8 + end9 + end10 + end11 + end12