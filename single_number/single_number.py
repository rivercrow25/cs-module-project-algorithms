'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    for k, v in counts.items():
        if v == 1:
            return k
    # duplicates = []
    # for i in range(len(arr)):
    #     k = i + 1
    #     for j in range(k, len(arr)):
    #         if arr[i] == arr[j]:
    #             duplicates.append(arr[i])
    # for a in arr:
    #     if not a in duplicates:
    #         return a


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
