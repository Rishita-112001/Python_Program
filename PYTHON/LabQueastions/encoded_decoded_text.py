def rot13(text):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w',
           'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g',
           'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}

    result = ""
    for char in text:
        if char.lower() in key:
            transformed = key[char.lower()]
            result += transformed.upper() if char.isupper() else transformed
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Example usage
text = input("Enter text to encode/decode using ROT-13: ")
print("Encoded/Decoded text:", rot13(text))