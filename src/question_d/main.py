#add import
#Q4

from question_d import reverse_string

while True:
    user_input = input("Enter a string or 'quit' to exit: ")

    if user_input == "quit":
        print("Exiting the program")
        break
    
    if any(char.isdigit() for char in user_input):
        print("Invalid input. Please enter a string")
    
    else:
        reverse_value = reverse_string(user_input)
        print(f"The reverse of '{user_input}' is '{reverse_value}'")
