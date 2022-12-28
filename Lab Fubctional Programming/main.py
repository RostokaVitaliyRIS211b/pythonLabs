from functools import reduce
import csv
#Задача 1: посчитать сумму первого столбца
#Задача 2: Наибольший элемент второго столбца
with open("bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv", "r") as file:
    #Задача№1
    csv_file=csv.reader(file)
    f = filter(lambda x: x[1] != 'NaN', csv_file) #Исключаем аргументы равные NaN
    next(f) #Скипаем первую запись
    m = map(lambda x: float(x[1]),f) #Первый столбец
    s = reduce(lambda accumulator, value: accumulator+value, m) # Подсчет суммы
    #print('Summ: ',s)
    file.seek(0)
    #Задача№2
    csv_file=csv.reader(file)
    f = filter(lambda x: x[2] != 'NaN', csv_file)
    next(f)
    m = map(lambda x: float(x[2]),f)
    result = reduce(max, m) # Нахождение максимального аргумента
    #print('Max: ', result)
    ftxt = open('output.txt','w')
    ftxt.write(f'Summ: {s}\nMax: {result}')
    ftxt.close()