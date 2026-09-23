less_num = int(input("Enter a number less than 25: "))
if less_num >= 25:
    print("Error")
else:
    for i in range(less_num, 26):
        print("Inside the loop, my variable is ", i)