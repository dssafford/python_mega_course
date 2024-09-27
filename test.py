temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(str(temperatures))


# user_entries = ['10', '19.1', '20']
#
# # new_user_entries = [sum(float(entry)) for entry in user_entries]
# sum_new_entry = 0
# for entry in user_entries:
#     new_entry  = float(entry)
#     sum_new_entry = sum_new_entry + new_entry
#
# print(sum_new_entry)




# user_entries = ['10', '19.1', '20']
#
# new_user_entries = [float(entry) for entry in user_entries]
# print(new_user_entries)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
#
# new_usernames = [len(name) for name in usernames]
# print(new_usernames)


# names = ["john smith", "jay santi", "eva kuki"]
#
# new_names = [name.title() for name in names]
#
# print(new_names)







# rate = 2
#
# dollars = int(input('enter dollar amount'))
#
# euros = rate * dollars
#
# print(str(euros))

# ranking = ['John', 'Sen', 'Lisa']
#
# person = input('enter a name')
#
# print(str(ranking.index(person)+1))

# filenames = ['document', 'report', 'presentation']
#
# for index, filename in enumerate(filenames):
#     print(f'{index}-{filename.capitalize()}.txt')

# ips = ['100.122.133.105', '100.122.133.111']
#
# number = int(input('Enter the index: '))
#
# print(f'You chose {ips[number]}')
#
# doug = [1,2,3]
#
# rainfall = [1.02, 32, 'test', doug]