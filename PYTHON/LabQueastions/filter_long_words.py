def filter_long_words(word_list, n):
    return [word for word in word_list if len(word) > n]

# Example usage
words = input("Enter words separated by space: ").split()
n = int(input("Enter length threshold: "))

print("Filtered words:", filter_long_words(words, n))