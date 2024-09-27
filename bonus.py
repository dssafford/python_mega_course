# file = open('members.txt','r')
#
# mylist = file.readlines()
# file.close()
#
# newName = input('Enter your name: ')
# mylist.append('\n' + newName)
#
# print(mylist)
#
#
# file = open('members.txt', 'w')
# file.writelines(mylist)
# file.close()


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)





# file = open('essay.txt', 'r')
#
# mylist = file.readlines()
#
# print(sum([len(i) for i in mylist]))

# for item in mylist:
#     print(item.title())