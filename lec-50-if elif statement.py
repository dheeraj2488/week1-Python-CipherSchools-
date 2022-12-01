age=int(input("ente your  age: "))
if age==0:
    print("you cant watch")
elif 0<age<=3:
    print("ticket price :free")
elif 3<age<=10:
    print("ticket price:150")
elif 10<age<=60:
    print("tiket price:250")
else:
    print("tiket price:200")             