# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.
a=[10,24,54,67,43,11,1,5]
b=[]
for i in a:
    if i%2==0:
        i = i/4
        b.append(int(i))
    else:
        i=i*2
        b.append(int(i))
print(b)