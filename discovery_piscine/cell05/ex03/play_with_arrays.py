original_array = [2, 8, 16, 42, 8, 24, -13, 3]
new_array = []
for number in original_array:
    if number > 5:
        new_array.append(number + 2)
        new_array = list(set(new_array))
print(original_array)
print(new_array)