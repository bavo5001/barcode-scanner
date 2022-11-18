import os
import tempfile
import time
from datetime import datetime as dt
import csv


def print_harnesses_name(x):
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(x)
    os.startfile(filename, 'print')


while(True):
    print('Зіскануйте кабельну мережу:')
    name_harness: str = input()
    now = dt.now()
    # open the file in the write mode
    with open('print_archive.csv', 'a', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow([name_harness]+[now.strftime("%d.%m.%Y %H:%M")])
    for x in range(0, 2):
        print_harnesses_name((f'КМ:{name_harness}\n') + (f"{now:%d.%m.%Y %H:%M}"))

