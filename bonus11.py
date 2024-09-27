#
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_number = max(grades)
#     return max_number
#
# print(get_max())

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_number = max(grades)
#     min_number = min(grades)
#     return f'"Max: {max_number}, Min: {min_number}\"'
#
#
#
# print(get_max())
#
# exit()
def get_average(my_list_local):
    # with open("files/data.txt", "r") as file:
    #     data = file.readlines()
    values = my_list_local
    values = [float(i) for i in values]
    average_local = sum(values)/len(values)
    return average_local

my_list = [2,4,6]
average = get_average(my_list)
print(average)