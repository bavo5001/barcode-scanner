import os
import tempfile
import time
from datetime import datetime as dt


def print_harnesses_name(x):
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(x)
    os.startfile(filename, 'print')


z = int(input("Введіть к-ть лейб для видруку, 3 шт. макс.: "))

if 0 < z < 4:
    while(True):
        print('Зіскануйте кабельну мережу:')
        name_harness: str = input()
        now = dt.now()
        for x in range(0, z):
            print_harnesses_name((f'КМ:{name_harness}\n') + (f"{now:%d.%m.%Y %H:%M}"))

else:
    print("Вказана к-ть лейб для друку перевищена!!!")
    time.sleep(5)
