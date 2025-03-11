def process_array(arr):
    my_arrayy = [my_array for my_array in arr if my_array > 5]
    myarray = [my_array + 2 for my_array in my_arrayy]
    return myarray

my_array = [2, 8, 9, 48, 8, 22, -12, 2]

print(my_array)

print(process_array(my_array))