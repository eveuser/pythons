# -*- coding: utf-8 -*-
"""06/01_20512심완기-2차원 리스트~내포

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iqBNGJBskAhIFBOadbaibbrhkJfemZU5
"""

#37
numbers = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]

sum = 0
i = 0
print("짝수 번쨰  요소 :",end="")

while i<len(numbers):
  if (i+1)%2==0:
    sum+=numbers[i]
    print(numbers[i], end =' ')
  i+=1
print("\n합계 : ", sum)

#38
numbers = [[10, 20, 30],[40,50,60]]
numbers

print(numbers[0])
print(numbers[1])

print(numbers[0][1])
print(numbers[1][2])

for sub in numbers:
  for s in sub: 
    print(s, end=' ')
  print()

#42

data = [[10, 20], [30, 40], [50, 60], [70,80]]

for i in range(len(data)):
  for j in range(len(data[i])): 
    print('%d'%data[i][j], end=' ')
  print()

#43
strings = [["원두커피", "라떼", "콜라"], ["우동", "국수", "피자", "파스타"]]

print(len(strings))
print(len(strings[0]))
for i in range(len(strings)):#2
  for j in range(len(strings[i])): #3
    print('%s'%strings[i][j], end=' ')
  print()

#44
data = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]
print(data)
for i in range(3):
  for j in range(1): #3
    print('%d'%data[i][j], end=' ')
  print()

#45
score = [
       [88,76,92,98],
       [65,70,58,82],
       [82,80,78,88],
       ]

total = 0
totalsub = 0
for stu in score:
  sum=0
  for s in stu:
    sum +=s
  subjects=len(stu)#한 학생의 과목수
  print("총점 : ", sum, "평균 : ", sum/subjects)
  total +=sum
  totalsub += subjects
print("전체평균 : ", total/totalsub)

#46
seats = [[0,0,0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0,0,0],\
         [1,1,1,0,0,0,0,0,1,0],\
         [0,0,0,0,0,1,0,0,0,0],\
         [0,1,0,0,0,1,0,1,0,0],\
         [0,0,0,0,0,0,1,0,0,0],\
         [1,0,1,0,0,0,0,0,0,1]]

for i in range():
  for j in range():

    if seats == 0:
      print('$%3s' %'□', end='')
    else :
      print('$%3s' %'■', end='')
  print()

print('\n 예약가능 : ■, 예약불가 : □')

#47
scores = [[96, 84 ,80],[96, 86,76], [76, 95, 83],[89, 96, 69],[83, 86, 79],[85, 90, 83]]


sum = 0
i = 0
while i<len(scores):
  sum = 0
  j = 0
  while j<len(scores[i]):
    sum += scores[i][j]
    j+=1
  avg =sum/len(scores[i])
  print('%d번째 학생의 합계 : %d, 평균 : %.2f'%(i+1, sum, avg))
  i+=1

scores = [[96, 84 ,80],[96, 86,76], [76, 95, 83],[89, 96, 69],[83, 86, 79],[85, 90, 83]]


for i in range(len(scores)):
  sum = 0
  
  for j in range(len(scores[i])):
    sum += scores[i][j]
  avg =sum/len(scores[i])
  print('%d번째 학생의 합계 : %d, 평균 : %.2f'%(i+1, sum, avg))
  i+=1

#48
scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83],[89, 96, 69,], [83,86, 79],[85, 90, 83]]

print(len(strings))
print(len(strings[0]))
for i in range(len(strings)):#2
  for j in range(len(strings[i])): #3
    print('%s'%strings[i][j], end=' ')
  print()



for i in range(10):
  print(i, end=' ')

num = []
for i in range(10):
  num.append(i)
print(num)

[i for i in range(10) if i%2 == 0]

[i*i for i in range(10) ]

[i*2 for i in range(10) ]

from IPython.core import events
#50
even1 = [i for i in range(100) if i%2 == 0]
even2 = [i*2 for i in range(0,51)]
even3 = [i for i in range(0, 100, 2)]

print(even1)
print(even2)
print(even3)

#51
li = []
for n in range(1, 10):
  if n%3 ==0:
    li.append(n*n)
print(li)

#51-1
[n*n for n in range(1,10) if n%3 ==0]

#52
numbers = [1, 2, 3, 4, 5 ]
result = []
for n in numbers:
  if n % 2 == 1:
    result.append(n*2)

#52-1
result = [i for i in range(12) if (i+2)%4 == 0]
print(result)



#연습 1
v = [17, 92, 18, 33, 58, 7, 33, 42]

max = v[0]

for i in range(len(v)):
  if v[i]>max:
    max =v[i]
print('최대값=',max)

#연습2
for i in [1,2,3]:
  for j in['a', 'b', 'c']:
    print(i*j, end=' ')

#연습 3
list_a = ["I", "study", "python","language", "!" ]

for i in list_a:
  if len(i)>3:
    print(i)