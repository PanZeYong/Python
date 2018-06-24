print("Give me two numbers, and I'll add them.")



while True:
    try:
        first_number = input("\nFirst number: ")
        first_number = int(first_number)

        second_number = input("\nSecond number: ")
        second_number = int(second_number)

    except ValueError:
        print("the number what you input is not the int.")
    else:
        sum = int(first_number) + int(second_number)    
        print("Sum: " + str(sum))