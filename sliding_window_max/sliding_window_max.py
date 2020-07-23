'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque


def sliding_window_max(nums, k):
    # Your code here
    Qi = deque()
    arr = []
    for i in range(k):
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, len(nums)):
        arr.append(nums[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()

        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    arr.append(nums[Qi[0]])
    return arr


arr = [1, 3, -1, -3, 5, 3, 6, 7]
print(sliding_window_max(arr, 3))
# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(
#         f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
