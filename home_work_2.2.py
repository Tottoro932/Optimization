import math
#------f(x,y)=sqrt(1+x**2+y**2)-------
def f (x,y):
    return math.sqrt(1+x**2+y**2)
def f1 (x,y):
    return x/math.sqrt(1+x**2+y**2)
def f2(x,y):
    return (1+y**2)/((1+x**2+y**2)**1.5)
def zol(a,k,E):
    E=E/10
    a1=a
    b1=a-a/4
    d=0
    c=0
    while ((b1-a1)/2> E):
        if c==0:
            c=(3-math.sqrt(5))*(b1-a1)/2+a1
            f_c = f(c,k)
        if d==0:
            d=(math.sqrt(5)-1)*(b1-a1)/2+a1
            f_d=f(c,k)

        if f_c<=f_d:
            b1=d
            d=c
            c=0
        else:
            a1=c
            c=d
            d=0
    return((b1+a1)/2)

#градиентный спуск (2)
x1=3
y1=3
x0=4
y0=4
col_steps=0
E=0.001
print("градиентный спуск")
while abs(f(x1,y1)-f(x0,y0))>E or math.sqrt((x1-x0)**2+(y1-y0)**2)>E:
    col_steps+=1
    # фиксируем 2 координату
    x0=x1
    y0=y1
    x1=zol(x0,y0,E)
    # фиксируем 1 координату
    y1 = zol(y0,x1,E)
print("метода касательных:",x1,y1)
print("количество итераций:",col_steps)

