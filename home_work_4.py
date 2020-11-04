import math
import time

#------f(x,y)=sqrt(1+x**2+y**2)-------
def f (a):
    return math.sqrt(1+a[0]**2+a[1]**2)
def f1 (a):
    return [a[0]/math.sqrt(1+a[0]**2+a[0]**2),a[1]/math.sqrt(1+a[1]**2+a[1]**2)]
def f2 (a):
    return [(1+a[0]**2+a[1]**2+a[0])/(1+a[1]**2+a[1]**2)**1.5,a[0]*a[1]/math.sqrt(1+a[1]**2+a[1]**2),(1+a[0]**2+a[1]**2+a[1])/(1+a[1]**2+a[1]**2)**1.5]
# [f_xx, f_xy, f_yy] - матрица вторых частных производных
def f2_obratn (a):
    det=f2(a)[0]*f2(a)[2]-f2(a)[1]**2
    return [f2(a)[0]/det, f2(a)[1]/det, f2(a)[2]/det]

#---Метод пассивного поиска----
def pass_find (k1,k2,k3):
    a=-3
    b=3
    E=0.0001
    k = int((b - a) // E + 1)
    t = (b - a) / 20
    x = a
    mi_x = x
    mi = 10000
    for i in range(1, k + 1):
        f = math.sqrt(k1-2*k2*x+k3*x**2)
        if f < mi:
            mi = f
            mi_x = x
        x = x + t
    return(mi_x)

#---Метод пассивного поиска (2)----
def pass_find_2 (l,m,k1,k2):
    a=-3
    b=3
    E=0.0001
    k = int((b - a) // E + 1)
    t = (b - a) / 20
    x = a
    mi_x = x
    mi = 10000
    for i in range(1, k + 1):
        f = math.sqrt(1+(l-x*k1)**2+(m-x*k2)**2)
        if f < mi:
            mi = f
            mi_x = x
        x = x + t
    return(mi_x)


#----ускоренный градиентный спуск p-ого порядка-----
print('Ускоренный градиентный спуск p-ого порядка: ')
start_time=time.time()
a=[1,1]
a0=a # начальная точка
E=0.001
col_steps=0
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    if col_steps%3==0: # каждый 3 шаг
        a[0]=a[0]-a0[0]
        a[1] = a[1] - a0[1]
        a0=a
    k1=1+a[0]**2+a[1]**2
    k2=(a[0]**2+a[1]**2)/math.sqrt(1+a[0]**2+a[1]**2)
    k3=(a[0]**2+a[1]**2)/(1+a[0]**2+a[1]**2)
    alfa=pass_find(k1,k2,k3)
    a=[a[0]-alfa*f1(a)[0],a[1]-alfa*f1(a)[1]]

print("Точка минимума:", a)
print ("Количество шагов (вместе с МНГС):", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------

#----овражный метод-----
print('Овражный метод: ')
start_time=time.time()
a=[1,1]
a0=a
a0[0]=a[0]-0.001
a0[1]=a[1]-0.001 # вторая начальная точка
E=0.001
col_steps=0
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    if col_steps%3==0: # каждый 3 шаг
        a[0] =a [0]-a0[0]
        a[1] = a[1] - a0[1]

        k1 = 1 + a[0] ** 2 + a[1] ** 2
        k2 = (a[0] ** 2 + a[1] ** 2) / math.sqrt(1 + a[0] ** 2 + a[1] ** 2)
        k3 = (a[0] ** 2 + a[1] ** 2) / (1 + a[0] ** 2 + a[1] ** 2)
        alfa = pass_find(k1, k2, k3)
        a = [a[0] - alfa * f1(a)[0], a[1] - alfa * f1(a)[1]]
        a0[0] = a[0] - 0.001
        a0[1] = a[1] - 0.001

    else:
        k1=1+a[0]**2+a[1]**2
        k2=(a[0]**2+a[1]**2)/math.sqrt(1+a[0]**2+a[1]**2)
        k3=(a[0]**2+a[1]**2)/(1+a[0]**2+a[1]**2)
        alfa=pass_find(k1,k2,k3)
        a=[a[0]-alfa*f1(a)[0],a[1]-alfa*f1(a)[1]]

        k1 = 1 + a0[0] ** 2 + a0[1] ** 2
        k2 = (a0[0] ** 2 + a0[1] ** 2) / math.sqrt(1 + a0[0] ** 2 + a0[1] ** 2)
        k3 = (a0[0] ** 2 + a0[1] ** 2) / (1 + a0[0] ** 2 + a0[1] ** 2)
        alfa = pass_find(k1, k2, k3)
        a0 = [a0[0] - alfa * f1(a0)[0], a0[1] - alfa * f1(a0)[1]]

print("Точка минимума:", a)
print ("Количество шагов (вместе с МНГС):", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------

#----модифицированный метод Ньютона-----
print('Модифицированный метод Ньютона: ')
start_time=time.time()
a=[1,1]
E=0.001
col_steps=0
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    k1=f2_obratn(a)[0]*f1(a)[0]+f2_obratn(a)[1]*f1(a)[1]
    k2=f2_obratn(a)[1]*f1(a)[0]+f2_obratn(a)[2]*f1(a)[1]
    alfa=pass_find_2(a[0],a[1],k1,k2)
    a=[a[0]-alfa*k1,a[1]-alfa*k2]

print("Точка минимума:", a)
print ("Количество шагов (вместе с МНГС):", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------




