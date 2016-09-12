#   *** *** *** ***  *** *** *** *** 
#   Treehouse - Basic Python Course
#   *** *** *** ***  *** *** *** ***



#   create shopping_list to hold items. Inform about app and how to exit (DONE)

shopping_list = []

print('Welcome to shopping-list app. You can enter new items to add to list. Enter "DONE" to exit app!')


#   keep asking for items and add to list until exiting app

while True:
    new_item = input("Add item to shopping-list >")
    if new_item == "EXIT":
        break
    else:
        shopping_list.append(new_item)
    

#   on exiting, print out DONE in capitals

print('DONE')

#   after exiting, print out every item in shopping_list

for item in shopping_list:
    print(item)



