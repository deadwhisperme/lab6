'''
Задача C
++++++++

В прихожей в ряд стоит N тапочек, которые бывают разных размеров, а также левыми и правыми. Гость выбирает два тапочка,
удовлетворяющих следующим условиям:

- выбранные тапочки должны быть одного размера;
- из выбранных тапочков левый тапочек должен стоять левее правого;
- если можно выбрать несколько пар тапочек, удовлетворяющих первым двум условиям, то выбирается два тапочка с наименьшим
  расстоянием между ними.

  В первой строке входны данных записано число тапочков N. Во второй строке записаны размеры тапочков в порядке слева
  направо, при этом левые тапочки условно обозначаются отрицательными числами (то есть -s обозначает левый тапочек, а s
  обозначает правый тапочек размера s).

  Выведите одно число: минимальное расстояние между двумя тапочками одного размера таких, что левый тапочек стоит левее
  правого. Если таких пар тапочек нет, то выведите одно число 0.

  +----------------------+-------+
  | Ввод                 | Вывод |
  +======================+=======+
  | 6                    | 2     |
  +----------------------+-------+
  | -40 41 -42 -41 42 40 |       |
  +----------------------+-------+
'''
q = 0
inp = open('input.txt','r')
out = open('output.txt','w')
N = int(inp.readline())
A = inp.readline().split()
for i in range(N):
  A[i] = int(A[i])
m = N + 1
for i in range(N):
  if((A[i]) < 0) and (A[i+1:].count(-A[i]) > 0):
    q = A.index(-A[i])-i
    if q < m:
      m = q
if m == N + 1:
  print(0, file=out)
else:
  print(m, file=out)

