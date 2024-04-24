def column_wise_sorting(m_arr):
    n = len(m_arr)

    for i in range(len(m_arr)):
        for j in range(len(m_arr[i])):
            print(m_arr[j][i], end=" ")
        print()


if __name__ == "__main__":
    m = [[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]]
    column_wise_sorting(m)
