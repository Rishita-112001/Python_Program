def translate(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char.isalpha() and char not in vowels:  # Check if consonant
            result += char + 'o' + char.lower()
        else:
            result += char  # Keep vowels and other characters unchanged

    return result


# Example usage
text = input("Enter text to translate: ")
print("Translated text:", translate(text))