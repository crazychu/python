#teacher_names = ['andrew','bobby','esther']
#hlallala

#python_sentence = "{} loves Python! Whoo!".format(teacher_names[0])
#print python_sentence
#python_sentence = "{} loves Python! Whoo!".format(teacher_names[1])
#print python_sentence
#python_sentence = "{} loves Python! Whoo!".format(teacher_names[2])
#print python_sentence


#for teacher_name in teacher_names:
#	python_sentence = "{} loves Python! Whoo!".format(teacher_name)
#	print python_sentence
	#*command executes:
	#adnrew loves python!
	#bobby love spythoN!
	#esther love spython!
#for iteration in range(1200):
	#print "Loop {}:I love pizza".format(iteration)
	#*this shoots out Loop 1188:I love pizza
	#*this shoots out Loop 1189:I love pizza
	#*this shoots out Loop 1190:I love pizza
	#*this shoots out Loop 1191:I love pizza
	#*this shoots out Loop 1192:I love pizza
#iteration is a temporary variable 
#print range(20)


#print 'min' in teacher_names
#spits out FALSE
#print 'andrew' in teacher_names
# >>> TRUE
#print 'Andrew' in teacher_names
# >>>FALSE > case-sensitive <
# print 'andrew' not in teacher_names
# >>> False, he IS in the list



#this program has a bunch of names and print statements based on whether those people are in the office.
people = [('andrew','in'),
			('bobby', 'out'),
			('judy', 'out'),
			('esther', 'in'),
			('vince','in')]

#declaring a function
#upper is a method in a string that turns the text UPPER CASE
def gets_reward(person_who_is_in, catchphrase):
    print"{} is in the office:{}".format(person_who_is_in, catchphrase)
    print"{} gets a bagel!".format(person_who_is_in, catchphrase)
    print"{} gets to have so much cream cheese".format(person_who_is_in, catchphrase)
#if the person is in the office, they get a bagel
def gets_punished(bad_person):
    print"{} is not in the office.".format(bad_person)
    print "{} gets more emails...".format(bad_person)
    print "{} gets NO cream cheese.".format(bad_person) 
def person_is_in_the_office():
    """ return True is the person's status is 'in'
    """ 
    return status == 'in'

def take_attendance():
    cheer = 'whoopee'
    for person, status in people:
        person = person.upper()
        if person_is_in_the_office(): #error here
            gets_reward(person, cheer)
        else:
            gets_punished(bad_person) 
take_attendance()           