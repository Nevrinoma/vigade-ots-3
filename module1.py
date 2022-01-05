from random import *
def arvud_loendis():
    print("Данные: ")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    pos=neg=null=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты: ")
    print("Полученный список от ",mini," до ",maxi,s)
    s.sort()
    print("Отсортированный список ",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов ",pos)
    print("Список отрицательных элементов ",neg)
    print("Список нулевых элементов ",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных: ",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных: ",kesk)
    print("Добавляем средние в изначалный массив: ")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """
    Меняем значение местами при помощи третей переменной.Дополнительная переменная принимает значение a,переменная а принимает значение b,
    затем переменная b принимает значение дополнительной.
    :param int a: 
    :param int b:
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    Генерирует числа от а до b в значении n
    :param int n: количество чисел
    :param int a: минимальное количество
    :param int b: максимальное количество
    :param list loend: список сгенерированых чисел
    """
    for i in range (n):
        loend.append(randint(a,b)) 

def jagamine(loend:list,p:list,n:int,nol:list):
    """
    Сортируем положительные и отрицательные числа
    :param list loend: список всех чисел
    :param list p: положительные числа
    :param list n: отрицательные числа
    :param list nol: нули
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)


def keskmine(loend:list):
    """
    Ищем среднее число
    :param list loend:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2) #Находим среднее путем деление суммы на два и округляем до 2 знаков после запятой
    return kesk

def lisamine(loend:list,el:float):
    """
    Добавляем число в список
    :param list loend:
    :param el float:
    """
    loend.append(el)
    loend.sort()

