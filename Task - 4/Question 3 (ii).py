a = input("Add Roll Number ")
b = input('Add a Name ')
c = input('Enter Marks ')
d = input("Add Roll Number ")
e = input('Add a Name ')
f = input('Enter Marks ')
g = input("Add Roll Number ")
h = input('Add a Name ')
i = input('Enter Marks ')
print('[Roll no, Name, Marks]')
matrix =[
    [a, b, c],
    [d, e, f],
    [g ,h ,i]
]
s = input('Put the roll number of the student you want to find marks of')
if s == a:
    print(matrix[0])
elif s == d:
    print(matrix[1])
elif s ==g:
    print(matrix[2])
else:
    print('There is no roll number in the records')

