
x = "There are %d types of people" % 10 #simple use of %d
binary = "binary" #simple variable assigning
do_not = "don't" #same
y = "those who know %s and those who %s." % (binary, do_not) # using multiple formatters

print x
print y

print "i said: %r." % x # using %r which is basically using the whole statement
print "i also said: %r." %y

hilarious = False #variable
joke_evslustion = "Isnt that joke so funny ?!. %r " #using %r for next line

print joke_evslustion % hilarious #very smartly used %r for advantage just by one variable adjustment, for eg, we could write any variable at place of hialrious at the last moment 

w = "this is the left side of..."
e = "a string with a right side."

print w + e # strings in one direction biyachhhhhh