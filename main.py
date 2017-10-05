from colorama import init
init()

version = 'v1.0'

def scan():
	if sys.platform == 'win32':
		pass
	else:
		print('ошибка: данная операционная система не поддерживается')
		input('Нажмите Enter')
		sys.exit()
try:
	print('Импорт стандартных библиотек...')
	print('Импорт sys.py...')
	import sys
	print('Импорт os.py...')
	import os
	print('Импорт time.py...')
	import time
	print('Импорт random.py...')
	import random
	print('Импорт subprocess.py...')
	import subprocess
	print('Импорт re.py...')
	import re

except StopIteration as exception:
	print('ОШИБКА:')
	print('StopIteration: в итераторе больше нет элементов')
	print(exception)
	input('Нажмите Enter')
except ArithmeticError as exception:
	print('ОШИБКА:')
	print('ArithmeticError: арифметическая ошибка')
	print(exception)
	input('Нажмите Enter')
except AssertionError as exception:
	print('ОШИБКА:')
	print('AssertionError: выражение в функции assert ложно')
	print(exception)
	input('Нажмите Enter')
except AttributeError as exception:
	print('ОШИБКА:')
	print('AttributeError: объект не имеет данного атрибута, значения или метода')
	print(exception)
	input('Нажмите Enter')
except BufferError as exception:
	print('ОШИБКА:')
	print('BufferError: операция, связанная с буфером, не можеть быть выполнена')
	print(exception)
	input('Нажмите Enter')
except EOFError as exception:
	print('ОШИБКА:')
	print('EOFError: функция наткнулась на конец файла и не смогла прочитать то, что хотела')
	print(exception)
	input('Нажмите Enter')
except ImportError as exception:
	print('ОШИБКА:')
	print('ImportError: не удалось импортирование модуля или его атрибута')
	print(exception)
	input('Нажмите Enter')
except LookupError as exception:
	print('ОШИБКА:')
	print('LookupError: некорректный индекс или ключ')
	print(exception)
	input('Нажмите Enter')
except MemoryError as exception:
	print('ОШИБКА:')
	print('MemoryError: недостаточно памяти')
	print(exception)
	input('Нажмите Enter')
except NameError as exception:
	print('ОШИБКА:')
	print('NameError: не найденно переменной с таким именем')
	print(exception)
	input('Нажмите Enter')
except UnboundLocalError as exception:
	print('ОШИБКА:')
	print('UnboundLocalError: сделана ссылка на локальную переменную в функции, но переменная не определена ранее')
	print(exception)
	input('Нажмите Enter')
except OSError as exception:
	print('ОШИБКА:')
	print('OSError: системная ошибка')
	print(exception)
	input('Нажмите Enter')
except ReferenceError as exception:
	print('ОШИБКА:')
	print('ReferenceError: попытка доступа к атрибуту со слабой ссылкой')
	print(exception)
	input('Нажмите Enter')
except RuntimeError as exception:
	print('ОШИБКА:')
	print('RuntimeError: неизвестная ошибка')
	print(exception)
	input('Нажмите Enter')
except NotImplementedError as exception:
	print('ОШИБКА:')
	print('NotImplementedError: абстрактные методы класса требуют переопределения в дочерних процессах')
	print(exception)
	input('Нажмите Enter')
except SyntaxError as exception:
	print('ОШИБКА:')
	print('SyntaxError: синтаксическая ошибка')
	print(exception)
	input('Нажмите Enter')
except IndentationError as exception:
	print('ОШИБКА:')
	print('IndentationError: неправильные отступы')
	print(exception)
	input('Нажмите Enter')
except TabError as exception:
	print('ОШИБКА:')
	print('TabError: смешивание в отступах табуляции и пробелов')
	print(exception)
	input('Нажмите Enter')
except SystemError as exception:
	print('ОШИБКА:')
	print('SystemError: внутренняя ошибка')
	print(exception)
	input('Нажмите Enter')
except TypeError as exception:
	print('ОШИБКА:')
	print('TypeError: операция применена к объекту несоответствующего типа')
	print(exception)
	input('Нажмите Enter')
except ValueError as exception:
	print('ОШИБКА:')
	print('ValueError: функция получила объект правильного типа, но некорректного значения')
	print(exception)
	input('Нажмите Enter')
except UnicodeError as exception:
	print('ОШИБКА:')
	print('UnicodeError: ошибка кодирования/раскодирования Юникода')
	print(exception)
	input('Нажмите Enter')
except Error as exception:
	print('ОШИБКА:')
	print(': ')
	print(exception)
	input('Нажмите Enter')