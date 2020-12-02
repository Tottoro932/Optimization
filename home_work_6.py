import math
import time

#------f(x,y)=x^2+y^2-20*x-30*y-------
#----условия: 1) 5*x+13*y-51<=0
#-------------2) 15*x+7*y-107<=0
#-------------3) -x<=0
#-------------4) -y<=0

#---функция H----
def H_fun (x,y):
    return (max(0, 5*x+13*y-51))**2 + (max(0, 15*x+7*y-107))**2 +  (max(0, -x))**2 + (max(0, -y))**2

#--------функция на вход в мнгс-----
def Func_mngs(x,y):
    a=[x,y]
    return a[0] ** 2 + a[1] ** 2 - 20 * a[0] - 30 * a[1] + r_k * (
                (max(0, 5 * a[0] + 13 * a[1] - 51)) ** 2 + (max(0, 15 * a[0] + 7 * a[1] - 107)) ** 2 + (
            max(0, -1*a[0])) ** 2 + (max(0, -1*a[1])) ** 2)




#----метод наискорейшего градиентного спуска-----
def MNGS(r_k,x,y):
#- поиск минимума функции f(x,y)=x^2+y^2-20*x-30*y + r_k*H
    print("Начинаю МНГС...")
    a=[x,y]
    E=0.01
    col_steps=0
    Func_mngs_x= 10
    Func_mngs_y= 10

    while math.sqrt(Func_mngs_x**2+Func_mngs_y**2)>E: #fabs- модуль
        #print("Метод МНГС:", col_steps)
        #print(a)
        col_steps+=1
        f1_a_0=0
        f1_a_1=0
        f2_a_0=0
        f2_a_1=0
        f3_a_0=0
        f4_a_1=0
        if (max(0, 5*a[0]+13*a[1]-51))!=0:
            f1_a_0=5
            f1_a_1=13
        if max(0, 15*a[0]+7*a[1]-107)!=0:
            f2_a_0=15
            f2_a_1=7
        if max(0, -a[0]) !=0:
            f3_a_0=-1
        if max(0, -a[1]) !=0:
            f4_a_1=-1

        Func_mngs_x=2*a[0]-20 + r_k*(2*(5*a[0]+13*a[1]-51)*f1_a_0+2*(15*a[0]+7*a[1]-107)*f2_a_0+2*(-1*a[0])*f3_a_0)  #- производная Func_mngs по х----
        Func_mngs_y=2*a[1]-30+r_k*(2*(5*a[0]+13*a[1]-51)*f1_a_1+2*(15*a[0]+7*a[1]-107)*f2_a_1+2*(-1*a[1])*f4_a_1)
        #print(Func_mngs_x,' ', Func_mngs_y)
        alfa=pass_find(r_k,Func_mngs_x,Func_mngs_y,a[0],a[1])
        #print("Полученный альфа: ",alfa)

        a=[a[0]-alfa*Func_mngs_x,a[1]-alfa*Func_mngs_y]
        print("Следующая точка МНГС", a)
        #print("выход", math.sqrt(Func_mngs_x ** 2 + Func_mngs_y ** 2))

    return [a[0],a[1]]
#-------------------------------

#---Метод пассивного поиска----
def pass_find ( r_k, Func_mngs_x,Func_mngs_y,a_0,a_1):
    a=0
    b=30
    E=0.001
    k = int((b - a) // E + 1)
    t = (b - a) / k
    x = a
    mi_x = x
    mi = 10000
    #print("Ищу минимум...")
    for i in range(1, k + 1):
        f = (a_0-x*Func_mngs_x)**2+(a_1-x*Func_mngs_y)**2-20*(a_0-x*Func_mngs_x)-30*(a_1-x*Func_mngs_y)+r_k*(
                (max(0, (5*(a_0-x*Func_mngs_x)+13*(a_1-x*Func_mngs_y)-51)))**2+(max(0, (15*(a_0-x*Func_mngs_x)+7*a_1-107)))**2+(max(0, (-1*(a_0-x*Func_mngs_x))))**2 + (max(0, (-1*(a_1-x*Func_mngs_y)))**2))
        if f < mi:
            mi = f
            mi_x = x
        x = x + t
    return(mi_x)



#----Метод внешних штрафов-----
print('Метод внешних штрафов: ')
start_time=time.time()
a = [6, 4] # начальная точка
E = 1
r_k = 1
col_steps = 0
#print(H_fun(a[0],a[1]))
while H_fun(a[0],a[1])>E: #or math.sqrt((a[0]-5)**2+(a[1]-2)**2)>E:
    col_steps+=1
    print("Метод внешних штрафов:", col_steps)
    #print(a)
    a[0]=MNGS(r_k,a[0],a[1])[0]
    a[1]=MNGS(r_k,a[0],a[1])[1]
    r_k=r_k*10
    print(a)
    print(H_fun(a[0],a[1]))

print("Точка минимума:", a)
print("Количество шагов:", col_steps)
print("затраченное время:", time.time()-start_time)
print()
#-------------------------------





