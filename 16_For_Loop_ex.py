#Ex= 1
num = int(input("enter a number: "))
i=1
while i <11:
    print(f"{num}X{i}={num*i}")
    i=i+1
#Ex= 2
name = ["nihar","nehu","biswa","tilu"]
for n in name:
    if n.startswith("n"):
        print("hello"+ n)
    