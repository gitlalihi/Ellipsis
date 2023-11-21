#Python function that takes a multidimensional array and slices the first two elements from the third dimension.

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
nested_list = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = input("Enter element at position ({}, {}): ".format(i, j))
        row.append(value)
    nested_list.append(row)
print("User Input Nested List:")
for row in nested_list:
    print(row)

def slice_third_dimension(arr):
    if not arr or not all(isinstance(sublist, list) for sublist in arr) or not all(all(isinstance(element, list) for element in sublist) for sublist in arr[0]):
        print("Input should be a 3D list.")
        return None
    sliced_array = [[[element[:2] for element in sublist] for sublist in subarray] for subarray in arr]
    return sliced_array

result = slice_third_dimension(nested_list)
print("Original List:")
for subarray in nested_list:
    for sublist in subarray:
        print(sublist)
    print()
print("\nSliced List (First Two Elements from the Third Dimension):")
for subarray in result:
    for sublist in subarray:
        print(sublist)
    print()
