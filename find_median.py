def median(work):
    sort = sorted(work)
    if len(sort)%2 == 0:
        median = (sort[len(sort)//2]+sort[(len(sort)//2)-1])/2
    else:
        median = sort[len(sort)//2]
    return median

# Example no.1:
work = [7,12,3,1,6] # odd-value list
print("Median of odd-number list [7,12,3,1,6] is:", median(work)) # median of odd-value list

# Example no.2:
work = [7,3,1,4] # even-value list
print("Median of even-number list [7,3,1,4] is:", median(work)) # median of even-value list

# test no.3
work = [4,5,5,4]
print("Median of even-number list [4,5,5,4] is:", median(work)) # median of even-value list
