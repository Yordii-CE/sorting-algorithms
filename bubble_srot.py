def bubble_sort(file_name):
    with open(file_name, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]

    n = len(numeros)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    with open(file_name, 'w') as archivo:
        for numero in numeros:
            archivo.write(str(numero) + '\n')

    print("Números ordenados con éxito utilizando Bubble Sort.")

bubble_sort('100.txt')
