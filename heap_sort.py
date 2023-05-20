def heap_sort(file_name):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    build_heap(numbers)
    sorted_numbers = []
    while numbers:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        sorted_numbers.insert(0, numbers.pop())
        heapify(numbers, len(numbers), 0)

    with open(file_name, 'w') as file:
        for number in sorted_numbers:
            file.write(str(number) + '\n')

    print("Números ordenados con éxito utilizando Heap Sort.")

heap_sort('100.txt')
