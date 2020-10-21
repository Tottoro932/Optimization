import math

#------f(x,y)=sqrt(1+x**2+y**2)-------
def f (a):
    return math.sqrt(1+a[0]**2+a[1]**2)
def f1 (a):
    return [a[0]/math.sqrt(1+a[0]**2+a[0]**2),a[1]/math.sqrt(1+a[1]**2+a[1]**2)]

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

#----метод наискорейшего градиентного спуска-----
print('МНГС: ')
a=[1,1]
E=0.001
col_steps=0
while math.sqrt(f1(a)[0]**2+f1(a)[1]**2)>E:
    col_steps+=1
    k1=1+a[0]**2+a[1]**2
    k2=(a[0]**2+a[1]**2)/math.sqrt(1+a[0]**2+a[1]**2)
    k3=(a[0]**2+a[1]**2)/(1+a[0]**2+a[1]**2)
    alfa=pass_find(k1,k2,k3)
    a=[a[0]-alfa*f1(a)[0],a[1]-alfa*f1(a)[1]]
print("Точка минимума:", a)
print ("Количество шагов:", col_steps)
print()
#-------------------------------

#---Метод с дроблением шага-----
print("Метод с дроблением шага: ")
xk=[1,1]
E=0.001
drobitel=0.5
delta=0.5
alfa=1
col_steps=0
f_x=-200  # для входа во второй цикл
f_xk=-100 # для входа во второй цикл
while math.sqrt(f1(xk)[0]**2+f1(xk)[1]**2)>E:
    alfa=1
    col_steps += 1
    while f_x-f_xk>(-1)*alfa*delta*(f1(xk)[0]**2+f1(xk)[1]**2):
        alfa=alfa*drobitel
        x=[xk[0]-alfa*f1(xk)[0],xk[1]-alfa*f1(xk)[1]]
        f_x=f([a[0]-alfa*f1(a)[0],a[1]-alfa*f1(a)[1]])
        f_xk=f(a) #xk-точка в которой сейчас находимся
    xk=[xk[0]-alfa*f1(xk)[0],xk[1]-alfa*f1(xk)[1]]
print("Точка минимума: ",xk)
print("количество шагов: ",col_steps)
print()

#----Метод с постоянным шагом-----------
print("Метод с постоянным шагом: ")
xk=[1,1]
E=0.001
alfa=0.1
col_steps=0
while math.sqrt(f1(xk)[0]**2+f1(xk)[1]**2)>E:
    col_steps += 1
    xk=[xk[0]-alfa*f1(xk)[0],xk[1]-alfa*f1(xk)[1]]
print("Точка минимума: ",xk)
print("количество шагов: ",col_steps)
print()

#------Метод с заранее заданным шагом--------
print("Метод с заранее заданным шагом: ")
xk=[1,1]
k=0
E=0.001
col_steps=0
while math.sqrt(f1(xk)[0]**2+f1(xk)[1]**2)>E:
    col_steps += 1
    k+=1
    alfa=1/k
    xk=[xk[0]-alfa*f1(xk)[0],xk[1]-alfa*f1(xk)[1]]
print("Точка минимума: ",xk)
print("количество шагов: ",col_steps)
print()