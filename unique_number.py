my_list = [1, 2, 2, 3, 4, 5, 5, 6]
frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item] += 1  
    else:
        frequency[item] = 1  

unique_numbers = []
for key, value in frequency.items():
    if value == 1:
        unique_numbers.append(key)

print("Unique numbers:", unique_numbers)
