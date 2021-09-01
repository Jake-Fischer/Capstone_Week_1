classes = []

class_name = input('Enter class name: ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class name. Enter to quit.')

print(classes)

for c in classes:
    print(c)

for index, c in enumerate(classes):
    print(index, c)

for index, c in enumerate(classes):
    print(f'{index+1}: {c}')