import random

def get_number(a, b):
    return random.randint(a, b)


data_a = int(input('Выбери диапазон, я загадаю число от '))
data_b = int(input(' до включительно, ну а тебе отгадывать...'))
print('У тя Пять попыток отгадать')

numberOK = False
number = get_number(data_a, data_b)
count_c = 1
while count_c <= 5:
    print('count_c : ', count_c)
    data_c = int(input('Вводи число из диапазона, попытайся отгпдать : '))
    if data_c > number:
        print('Попытка номер ', count_c)
        print('Перелет')
        count_c = count_c + 1
    elif data_c < number:
        print('Попытка номер ', count_c)
        print('Недолет')
        count_c = count_c + 1
    else:
        print('Красава, отгадал число с попытки номер ', count_c)
        numberOK = True
        exit()
if numberOK:
    print('Красавец, отгадал с попытки ', count_c, ' число ', number)
else:
    print('Тупеня, просрал все попытки... Число было :', number, ' POPITKA ', count_c)
