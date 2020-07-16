# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Create a new array that will store the "sorted" values
    merged_arr = []

    # Check to make sure both arrays have values in them
    # Run it in a while loop
    # So, while array A and B are greater than 0
    while len(arrA) > 0 and len(arrB) > 0:
        # First, let's evalute if the first value of array A
        # is larger than the first value of array B
        if arrA[0] > arrB[0]:
            # If so, append the smaller B value to the merged array
            merged_arr.append(arrB[0])
            # Then, pop this value out of the main array B
            arrB.pop(0)
        # If this is not the case, then take the smaller A 
        # value and append IT to the merged array
        # Then, pop that value from the original array A
        else:
            merged_arr.append(arrA[0])
            arrA.pop(0)
    # Finally, we will check to see if each array is greater than 0
    # Starting with array A, then array B
    # While they have some values, we will take the first
    # element and append it to the merged array.
    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)

    # Lastly we return the merged array
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # First, we want to make sure the new merged array
    # has some elements in it with a simple if length check
    if len(arr) > 1:
        # Second, we create our start, middle, and end points of the array
        # The middle is the same as always
        # We take the length and divide it to the floor by two
        # Start is now looking at everything before the middle
        # End is looking at everything after the middle
        middle = len(arr)//2
        start = arr[:middle]
        end = arr[middle:]
        # Here is the actual recursion by calling first merge,
        # passing in the merge sort function with the start array
        # then passing in the second argument of the end array values
        return merge(merge_sort(start), merge_sort(end))
    # If the array is less than 1, simple return the array.
    else:
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
# TODO