import os

def read_file(file_name):
    file_path = os.getcwd()
    with open(f'{file_path}\\{file_name}') as f:
        content = f.read()
    return content


def count_line(file_name):
    file_path = os.getcwd()
    with open(f'{file_path}\\{file_name}') as f:
        content = f.readlines()
    return len(content)


statistics = []
statistics.append((read_file('1.txt'), count_line('1.txt'), '1.txt'))
statistics.append((read_file('2.txt'), count_line('2.txt'), '2.txt'))
statistics.append((read_file('3.txt'), count_line('3.txt'), '3.txt'))

statistics.sort(key=lambda el: el[1])

with open('4.txt', 'a') as file:
    for i in range(len(statistics)):
        file.write(f'{statistics[i][2]}\n')
        file.write(f'{str(statistics[i][1])}\n')
        file.write(f'{statistics[i][0]}\n')
