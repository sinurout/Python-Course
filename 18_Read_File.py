f = open("18text.txt")
data=f.read()
print(data)
f.close()


f = open("Another.txt","w")
f.write("i am smart")
f.close()