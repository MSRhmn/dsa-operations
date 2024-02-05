def insertion_sort(arr):
    """
    Sorts an array in ascending order using Insertion Sort algorithm.
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def main():
    num_lst = [11, 4, 8, 9, 5, 2]
    print(f"After applying insertion sort to: {num_lst} -> {insertion_sort(num_lst)}")


if __name__ == "__main__":
    main()
