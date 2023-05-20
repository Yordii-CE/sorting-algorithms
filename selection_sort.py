def selection_sort(file_name):    
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    print("Números ordenados con éxito utilizando Selection Sort.")

selection_sort('100.txt')
