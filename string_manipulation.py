#!/usr/bin/env python


def string_manipulation():
    var1 = "Hello world"
    var2 = "python programming"
    print var1+var2
    print r"var1\n"
    print "var1:[0:3]",var1[0:3]
    print "var1[:]" , var1[:]
    print "var1[:2]", var1[:2]
    print "var1[0:6]", var1[0:6]

    #Escape sequence
    print "Hello\aWorld"

    #String Special Operators
    if 'H' in var1:
        print "H is present"

    if 'A' not in var1:
        print "yahoo,not present"

    # usage of * in string
    print "var1" * 3
    print "varl" + str(3)

    # Tripple Quotes
    print ''' Python if condition format:
          if condition:
          \tstatements'''
    #Built-in String Methods

    #Capitalize
    name = "tom Capital"
    #first character capitalize
    print  name.capitalize()

    #centered with filler
    name = "Rahul"
    print name.center(10,'a')

    a,b,c = 12,13,14
    print a,b,c

    a,b,c = 'RAH'
    print a,b,c

    #Cutting and slicing strings in python

    string1 = "Thisstringisformanipulation" #testing the string without giving any space
    print string1

    print "string1[:]", string1 # print the whole string
    print "Length of the string is len(string1)", len(string1)
    print "string1[:len(string1)]",string1[:len(string1)] # len(string)

    print "string1[0:len(string1):1]", string1[0:len(string1):1] # Default is 1
    print "string1[0:len(string1):2]",string1[0:len(string1):2]  # return current character and move two character ahead
    print "string1[0:5]",string1[:5]







string_manipulation()