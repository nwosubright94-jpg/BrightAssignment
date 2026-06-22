# Store personal information in separate variables
fullname = "Bright Nwosu"
mothername = "Nwosu Nkiruka"
streetname = "10 A/C Road, WBHE"

# Join all the strings together to create one combined text
combinedText = fullname + mothername + streetname

# Remove all spaces and convert everything to lowercase
# This makes the analysis easier and more consistent
text_without_spaces = combinedText.replace(" ", "").lower()

# Count the total number of characters after removing spaces
total_characters = len(text_without_spaces)

# Create a set of unique characters
# A set automatically removes duplicates
unique_letters = set(text_without_spaces)

# Define the vowels we want to check for
vowels = "aeiou"

# Start the vowel counter at zero
vowel_count = 0

# Loop through each character in the text
for letter in text_without_spaces:

    # Check if the character is a vowel
    if letter in vowels:
        vowel_count += 1

# Calculate the percentage of vowels in the text
vowel_percentage = (vowel_count / total_characters) * 100

# Create variables to track the most repeated letter
most_repeated_letter = ""
highest_count = 0

# Check the frequency of each unique character
for letter in unique_letters:

    # Count how many times the character appears
    count = text_without_spaces.count(letter)

    # If this count is greater than the current highest count,
    # update the most repeated character
    if count > highest_count:
        highest_count = count
        most_repeated_letter = letter

# Assume all vowels are present until proven otherwise
contains_all_vowels = True

# Check for each vowel one after another
for vowel in vowels:

    # If any vowel is missing, change the result to False
    if vowel not in text_without_spaces:
        contains_all_vowels = False

# Print the report title
print("VOWEL DNA TEST REPORT")

# Print a line for formatting
print("-" * 35)

# Display the combined text used for analysis
print("Combined String:")
print(combinedText)

# Display the total number of characters
print("\nTotal Characters (No Spaces):")
print(total_characters)

# Display all unique characters found in the text
print("\nUnique Letters:")
print(unique_letters)

# Display the percentage of vowels
print("\nVowel Percentage:")
print(round(vowel_percentage, 2), "%")

# Display the most frequently occurring character
print("\nMost Repeated Letter:")
print(most_repeated_letter)

# Display whether all five vowels exist in the text
print("\nContains All Five Vowels?")
print(contains_all_vowels)
