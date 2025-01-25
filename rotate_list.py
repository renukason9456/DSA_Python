def rotate_array(arr, positions, direction='right'):
    positions %= len(arr)  # Handle rotations greater than array length
    if direction == 'left':
        return arr[positions:] + arr[:positions]
    return arr[-positions:] + arr[:-positions]


# Example usage
array = [1, 2, 3, 4, 5, 6, 7]
positions = 5

print("Original array:", array)
print("Rotated to the right by 3:", rotate_array(array, positions, 'right'))
print("Rotated to the left by 3:", rotate_array(array, positions, 'left'))