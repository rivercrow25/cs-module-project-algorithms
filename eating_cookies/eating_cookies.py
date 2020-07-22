'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
    """
    notes so u cant say i dont understand it :D
    we start with 2 base cases, if n is 1 or 0 and if n is 2
    in those cases the the count can only increase by 1 determined amount
    but what if n is 3 or greater? things get exponetially bigger so we reduce n by using recursion until it reaches the base case
    by all allowed increments
    as it comes back up you reach the sum of all possible moves
    """


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
