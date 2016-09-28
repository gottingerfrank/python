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