def find_subarray_with_given_sum(arr, target_sum):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]
        if current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return (start, end)  
    return None  


# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target_sum = 12
    result = find_subarray_with_given_sum(arr, target_sum)
    if result:
        print(f"Subarray with given sum found from index {result[0]} to {result[1]}.")
    else:
        print("No subarray with the given sum found.")
