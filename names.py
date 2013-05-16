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




people = [('andrew','in'),
				('bobby', 'in'),
				('judy', 'out'),
				('esther', 'in'),
				('vince','in')]

#declaring a function
#upper is a method in a string that turns the text UPPER CASE
def gets_reward():
    print"{} is in the office.".format(person)
    print"{} gets a bagel!".format(person)
    print"{} gets to have so much cream cheese".format(person)
#if the person is in the office, they get a bagel
for person, status in people:
    person = person.upper()
    if status == 'in':
        gets_reward()
    else:
        print"{} is not in the office.".format(person)
        print "{} gets more emails...".format(person)
        print "{} gets NO cream cheese.".format(person) 