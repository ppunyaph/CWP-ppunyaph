first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
result = first_num * second_num
print(f"{first_num} * {second_num} = {result}")
if result == 0:
    print("This number is positive and negative.")
elif result > 0:
    print("This number is positive.")
else:
    print("This number is negative.")