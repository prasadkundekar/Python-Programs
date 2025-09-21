def count_vowels_consonants(input_string):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    input_string = input_string.lower()

    for char in input_string:
        if 'a' <= char <= 'z':
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

my_string = "Hello World"
vowels, consonants = count_vowels_consonants(my_string)

print(f"The string is: '{my_string}'")
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")