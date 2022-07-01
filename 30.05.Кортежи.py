# korteg=(9)
# print(type(korteg))
# korteg=(9,0,[9,4,7])# можем изменить вложенный список
# korteg[2][1]=9
# print(korteg)

# x=(1,2,3,4)# сложение кортежей
# y=(5,6,7,8)
# z=x+y
# print(z)

# x=(1,2,3,4)# умножение кортежей
# y=(5,6,7,8)
# z=x * 2
# print(z)
# l=y * 3
# print(l)
#(1, 2, 3, 4, 1, 2, 3, 4)
#(5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8)

#
# a=(1,2,3,4,5,5) # находим  максим и миним знач
# print("max", max(a),'min', min(a))

# list=[i for i in range(6)] #генератор списка первая i то чем будет заполняться список
# print(list)

# list=['a' for i in range(6)]
# print(list)
# ['a', 'a', 'a', 'a', 'a', 'a']

# list=['2a' for i in range(6)] # range(6) #список будет стоять из 6 элемент,
                                           #'2a' for i in-чем будем заполнять
# print(list)
# ['2a', '2a', '2a', '2a', '2a', '2a']

# list2=[] #с помощью функции
# for i in range(6):
#     list2.append('a2')
# print(list2)

# import random
# list=[random.randint(1,100)for i in range(1)]
# list=tuple(list)
# print(list)
# print(max(list),min(list))


# import random
# list=[random.randint(0,5) for i in range(10)]
# kg=tuple(list)#перевели лист в кортеж
# list2=[random.randint(-5,0) for x in range(10)]
# kg2=tuple(list2) #перевели лист в кортеж
# print(kg, kg2, sep='\n') #напечатали кортежи первый и второй
# sum=kg+kg2
# print(sum)
# print(sum.count(0))# посчитали количество нулей

# import random
# a=tuple([random.randint(0,5) for _ in range(10)])
# b=tuple([random.randint(-5,0) for _ in range(10)])
# c=a+b
# print(c,'\n Количество нулей:', c.count(0))


# вывести данные кортежа без скобок, через запятую
#Обязательно: элементы кортежа-
# list=('n', 'a','t') # в кортеже тип элементов str
# list2=','.join(list)
# print(list2)

# list1=('n', 'a','t')
# for i in list1:
#     print(type(list1))# печатаем (спрашиваем) какой тип
#     class 'tuple'>
#     class 'tuple'
#     class 'tuple'>


# # решаем по индексам: инд0+инд1+инд2...
# list1=('n', 'a','t')
# list1=list(list1)
# for i in list1:
#       print(type(list1))
# print(list1[0],'-', list1[1], ',', list1[2])
# print(list1[0], list1[1],  list1[2], sep=',')

# решаем по индексам: инд0+инд1+инд2...
# list1=('n', 'a','t')
# print(list1[0], list1[1],  list1[2], sep=',')

# A=(13,5,43,67,32,12,98,6,10,34,20,55,8,14,60,14)
# B=(53,21,4,23,76,3,43,12,54,342,21)
# if sum(A)>sum(B):
#     print('сумма больше в кортеже A')
# else:
#     print('сумма больше в кортеже B')
#
# min1=min(A)
# min2=min(B)
# print(min1)
# print(min2)
#
# print(A.index(min1))
# print(B.index(min2))

# nums=[5,7,8]
# data=tuple(nums)
# world=tuple ('Hello world')
# print(world)
# #('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')


#закрепление 1.
# l=(0,1,2,3,4,5,6,7,8,9)
# print('sum=', sum(l))
# sum= 45

#закрепление 2.
# long_word=('т','т','а','и','и','а','и','и','и','т','т','а','и','и','и','и','и','т','и')
# print("Буква 'т' встречается:", long_word.count('т'), "раз")
# print("Буква 'а' встречается:", long_word.count('а'), "раз")
# print("Буква 'и' встречается:", long_word.count('и'), "раз")
# Буква 'т' встречается: 5 раз
# Буква 'а' встречается: 3 раз
# Буква 'и' встречается: 11 раз

#закрепление 3.#посчитать кол-во дней на основе
# week_temp=(26,29,34,32,28,26,23)
# sum_temp=sum(week_temp)
# days=len(week_temp)
# mean_temp=sum_temp/days
# print("сумма t за неделю:", sum(week_temp))
# print("количество дней:", len(week_temp))
# print("средняя температура за 7 дней:", int(mean_temp))
#сумма t за неделю: 198
#количество дней: 7
#средняя температура за 7 дней: 28


#дом задание:
# найти самое длиное слово в строке.
# l='я помня чудное мгновение'
# print(max(l.split())) #split() разбивает строку на слова ( split() пробелами);
#                               # max() находит наибольший элемент, используя встроенную функцию len()
                              #указатель len() в виде параметра key сортировка производится по длине.

#дом задание:
# найти самое длиное слово в строке.
# a='я помня чудное мгновение'
# print(a)
# a1=a.split()
# print(a1)
# i=0
# for i in a1:
#     if дописать
#     l+=1
# print(len(a1))
# print(max(a1,key=len))

# найти самое длиное слово в строке.
# l='я помня чудное мгновение'
# print(max(l.split(),key=len))




#дом задание:
#преобразовать текст в список слов с удалением знаков препинания
# str='солнце - это планета'# 'дан текст
# d=str.split() # преобразую в список
# print(d)
# d.remove(d[1]) # удаляю элемент 'знак препинания'
# print(d)

