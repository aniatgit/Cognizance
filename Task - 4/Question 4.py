variable = int(input("Number:"))
temporary = variable
reverse = 0
while variable > 0:
    dig = variable % 10
    reverse = reverse * 10 + dig
    variable = variable // 10
if temporary == reverse:
    print("True")
else:
    print("False")