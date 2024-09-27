colors = [11, 34, 98, 43, 45, 54, 54]

for item in colors:
    if item > 50:
        print(item)

    # if colors[item] > 50:
    #     print(colors[item])

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = value/total_value*100
#     print(f'That is {percentage}%')
# except ValueError:
#     print("You need to enter a number. Run the program again.")