'''Backtracking:
Backtracking is a recursive algorithmic technique used to 
solve problems by trying all possible solutions and undoing
(backtracking) steps if they lead to a dead end.
It is commonly used for problems like N-Queens, Sudoku Solver, and Subsets Generation.'''


def generate_subsets(nums, current, index):
    if index == len(nums):  
        print(current)      
        return
    current.append(nums[index])
    generate_subsets(nums, current, index + 1)
    current.pop()
    generate_subsets(nums, current, index + 1)


nums = [1, 2, 3]
print("All subsets of", nums, "are:")
generate_subsets(nums, [], 0)
