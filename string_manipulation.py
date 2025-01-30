# String Manipulations

# 1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# 2. String Slicing
text = "Programming"
print("Slicing (0 to 4):", text[0:4])  # Output: Prog
print("Slicing (last 3 characters):", text[-3:])  # Output: ing

# 3. String Length
print("Length of text:", len(text))

# 4. Changing Case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Titlecase:", text.title())
print("Capitalize:", text.capitalize())

# 5. String Replacement
text2 = "I love Java"
new_text = text2.replace("Java", "Python")
print("Replacement:", new_text)

# 6. Removing Whitespaces
text3 = "  Hello World  "

print("Stripped text:", text3.strip())  # Removes both leading and trailing spaces
print("Left stripped:", text3.lstrip())  # Removes leading spaces
print("Right stripped:", text3.rstrip())  # Removes trailing spaces

# 7. Checking Substrings
print("Is 'Python' in text2?", "Python" in text2)  # Output: False
print("Is 'Java' not in text2?", "Java" not in text2)  # Output: False

# 8. Splitting and Joining Strings
text4 = "apple,banana,cherry"
words = text4.split(",")  
print("Split text:", words)  # Output: ['apple', 'banana', 'cherry']

new_text = "-".join(words)
print("Joined text:", new_text)  # Output: apple-banana-cherry

# 9. String Formatting
name = "Renuka"
age = 21
print(f"Formatted String: My name is {name} and I am {age} years old.")

# 10. Reversing a String
text5 = "Hello"
print("Reversed text:", text5[::-1])  # Output: olleH
