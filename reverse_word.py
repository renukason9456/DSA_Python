def reverse_words(s):
    words = s.split()  # Split the string into words
    reversed_words = []  # Create an empty list to store reversed words

    for word in words:
        reversed_words.append(word[::-1])  # Reverse each word and add to the list

    return " ".join(reversed_words) 

# Example usage
s = "Hello World"
print(reverse_words(s))  # Output: "olleH dlroW"
