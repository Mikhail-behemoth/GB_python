# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

array = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'ant0n']

for j in range(0, len(array)):
    array1 = array[j]
    array_split = list(array1)
    count = 0
    for i in range(0, len(array_split)):
        if array_split[i] == 'a':
            del array_split[0:i+1]
            count = count + 1
            break
    for i in range(0, len(array_split)):
        if array_split[i] == 'n':
            del array_split[0:i+1]
            count = count + 1
            break
    for i in range(0, len(array_split)):
        if array_split[i] == 't':
            del array_split[0:i+1]
            count = count + 1
            break
    for i in range(0, len(array_split)):
        if array_split[i] == 'o':
            del array_split[0:i+1]
            count = count + 1
            break
    for i in range(0, len(array_split)):
        if array_split[i] == 'n':
            del array_split[0:i+1]
            count = count + 1
            break
    if count == 5:
        print(j+1, end=' ')