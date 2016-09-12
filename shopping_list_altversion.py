print("Please Enter items into your Shopping List ...\n")
print("Enter 'LIST' to show List or 'EXIT' to exit!\n\n")

list_a = input("Enter Item: > ")

while True:
	item = input(">:")

	if item == "LIST":
		for item in list_a:
			print(item)
		continue
	elif item == "EXIT":
		print("Closing Shopping List. Have a nice day!")
		break
	else:
		list_a.append(item)
		print (list_a)






