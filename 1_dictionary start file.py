

# This is used to import the random module, which is used to generate random numbers and make random choices.
import random                           

# WHAT IS A DICTIONARY?
# A dictionary is a collection of key/value pairs.
# Keys are used to look up values quickly.


# The phonebook dictionary is used to store names and phone numbers.
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


# The three apostrophes are used to create a multi-line string, which is used to comment out a block of code.
'''    


print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)                    # This will print the entire dictionary, including the keys and values.
print(len(phonebook))               # The print(len(phonebook)) will print the number of key/value pairs in the dictionary, which is 3 in this case.


mydictionary = dict(m=8, n=9)
print(mydictionary)

chris_phone = phonebook['Chris']    
print(chris_phone)

print(phonebook['Kati'])



print()
print('*****  end section 1 ********')
print()










print()
print('*****  start section 2 - search dictionary ********')
print()



name = 'Katie'                          #everything is case sensitive, so if you type in 'katie' it will not find it

if name in phonebook:                   #this searches all the keys in the dictionary
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")



print()
print('*****  end section 2 ********')
print()










print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

(phonebook['Joe']) = '555-0123'               # How to add/append a value in a dictionary  

(phonebook['Chris']) = '555-4444'             # How to update a value in a dictionary       

print(phonebook)                              # There is no way to update a key in a dictionary.


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()



print(phonebook)
del phonebook['Chris']                       # How to delete a key/value pair from a dictionary
print(phonebook)







print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()



for key in phonebook:
    print(f"{key} - {phonebook[key]}")
    

for value in phonebook.values():
    print(value)


for k,v in phonebook.items():                       # Are immutable, meaning they cannot be changed.  You can change the values, but not the keys.
    print(k,v)

for x in phonebook.items():                         # This would be called a tuple, are mutable, meaning they can be changed.  You can change the values, but not the keys.
    print(x)



print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('Chris', 'key not found')          # This is a better way to search for a key in a dictionary.  It will return the value if it finds it, and if it doesn't find it, it will return the second argument, which is 'key not found' in this case.
print(phone)


phonebook.clear()                                         # This will clear the entire dictionary, removing all key/value pairs.
print(phonebook)




print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found')          # This will remove the key/value pair from the dictionary and return the value.  If the key is not found, it will return the second argument, which is 'not found' in this case.
print(remove)

print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem()          # This will remove the last key/value pair from the dictionary and return it as a tuple.  If the dictionary is empty, it will raise a KeyError.

print(a)                         # Will pick a random key/value pair to remove from the dictionary, and return it as a tuple.  If the dictionary is empty, it will raise a KeyError.

print(phonebook)






print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()




mylist = list(phonebook)  
print(mylist)
random_key = random.choice(mylist)          # This will pick a random key from the dictionary and return it.  If the dictionary is empty, it will raise an IndexError.
print(random_key)
print(phonebook[random_key])


print(phonebook[random.choice(list(phonebook))])          # This will pick a random key from the dictionary and return it.  If the dictionary is empty, it will raise an IndexError.



print()
print('*****  end section 9 ********')
print()







