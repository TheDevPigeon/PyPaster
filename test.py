import os
file_name = 'nbrcours.txt'
os.path.exists(file_name)
with open(file_name, 'r') as file:
    nbrcours = int(file.read().strip())
    nbrcours += 1
with open(file_name, 'w') as file:
    file.write(str(nbrcours))


print(nbrcours)