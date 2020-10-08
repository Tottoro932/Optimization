import math
import math
#f(x)=tg(x)-2*sin(x)
def f(x):
    return(math.tan(x)-2*math.sin(x))
def f1(x):
    return((1/math.cos(x)**2)-2*math.cos(x))
def f2(x):
    return(2*math.sin(x)/math.cos(x)**3+2*math.sin(x))
a=0
b=math.pi/4
E=0.03
col_steps=0
# метод касательных
print("медод касательных")
c=0
kol=0
if f1(a)<0 and f1(b)>0:
    while abs(b-a)>E or abs(f(b)-f(a))>E or kol<5:
        col_steps += 1
        kol+=1
        c=(f(b)-f(a)+f1(a)*a-f1(b)*b)/(f1(a)-f1(b))
        if f1(c)==0:
            break
        if f1(c)<0:
            a=c
        else:
            b=c

if f1(a)==0:
    c=a
else:
    c=b
print ("точка минимума: ",c)
print("количество шагов: ", col_steps)


# метод Ньютона-Рафсона
a=0
b=math.pi/4
E=0.03
col_steps=0
print("метод Ньютона-Рафсона")
kol=0
while abs(f1(b))>E or kol<5:
    if abs(f1(b))<E:
        kol+=1
    b=b-f1(b)/f2(b)
    col_steps+=1
print("точка минимума: ",b)
print("количество шагов: ", col_steps)

# метод секущих (хорд)
a=0
b=math.pi/4
E=0.03
col_steps=0
print("метод секущих")
kol=0
c=10
while abs(f1(c))>E or kol<5:
    kol+=1
    c=b-(b-a)*f1(b)/(f1(b)-f1(a))
    a=b
    b=c
    col_steps+=1
print("точка минимума: ", c)
print("количество шагов: ", col_steps)

