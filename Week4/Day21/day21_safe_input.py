print("===== SAFE NUMBER INPUT =====")

while True:
    user_input = input("Enter a number: ")
    
    try:
        number = float(user_input)
        if number < 0:
            print("Please enter a positive number.")
            continue
        elif number >= 0:
            if "." in user_input:
                print("Valid float number entered: ", number)
            else:
                print("Valid integer number entered: ", int(number))
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
       