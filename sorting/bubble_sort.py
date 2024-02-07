def bubble_sort(arr):
    """
    Sorts an array in ascending order using Bubble Sort algorithm.
    """
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap occured in the innerloop, hence the array is already sorted.
        if not swapped:
            break

    return arr


def main():
    num_lst = [4, 11, 9, 15, 5, 2]
    print(f"Applying bubble sort on {num_lst} -> {bubble_sort(num_lst)}")


if __name__ == "__main__":
    main()
