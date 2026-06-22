# This is the full name I want to encrypt
fullName = "Bright Nwosu"

# Split the full name into words and take the first name
firstName = fullName.split()[0]

# Use the length of the first name as the shift value for encryption
shift = len(firstName)

# Create an empty string to store the encrypted result
encrypted = ""

# Loop through every character in the full name
for letter in fullName:

    # Check if the character is a letter (A-Z or a-z)
    if letter.isalpha():

        # Define the lowercase alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # If the current letter is uppercase, use an uppercase alphabet
        if letter.isupper():
            alphabet = alphabet.upper()

        # Find the current position of the letter in the alphabet
        position = alphabet.index(letter)

        # Move the letter forward by the shift value
        newPosition = position + shift

        # If the new position goes beyond the alphabet range,
        # wrap around to the beginning
        if newPosition >= 26:
            newPosition = newPosition - 26

        # Add the encrypted letter to the encrypted string
        encrypted += alphabet[newPosition]

    else:
        # If the character is not a letter (e.g., a space),
        # keep it unchanged
        encrypted += letter

# Display the original name
print("Original Name:-", fullName)

# Display the encrypted version of the name
print("Encrypted Name:-", encrypted)

# Create an empty string to store the decrypted result
decrypted = ""

# Loop through every character in the encrypted text
for letter in encrypted:

    # Check if the character is a letter
    if letter.isalpha():

        # Define the lowercase alphabet
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # If the letter is uppercase, switch to uppercase alphabet
        if letter.isupper():
            alphabet = alphabet.upper()

        # Find the position of the encrypted letter
        position = alphabet.index(letter)

        # Move the letter backward by the shift value
        # to get the original character
        newPosition = position - shift

        # Add the decrypted letter to the decrypted string
        decrypted += alphabet[newPosition]

    else:
        # Keep non-alphabet characters unchanged
        decrypted += letter

# Display the decrypted name to confirm it matches the original
print("Decrypted Name:", decrypted)
