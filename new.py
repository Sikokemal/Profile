sec=int(input("Секунд енгізіңіз:  "))
min=sec//60
sec1=sec%60 
hour=min//60
print(f"{sec} секунд = {hour} сағат {min%60} минут {sec1} секунд")

print("Екінші тапсырма калкулатор") 
a=int(input("Бірінші санды енгізіңіз:  ")       )
b=int(input("Екінші санды енгізіңіз:  "))
c=input("Операцияны енгізіңіз (+,-,*,/):  ")
match c:
    case "+":           
        print(f"{a}+{b}="+str(a+b))
    case "-":
        print(f"{a}-{b}="+str(a-b))
    case "*":
        print(f"{a}*{b}="+str(a*b))
    case "/":
        if b!=0:
            print(f"{a}/{b}="+str(a/b))
        else:
            print("На ноль делить нельзя")