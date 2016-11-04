##################################################
##### 'Python Crash Course' Book - Exercises #####
##################################################

# NOTE: THIS FUNCTION IS A SPINNOF OF "EX.3-10. Every Function"

##################################################

# make list with favorite languages and show restlist 
# Note: somehow i seemed to have the keen interest to make a function 
# with user-input out of it ;) 

# original list (of programing languages)

languages = ["ruby", "python", "java", "javascript", "html", "css", "php"]

# function making new list of favorite languages with remainder of old input-list

def fav_languages(languages):
	print("Please note this list of programing languages:", languages,"\n")
	chosen = ""
	favorites = []
	while chosen != "exit":
		chosen = input('Choose your favorite language(s) from the list "languages"\n, or enter "exit"> ').lower()
		for language in languages:
			if chosen == language:
				favorites.append(language)
				index = languages.index(language)
				del languages[index]
			elif languages == []:
				print("Original list is empty now!")
				break
		
                        else:
                                break
                        
        print("Your favorite languages are:",favorites)

	print("\nRemaining languages in the original list:\n")
	print(languages)
	return favorites

# call function

fav_languages(languages)




