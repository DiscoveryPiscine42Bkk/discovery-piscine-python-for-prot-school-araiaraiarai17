def process_array(arr):
    myarray = [my_array + 2 for my_array in arr]
    return myarray
my_array = [2, 8, 9, 48, 8, 22, -12, 2]

print(my_array)

print(process_array(my_array))