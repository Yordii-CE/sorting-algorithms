def counting_sort(file_name):

    with open(file_name, 'r') as archivo:
        numeros = [int(linea.strip()) for linea in archivo]

    valor_maximo = max(numeros)

    conteo = [0] * (valor_maximo + 1)

    for numero in numeros:
        conteo[numero] += 1

    numeros_ordenados = []
    for i in range(len(conteo)):
        numeros_ordenados.extend([i] * conteo[i])

    with open(file_name, 'w') as archivo:
        for numero in numeros_ordenados:
            archivo.write(str(numero) + '\n')

    print("Números ordenados con éxito utilizando Counting Sort.")

counting_sort('100.txt')
