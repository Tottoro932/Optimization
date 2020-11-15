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
        f = math.sqrt(k1+2*k2*x+k3*x**2)
        if f < mi:
            mi = f
            mi_x = x
        x = x + t
    return(mi_x)


#----Метод Флетчера-Ривза-----
print('Метод Флетчера-Ривза: ')
start_time=time.time()
a=[1,1]
a0=a # начальная точка
E=0.0001
col_steps=0
d_k=[-1*f1(a)[0], -1*f1(a)[1]]
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    k1 = 1 + a[0] ** 2 + a[1] ** 2
    k2 = (a[0]*d_k[0]+a[1]*d_k[1])
    k3 = d_k[0]**2+d_k[1]**2
    alfa = pass_find(k1, k2, k3)
    if col_steps%3==0: # каждый 3 шаг
        a=[a[0]+alfa*d_k[0], a[1]+alfa*d_k[1]]
        d_k = [-1 * f1(a)[0], -1 * f1(a)[1]]
    else:
        a = [a[0] + alfa * d_k[0], a[1] + alfa * d_k[1]]
        betta=(f1(a)[0]**2+f1(a)[1]**2)/(f1(a0)[0]**2+f1(a0)[1]**2)
        d_k=[-1*f1(a)[0]+betta*d_k[0], -1*f1(a)[1]+betta*d_k[1]]
    a0=a

print("Точка минимума:", a)
print ("Количество шагов:", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------

#----Метод Полака-Рибьера-----
print('Метод Полака-Рибьера: ')
start_time=time.time()
a=[1,1]
a0=a # начальная точка
E=0.0001
col_steps=0
d_k=[-1*f1(a)[0], -1*f1(a)[1]]
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    k1 = 1 + a[0] ** 2 + a[1] ** 2
    k2 = (a[0]*d_k[0]+a[1]*d_k[1])
    k3 = d_k[0]**2+d_k[1]**2
    alfa = pass_find(k1, k2, k3)
    if col_steps%3==0: # каждый 3 шаг
        a=[a[0]+alfa*d_k[0], a[1]+alfa*d_k[1]]
        d_k = [-1 * f1(a)[0], -1 * f1(a)[1]]
    else:
        a = [a[0] + alfa * d_k[0], a[1] + alfa * d_k[1]]
        betta=(f1(a)[0]*(f1(a)[0]-f1(a0)[0])+f1(a)[1]*(f1(a)[1]-f1(a0)[1]))/(f1(a0)[0]**2+f1(a0)[1]**2)
        d_k=[-1*f1(a)[0]+betta*d_k[0], -1*f1(a)[1]+betta*d_k[1]]
    a0=a

print("Точка минимума:", a)
print ("Количество шагов:", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------





