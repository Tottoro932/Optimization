import math
#f(x)=tg(x)-2*sin(x)
a=0
b=math.pi/4
E=0.03
col_steps=0

print('Метод пассивного поиска')
k=int((b-a)//E+1)
x=a
mi_x=x
mi=10000
for i in range(1,k+1):
    f=math.tan(x)-2*math.sin(x)
    col_steps+=1
    if f<mi:
        mi=f
        mi_x=x
    x=x+E
print('точка минимума: x=',mi_x)
print('количество шагов:',col_steps)
print()
#----------------

print('Метод дихотомии')
col_steps=0
delta=E/4
b1=b
a1=a
while (b1-a1)/2> E:
    c=(a1+b1)/2-delta/2
    d=(a1+b1)/2+delta/2
    f_c=math.tan(c)-2*math.sin(c)
    f_d=math.tan(d)-2*math.sin(d)
    col_steps+=2
    if f_c<=f_d:
        b1=d
    else:
        a1=c
print('точка минимума: x=',(b1+a1)/2)
print('количество шагов:',col_steps)
print()
#---------------
print('Метод золотого сечения')
col_steps=0
a1=a
b1=b
d=0
c=0
while ((b1-a1)/2> E):
    if c==0:
        c=(3-math.sqrt(5))*(b1-a1)/2+a1
        f_c = math.tan(c) - 2 * math.sin(c)
        col_steps+=1
    if d==0:
        d=(math.sqrt(5)-1)*(b1-a1)/2+a1
        f_d=math.tan(d)-2*math.sin(d)
        col_steps += 1

    if f_c<=f_d:
        b1=d
        d=c
        c=0
    else:
        a1=c
        c=d
        d=0


print('точка минимума: x=',(b1+a1)/2)
print('количество шагов:',col_steps)
print()