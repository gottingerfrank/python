
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.


#	*** Challenges ***

#	### CHALLENGE 1/4: ###

#	Create a function named most_classes that takes a dictionary of teachers. Each key is a teacher's name and their value is a list of classes they've taught.
#	most_classes should return the teacher with the most classes.


#	Create function "most_classes", with argument being a dictionary of teachers

#	"teachers"-dictionary has keys=teacher and values=list of classes - e.g:

def most_classes(teachers):
	max_count = 0
	max_teacher = ""
	for teacher in teachers:
		course_list = teachers[teacher]
		course_count = 0
		for course in course_list:
			course_count += 1
			if course_count > max_count:
				max_count = course_count
				max_teacher = teacher
	return max_teacher

#	Example dict "teachers":

teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
'Kenneth Love': ['Python Basics', 'Python Collections']}

#	Call function with dict "teachers":

most_classes(teachers)

#	most_classes"-function should return the name of teacher with the most classes

#	### CHALLENGE 2/4: ###

#	Next, create a function named num_teachers that takes the same dictionary of teachers and classes
#	Return the total number of teachers


def num_teachers(teachers):
	total = 0
	for teacher in teachers:
		total += 1
	return total

#	### CHALLENGE 3/4: ###

#	Now, create a function named stats that takes the teacher dictionary
#	Return a list of lists in the format [<teacher name>, <number of classes>]
#	For example, one item in the list would be ['Dave McFarland', 1]

def stats(teachers):
	stats_list = []
	for teacher in teachers:
	        course_list = teachers[teacher]
	        course_count = 0
	        for course in course_list:
	                course_count += 1
	        list_item = [teacher, course_count]
	        stats_list.append(list_item)
	return stats_list



#	def stats(teachers):
#		stats_list = []
#	
#		for teacher in teachers:
#			course_list = teachers[teacher]
#			course_count = 0
#			for course in course_list:
#				course_count += 1
#			list_item = [teacher, course_num]
#			stats_list.append(list_item)
#		return stats_list






	





















