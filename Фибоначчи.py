import math

#f(x)=tg(x)-2*sin(x)
a=0
b=math.pi/4
E=0.03
col_steps=0
# Fn+2>=1.1(b-a)/E  =>  Fn+2>=28,6 => n=7
n=7

def fibonachi(k):
    if (k==1) or (k==2):
        return 1
    k1=1
    k2=1
    for i in range(3,k+1):
        a=k2
        k2=k2+k1
        k1=k2
    return k2

def f(a):
    return math.tan(a)-2*math.sin(a)


print('Метод Фибоначчи')

c=a+(b-a)*fibonachi(n)/fibonachi(n+2)
d=a+(b-a)*fibonachi(n+1)/fibonachi(n+2)

for i in range(1,n+1):
    col_steps+=1
    if f(c)>f(d):
        a=c
        c=d
        d=a+(b-a)*fibonachi(n+1-i)/fibonachi(n+2-i)
    else:
        if f(c)==f(b):
            print("значения стали равными на", i, "шаге")
        b=d
        d=c
        c=a+(b-a)*fibonachi(n-i)/fibonachi(n+2-i)
    print("[",c,",",d,"]")

print("c= ",c)
print("d= ",d)
print('точка минимума: x=',c)
print('количество шагов:',col_steps)
print()
#----------------





