print("Введите значения a,b,c,d,f")
print("Введите a")
a = float(input())
print("Введите b")
b=float(input())
print("Введите c")
c=float(input())
print("Введите d")
d=float(input())
print("Введите f")
f=float(input())
if b==0 or a==0:
    print("Ошибка, неверно введены данные")
else:
    k=abs((a-b*c*d**3+(c**5-a**2)/a+f**3*(a-213)))
    print("k=", k)

