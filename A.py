'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
inp = open("input.txt","r") 
otp = open("output.txt","w") 
N = list(inp.readlines()) 
A = list(map(int,N[1].split(" "))) 
for i in range(int(N[0])): 
    if A.count(A[i]) == 2: 
        otp.write(str(A[i])) 
        otp.close() 
        inp.close() 
        break 
    if A.count(A[int(N[0])-1-i]) == 2: 
        otp.write(str(A[int(N[0])-1-i])) 
        otp.close() 
        inp.close() 
        break 
