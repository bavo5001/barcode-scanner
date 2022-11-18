import tempfile
import time
#import pywin32_bootstrap
import win32api
import win32print

#import sys
#sys.path.append('C:\\Users\\pavo5002\\AppData\\Local\\Programs\\Python\\Python311\\lib\\site-packages\\win32')
#sys.path.append('C:\\Users\\pavo5002\\AppData\\Local\\Programs\\Python\\Python311\\lib\\site-packages\\win32\\lib')

def print_harnesses_name(x):
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(x)
    win32api.ShellExecute(0, "print", filename, '"%s"' % win32print.GetDefaultPrinter(),".",0)
while (True):
    print('Зіскануйте кабельну мережу:')
    name_harness: str = input()
    current_time = time.asctime()
    print_harnesses_name(name_harness)
    print_harnesses_name(current_time)

