from sys import argv	

print argv


#'unpacking the argv list values, setting them to our variables
program_name, person_name, favorite_number, gender = argv

favorite_number = 2
person_name = "Erik"
gender = "his"
#grouping their name, gender and number 

#indexing begins at 0
person = (person_name, favorite_number, gender)



# Wrote 3 Print Statements here
print "Howdy"
print "{} name is {}".format(person[2], person[0])
print "{} favorite number is {}".format(person[2], person[1])

#List all things I have my favorite number of
print "{} has {} slices of pizza in {} fridge.".format(person[0], person[1], person[2])
print "{} has seen {} panda bears in {} backyard.".format(person[0], person[1], person[2])
print "{} have {} pairs of old shoes in {} drawer.".format(person[0], person[1], person[2])