
# A Program that checks if two words are anagrams. Dictionary meanings do not apply

# Ask for user input. Convert to lower case
# - word, anagram
print('Hi there! Please enter the word first, followed by the anagram.')
word = input('Please enter your chosen word: ').lower()
anagram = input('Please enter an anagram: ').lower()


def find_anagram(word, anagram):
    # Convert args(strings) to a list of characters
    word_chars = list(word)
    anagram_chars = list(anagram)

    # Define a boolean state for evaluating for anagrams
    is_anagram = False

    # Compare for anagrams
    if (set(anagram_chars).issubset(set(word_chars))):
        print('Congrats! You are an anagramist.')
        is_anagram = True
    else:
        print('Anagram incorrect. Please try again.')
        is_anagram

    # Return true or false based on comparison
    return is_anagram

# Call function
find_anagram(word, anagram)