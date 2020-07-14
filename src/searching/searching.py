# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # First we establish our middle point in the list/array
    # We create a variable called middle
    # Then, we add our start and end before dividing the floor by 2
    middle = (start + end) // 2
    
    # We do a check for array length.
    # IF it is 0, then we do not need to go further. 
    if len(arr) == 0:
        return -1

    # Similar notes on the regular binary search
    # We first check if the middle value is our target
    # If so, then simply return because we found it.
    if arr[middle] == target:
        return middle
    # If the middle is greater than our target value
    # We call the function and make our end value the middle value
    # Because it is no longer needed.
    # We can then continue to run iterations till we find out target.
    elif arr[middle] > target:
        return binary_search(arr, target, start, middle)
    # If the middle is smaller than our target value
    # We call the function and make our start value the middle value
    # Because it is no longer needed.
    # We can then continue to run iterations till we find out target.
    elif arr[middle] < target:
        return binary_search(arr, target, middle, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

