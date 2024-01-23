# Searching position of a item in a list using binary search algorithm


def binary_search(lst, item):
    """
    binary_search function takes a list and a item number.
    Returns items index number in the list.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if item < lst[mid]:
            high = mid - 1
        elif item > lst[mid]:
            low = mid + 1
        else:
            return mid
    return None


def main():
    num_list = [3, 4, 5, 9, 10, 11, 24, 28, 31, 40, 41, 42, 50]
    print(num_list)
    index = int(input("Enter a item from the list to get is's index: "))
    print(f"Index of {index} is {binary_search(num_list, index)}")


if __name__ == "__main__":
    main()
