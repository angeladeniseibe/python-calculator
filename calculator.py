print("1. +")
print("2. -")
print("3. *")
print("4. /")

operator = int(input("Select Operator: "))
first_num = float(input("Enter First Number: "))
second_num = float(input("Enter second Number: "))

if operator == 1:
    answer = first_num + second_num
elif operator == 2:
    answer = first_num - second_num
elif operator == 3:
    answer = first_num * second_num
elif operator == 4:
    answer = first_num / second_num
else:
    print("Invalid")

print("Answer: ", answer)