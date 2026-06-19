fullName = "Bright Nwosu"

firstName = fullName.split()[0]
shift = len(firstName)

encrypted = ""

for letter in fullName:
    if letter.isalpha():

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if letter.isupper():
            alphabet = alphabet.upper()

        position = alphabet.index(letter)
        newPosition = position + shift

        if newPosition >= 26:
            newPosition = newPosition - 26

        encrypted += alphabet[newPosition]

    else:
        encrypted += letter

print("Original Name:-", fullName)
print("Encrypted Name:-", encrypted)

decrypted = ""

for letter in encrypted:
    if letter.isalpha():

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if letter.isupper():
            alphabet = alphabet.upper()

        position = alphabet.index(letter)
        newPosition = position - shift

        decrypted += alphabet[newPosition]

    else:
        decrypted += letter

print("Decrypted Name:", decrypted)
