def quick_sort(file_name):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    quick_sort_helper(numbers, 0, len(numbers) - 1)

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    print("Números ordenados con éxito utilizando Quick Sort.")

quick_sort('100.txt')
