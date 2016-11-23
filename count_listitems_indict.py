#	count items in list that are also in dictionary


def members(my_dict,my_list):
    count = 0
    for item in my_list:
        if item in my_dict:
            count += 1
    return count

