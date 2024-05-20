# Given a matrix arr[][] of size M x N, where every row and column is sorted in increasing order, and a number X is given.
# The task is to find whether element X is present in the matrix or not.


def search_in_matrix(arr, x):
    # M = 4, N = 5
    for i in range(0, 4):
        for j in range(0, 5):
            if arr[i][j] == x:
                return 1
    return


x = int(input("Enter the value of 'X': "))
arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128],
]

if search_in_matrix(arr, x):
    print("YES")
else:
    print("NO")
