fullname = "Bright Nwosu"
mothername = "Nwosu Nkiruka"
streetname = "10 A/C Road, WBHE"

combinedText = fullname +mothername + streetname

text_without_spaces = combinedText.replace(" ", "").lower()

total_characters = len(text_without_spaces)

unique_letters = set(text_without_spaces)

vowels = "aeiou"
vowel_count = 0

for letter in text_without_spaces:
    if letter in vowels:
        vowel_count += 1

vowel_percentage = (vowel_count / total_characters) * 100

most_repeated_letter = ""

highest_count = 0

for letter in unique_letters:
    count = text_without_spaces.count(letter)

    if count > highest_count:
        highest_count = count
        most_repeated_letter = letter

contains_all_vowels = True

for vowel in vowels:
    if vowel not in text_without_spaces:
        contains_all_vowels = False

print("VOWEL DNA TEST REPORT")
print("-" * 35)

print("Combined String:")
print(combinedText)

print("\nTotal Characters (No Spaces):")
print(total_characters)

print("\nUnique Letters:")
print(unique_letters)

print("\nVowel Percentage:")
print(round(vowel_percentage, 2), "%")

print("\nMost Repeated Letter:")
print(most_repeated_letter)

print("\nContains All Five Vowels?")
print(contains_all_vowels)