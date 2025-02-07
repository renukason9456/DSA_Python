def convertZigzag(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s  # No zigzag needed

    rows = [''] * numRows  # Create a list of strings for each row
    row = 0  # Counter variable to track the current row
    step = 1  # Step to control the movement (1 for down, -1 for up)

    for char in s:
        rows[row] += char  # Append the character to the current row
        
        # Change direction if we hit the first or last row
        if row == 0:
            step = 1  # Move down
        elif row == numRows - 1:
            step = -1  # Move up
        
        row += step  # Move to the next row

    return ''.join(rows)  # Combine all rows into a single string

# Example
s = "PAYPALISHIRING"
numRows = 3
print(convertZigzag(s, numRows))  # Output: "PAHNAPLSIIGYIR"
