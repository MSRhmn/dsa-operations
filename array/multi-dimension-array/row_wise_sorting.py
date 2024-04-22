# Given a 2D array, sort each row of this array and print the result.


# Method 1 Using Bubble Sort Algorithm


def sort_row_wise(m_arr):
    """
    Sort an matrix array in ascending order using Bubble Sort algorithm.
    """
    # Loop for rows of matrix
    for i in range(len(m_arr)):
        # Loop for columns of matrix
        for j in range(len(m_arr[i]) - 1):
            # Loop for comparison and swapping
            swapped = False
            for k in range(len(m_arr[i]) - j - 1):
                if m_arr[i][k] > m_arr[i][k + 1]:
                    m_arr[i][k], m_arr[i][k + 1] = m_arr[i][k + 1], m_arr[i][k]
                    swapped = True
            # If no swap occured in the innerloop, hence the array is already sorted.
            if not swapped:
                break

    sorted_matrix(m_arr)


# Method 2 Using the built-in library function


def sort_matrix(m_arr):
    """Sort individual rows using built-in sort list method."""
    for i in range(len(m_arr)):
        m_arr[i].sort()

    sorted_matrix(m_arr)


# Print output function for matrix array


def sorted_matrix(m_arr):
    """Print the sorted matrix array."""
    for i in range(len(m_arr)):
        for j in range(len(m_arr[i])):
            print(m[i][j], end=" ")
        print()


if __name__ == "__main__":
    m = [[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]]
    sort_matrix(m)
