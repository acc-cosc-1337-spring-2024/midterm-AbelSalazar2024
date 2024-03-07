#add import
#Q2

from question_b import is_prime

while True:
    user_input = input("Enter a whole number or 'quit' to exit: ")

    if user_input == "quit":
        print("Exiting the program")
        break

    try:
        num = int(user_input)
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number or 'quit' to exit.")
