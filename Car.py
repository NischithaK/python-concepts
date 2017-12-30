import sys

print sys.subversion

variable_name = raw_input("enter the input\n")

print variable_name


vartuple = tuple(variable_name)

print "tuple is{0}".format(vartuple)

varlist = list(variable_name)

print "list is {0}".format(varlist)

varset = set(variable_name)

print "set is {0}".format(varset)
