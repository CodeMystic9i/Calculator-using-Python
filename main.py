# BasicCalculator

first_number = input("Enter your First Number: ")
operator = input("choose a Operator(+, -, *, /, %): ")
second_number = input("Enter your Second Number: ")

first_number = int(first_number )
second_number = int(second_number)

if operator == "+":
  print(first_number + second_number)

elif operator == "-":
  print(first_number - second_number)

elif operator == "*":
  print(first_number * second_number)

elif operator == "/":
  print(first_number / second_number)

elif operator == "%":
  print(first_number % second_number)

else:
  print("Math Error! Try again")
