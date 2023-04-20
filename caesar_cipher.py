alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True: # will forever run the loop of asking the user for a phrase to encrypt

    input_text = input("Please enter a message to encrypt: ").upper() # collects user input as input_text
    output_text = '' # initializes the output text
    print()

    if input_text == "quit".upper() or input_text == "exit".upper():
        print("Goodbye") 
        break # ends the loop 

    key = int(input("Please enter a key: ")) # collects user input as key *must be an integer
    print()
    print("Your cypher is: ")

    for char in input_text:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + key)%26 # gives the letter its new position
            new_char = alphabet[new_position]
            output_text += new_char
        else:
            output_text += char

    print(output_text) # prints the encrypted cypher
    print()
