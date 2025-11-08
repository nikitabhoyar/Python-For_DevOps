day_of_week = input("Enter the day of the week: ").lower() #convert input into lowercase
print(day_of_week)

if day_of_week == "Saturday" or day_of_week == "Sunday":
    print("I will learn live DevOps")
else:
    print("I will practise devops")

    num1 = int(input("Enter the First number: "))
    print(num1)
    num2 = int(input("Enter the Second number: "))
    print(num2)

choice = input("Enter the operation: ( options +,-,*,/,% ) ")

if choice == "+":
    print("Addition of two numbers is: ",num1+num2)
elif choice == "-":
    print("Subtraction of two number is: ",num1 - num2)
elif choice == "*":
    print("Multiplication of two number is: ", num1 * num2)
elif choice == "/":
    print("Division of two numbers is: ", num1/num2)
elif choice == "%":
    print("Modulous of two number is: ", num1%num2)
else: 
    print("Invalid choice")





   
    


    

