# Sort a list using selection sort algorithm


def selection_sort(arr):
    """
    Sorts a list of comparable elements using Selection Sort algorithm.
    Raises "TypeError" If any element in the data structure is not comparable.
    """
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    num_lst = [22, 5, 9, 7, 11, 2, 10, 3]
    print(f"The result of selection sort: {num_lst} -> {selection_sort(num_lst)}")


if __name__ == "__main__":
    main()
