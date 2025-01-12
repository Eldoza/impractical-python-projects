# Pig latin
# if word that begins with a consonant, move the constant to the end and add "ay" to the end of the word
# if the word begins with a vowel, add "way" to the end of the word.OverflowError
# Write a program that takes in a word as input and uses indexing and slicing to return it's pig latin equivalent. Run pylint and pydocstyle on the code:
# pylint --rcfile name.pylintrc pseudonyms.py
"""Turn a word into its Pig Latin equivalent."""

def main():
    print("\nWelcome to the PIG LATIN translator. '\n")
    vowels = 'aeiou'
    while True:
        word = input("Please enter a word to translate (Press q to quit)'\n")

        if word.lower() == 'q':
            break

        first_letter = word[0].lower()
        pig_latin = word + 'way'

        if first_letter in vowels:
            print(f"Your word {word} in pig latin is {pig_latin}")
        else: 
            first_letter = word[0].lower()
            rest_word = word[1:]
            pig_latin = rest_word + first_letter + 'ay'
            print(f"Your word {word} in pig latin is {pig_latin}")

        
if __name__ == "__main__":
    main()
