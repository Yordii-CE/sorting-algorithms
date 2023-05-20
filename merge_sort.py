def merge_sort(file_name):
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [arr[left + i] for i in range(n1)]
        R = [arr[mid + 1 + i] for i in range(n2)]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    merge_sort_helper(numbers, 0, len(numbers) - 1)

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    print("Números ordenados con éxito utilizando Merge Sort.")

merge_sort('100.txt')
