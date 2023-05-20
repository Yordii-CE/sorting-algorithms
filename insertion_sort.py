def insertion_sort(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    print("Números ordenados con éxito utilizando Insertion Sort.")

insertion_sort('100.txt')
