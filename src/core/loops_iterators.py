# Loops and iterators

# This is a list
list_words = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Kappa', 'Sigma']
for w in list_words:
	print(w, len(w))
	
# This is a dictionary
users = {"user_01" : "active", "user_02" : "inactive", "user_03" : "active",  "user_04" : "inactive", "user_05" : "inactive"}
print("\n" + str(users))

# Iterating over a copy else will get a runtime error : "dictionary changed size during iteration"
inactive_list = {}	
for user, status in users.copy().items():
	if status == 'inactive':
		#print('deleting inactive user : ', user)
		#print("assigning to inactive list :	", user)
		inactive_list[user] = status
		del users[user]	
#print("Remaining users :				", users)

active_list = {}
for user, status in users.items():
	#print("assigning to active list :	", user)
	active_list[user] = status

print("Active users	:	", active_list)
print("Inactive users	:	", inactive_list)
print('-' * 80)
# Range from 5 to 100 in steps of 10
for i in range(5, 100, 10):	
	print(i, end = " ")
print("")
list_num = list(range(0,10,2))
print(list_num)
print("Sum of 0 + 1 + 2 + 3 = ", sum(range(4)))

for i in range(len(list_words)):
	print(i, list_words[i])
print('')
print('-' * 80)

# Use enumerate() instead of range() : to get both index and element instead
for i, elem in enumerate(list_words):
	print(i, elem)
	
print('-' * 80)
