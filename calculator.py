print("=== Simple Calculator ===")

num1 = float(input("Pehla number daalo: "))
num2 = float(input("Dusra number daalo: "))

print("Operation choose karo:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Zero se divide nahi hota")

else:
    print("Invalid choice")
