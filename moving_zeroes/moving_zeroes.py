'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # plan
    # itterate through the list
    # swap the element to a counters index
    # when an element is not zero increment a counter
    counter = 0
    for i in range(len(arr)):
        if arr[i] is not 0:
            last = arr[counter]
            arr[counter] = arr[i]
            arr[i] = last
            counter += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
