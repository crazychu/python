favorite_number = 2
person_name = "Erik"
gender = "his"
#grouping their name, gender and number 

#indexing begins at 0
person = (person_name, favorite_number, gender)
andrew = ('Andrew',6,'his')
courtney = ('Courtney',21,'her')

person = courtney


#print person[0]
#print person[1]
#print person[2]


# Wrote 3 Print Statements here
print "Howdy"
print "{} name is {}".format(person[2], person[0])
print "{} favorite number is {}".format(person[2], person[1])

#List all things I have my favorite number of
print "{} has {} slices of pizza in {} fridge.".format(person[0], person[1], person[2])
print "{} has seen {} panda bears in {} backyard.".format(person[0], person[1], person[2])
print "{} have {} pairs of old shoes in {} drawer.".format(person[0], person[1], person[2])