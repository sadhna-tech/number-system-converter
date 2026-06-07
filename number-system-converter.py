while True:
    print("\n===== NUMBER SYSTEM CONVERTER =====")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a decimal number: "))
        print("Binary:", bin(number)[2:])

    elif choice == "2":
        number = int(input("Enter a decimal number: "))
        print("Octal:", oct(number)[2:])

    elif choice == "3":
        number = int(input("Enter a decimal number: "))
        print("Hexadecimal:", hex(number)[2:].upper())

    elif choice == "4":
        print("Exiting Number System Converter...")
        break

    else:
        print("Invalid choice.")