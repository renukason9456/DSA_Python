def reverse_word_order(s):
    words = s.split()  # Split the sentence into words
    reversed_words = []  # Create an empty list to store words in reverse order

    for word in reversed(words):  # Iterate through words in reverse order
        reversed_words.append(word)

    return " ".join(reversed_words)  # 

# Example usage
s = "Hello World"
print(reverse_word_order(s))  # Output: "World Hello"
