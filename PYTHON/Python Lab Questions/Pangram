import string

def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(sentence)  # Check if all letters exist

# Example usage
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is NOT a pangram.")