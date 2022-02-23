num = int(input("enter the number of columns:"))
for i in range(1, num + 1):
    print(" " * (num - i) + "* " * i)