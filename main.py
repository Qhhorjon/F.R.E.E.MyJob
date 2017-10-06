from colorama import init
init()

version = 'v1.5'
earnings_hour = 'NO_DATA'
earnings_month = 'NO_DATA'
dollar_rate = 'NO_DATA'
earnings_grn = 'NO_DATA'
earhour_grn = 'NO_DATA'

probel = '''
'''

def scanOS():
	if sys.platform == 'win32':
		pass
	else:
		print('ошибка: данная операционная система не поддерживается')
		input('Нажмите Enter')
		sys.exit()
def dataLook(earnings_hour,earnings_month,dollar_rate):
	earnings_month = int(earnings_month)
	earnings_hour = int(earnings_hour)
	earnings_grn = earnings_month * dollar_rate
	earhour_grn = int(earnings_hour) * dollar_rate

	time.sleep(0.05)
	print('ЗАРАБОТАНО     : '+'\x1b[32m{0} $ ({1} грн)\x1b[0m'.format(earnings_month,earnings_grn))
	time.sleep(0.05)
	print('ЗАРПЛАТА В ЧАС : '+'\x1b[32m{0} $ ({1} грн)\x1b[0m'.format(earnings_hour,earhour_grn))
	time.sleep(0.05)
	print('ТЕКУЩИЙ КУРС   : '+'\x1b[32m{0} $\x1b[0m'.format(dollar_rate))
def commandsHelp():
	print('/addea   - \x1b[32mВнести часы работы\x1b[0m')
	time.sleep(0.05)
	print('/edrate  - \x1b[0mИзменить курс\x1b[0m')
	time.sleep(0.05)
	print('/edhour  - \x1b[0mИзменить часовой заработок\x1b[0m')
	time.sleep(0.05)
	print('/wdaa    - \x1b[0mСнять счет\x1b[0m')
	time.sleep(0.05)
	print('/ersdata - \x1b[31mСтереть данные\x1b[0m')
	time.sleep(0.05)
	print('/erslog  - \x1b[33mОчистить лог\x1b[0m')
	time.sleep(0.05)
	print('/log     - \x1b[0mПросмотреть лог\x1b[0m')
	time.sleep(0.05)

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
	scanOS()
	os.system('cls')

	while True:
		run = True
		while run: #  Получение заработанных денег
			f = open('data\\earnmonth.freedata') # если не указан режим, по умолчанию подразумевается
			# режим чтения ('r'eading)
			while run:
				line = f.readline()
				if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
					run = False
				earnings_month = int(line)
				run = False
		run = True
		while run: #  Получение часового заработка
			f = open('data\\earnhour.freedata') # если не указан режим, по умолчанию подразумевается
			# режим чтения ('r'eading)
			while run:
				line = f.readline()
				if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
					run = False
				earnings_hour = int(line)
				run = False
		run = True
		while run: #  Получение курса доллара
			f = open('data\\dollar_rate.freedata') # если не указан режим, по умолчанию подразумевается
			# режим чтения ('r'eading)
			while run:
				line = f.readline()
				if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
					run = False
				dollar_rate = int(line)
				run = False
		
		if earnings_hour <= 0:
			print('F.R:E.E.MyJob',version)
			print('Ваш часовой заработок не указан.')
			print('Пожалуйста, укажите Ваш часовой заработок в долларовом эквиваленте.')
		
			while True:
				try:
					earnings_hour = input('Укажите целое число: ')
					if int(earnings_hour) > 0:
						add = time.strftime('%d.%m.%Y %H:%M Added {0} hourly earnings'.format(earnings_hour))
						f = open("data\\earnhour.freedata", "w")
						f.write(earnings_hour)
						f.close()
						print('\x1b[32m',end='')
						f = open("earnings.log", "a")
						f.write(add)
						f.write(probel)
						f.close()
						print('Часовой заработок успешно указан')
						time.sleep(1)
						os.system('cls')
						print('\x1b[0m')
						#os.system('cls')
					elif int(earnings_hour) <= 0:
						print('\x1b[31m'+'Вы указали число 0 или меньше.'+'\x1b[0m')
						print('\x1b[31m'+'Пожалуйста, укажите число больше 0'+'\x1b[0m')
					break
				except ValueError as exception:
					print('\x1b[31m'+'Вы указали число неправильного формата или текст.'+'\x1b[0m')
					print('\x1b[31m'+'Пожалуйста, укажите ЦЕЛОЕ ЧИСЛО без пробелов и текста'+'\x1b[0m')
		if dollar_rate <= 0:
			print('F.R:E.E.MyJob',version)
			print('Курс доллара не указан.')
			print('Пожалуйста, укажите текущий курс доллара в гривнах.')
		
			while True:
				try:
					dollar_rate = input('Укажите целое число: ')
					if int(dollar_rate) > 0:
						add = time.strftime('%d.%m.%Y %H:%M Added {0} dollar rate'.format(dollar_rate))
						f = open("data\\dollar_rate.freedata", "w")
						f.write(dollar_rate)
						f.close()
						print('\x1b[32m',end='')
						f = open("earnings.log", "a")
						f.write(add)
						f.write(probel)
						f.close()
						print('Курс доллара успешно указан')
						time.sleep(1)
						os.system('cls')
						print('\x1b[0m')
						#os.system('cls')
					elif int(dollar_rate) <= 0:
						print('\x1b[31m'+'Вы указали число 0 или меньше.'+'\x1b[0m')
						print('\x1b[31m'+'Пожалуйста, укажите число больше 0'+'\x1b[0m')
					break
				except ValueError as exception:
					print('\x1b[31m'+'Вы указали число неправильного формата или текст.'+'\x1b[0m')
					print('\x1b[31m'+'Пожалуйста, укажите ЦЕЛОЕ ЧИСЛО без пробелов и текста'+'\x1b[0m')

		os.system('cls')
		print('F.R:E.E.MyJob',version)
		dataLook(earnings_hour,earnings_month,dollar_rate)
		print()
		commandsHelp()
		print()
		command = input('/')
		if command == 'addea':
			try:
				print('Введите количество отработанных вами сегодня часов')
				print('Нажмите Enter не вводя ничего, чтобы отменить')
				while True:
					hoursJob = input('Отработано: ')
					hoursJob = int(hoursJob)
					if hoursJob == '':
						break
					if hoursJob <= 24:
						if hoursJob <= 0:
							print('\x1b[31mВы ввели число меньше 1\x1b[0m')
							print('\x1b[31mПожалуйста, введите нужное число\x1b[0m')
						else:
							earnings_month = hoursJob * earnings_hour + earnings_month
							add = time.strftime('%d.%m.%Y %H:%M Added {0} hours of job ({1}$)'.format(hoursJob,hoursJob*earnings_hour))
							f = open("data\\earnmonth.freedata", "w")
							f.write(str(earnings_month))
							f.close()
							f = open("earnings.log", "a")
							f.write(add)
							f.write(probel)
							f.close()
							print('\x1b[32mУспешно засчитано\x1b[0m')
							time.sleep(1)
							break
					if hoursJob > 24:
						print('\x1b[31mВы ввели число больше 24\x1b[0m')
						print('\x1b[31mПожалуйста, введите нужное число\x1b[0m')

			except ValueError as exception:
				print('\x1b[31m'+'Вы указали число неправильного формата или текст.'+'\x1b[0m')
				print('\x1b[31m'+'Пожалуйста, укажите ЦЕЛОЕ ЧИСЛО без пробелов и текста'+'\x1b[0m')
		if command == 'edrate':
			print('Введите новый курс доллара (в гривнах)')
			print('Нажмите Enter не вводя ничего, чтобы отменить')
			try:
				while True:
					new_rate = input('Текущий курс: ')
					new_rate = int(new_rate)
					if new_rate == '':
						break
					if new_rate <= 0:
						print('\x1b[31mВы ввели число меньше 1\x1b[0m')
						print('\x1b[31mПожалуйста, введите нужное число\x1b[0m')
					else:
						dollar_rate = new_rate
						add = time.strftime('%d.%m.%Y %H:%M Dollar rate has been changed to {0} $'.format(dollar_rate))
						f = open("data\\dollar_rate.freedata", "w")
						f.write(str(dollar_rate))
						f.close()
						f = open("earnings.log", "a")
						f.write(add)
						f.write(probel)
						f.close()
						print('\x1b[32mУспешно применено\x1b[0m')
						time.sleep(1)
						break
			except ValueError as exception:
				print('\x1b[31m'+'Вы указали число неправильного формата или текст.'+'\x1b[0m')
				print('\x1b[31m'+'Пожалуйста, укажите ЦЕЛОЕ ЧИСЛО без пробелов и текста'+'\x1b[0m')
		if command == 'edhour':
			print('Введите новый часовой заработок (в долларах)')
			print('Нажмите Enter не вводя ничего, чтобы отменить')
			try:
				while True:
					new_hourea = input('Текущий заработок: ')
					new_hourea = int(new_hourea)
					if new_hourea == '':
						break
					if new_hourea <= 0:
						print('\x1b[31mВы ввели число меньше 1\x1b[0m')
						print('\x1b[31mПожалуйста, введите нужное число\x1b[0m')
					else:
						earnings_hour = new_hourea
						add = time.strftime('%d.%m.%Y %H:%M Hour earnings changed to {0} $'.format(earnings_hour))
						f = open("data\\earnhour.freedata", "w")
						f.write(str(earnings_hour))
						f.close()
						f = open("earnings.log", "a")
						f.write(add)
						f.write(probel)
						f.close()
						print('\x1b[32mУспешно применено\x1b[0m')
						time.sleep(1)
						break
			except ValueError as exception:
				print('\x1b[31m'+'Вы указали число неправильного формата или текст.'+'\x1b[0m')
				print('\x1b[31m'+'Пожалуйста, укажите ЦЕЛОЕ ЧИСЛО без пробелов и текста'+'\x1b[0m')
		if command == 'wdaa':
			print('Вы уверены?')
			print('При снятии счета будет считатся, что вам оплатили деньги')
			print('При этом заработанный вами за месяц счет будет обнулятся')
			#print('Каждый месяц эта операция будет проводится автоматически')
			print('Оставьте поле пустым и нажмите Enter, чтобы отменить')
			print('Введите ЛЮБОЕ значение, чтобы подтвердить')
			choice = input('/')
			if choice == '':
				pass
			else:
				add = time.strftime('%d.%m.%Y %H:%M Earnings month cleared')
				f = open("data\\earnmonth.freedata", "w")
				f.write('0')
				f.close()
				f = open("earnings.log", "a")
				f.write(add)
				f.write(probel)
				f.write('                 Cause: user cleared it')
				f.write(probel)
				f.close()

				print('\x1b[32mУспешно применено\x1b[0m')
				time.sleep(1)
		if command == 'ersdata':
			print('Вы уверены?')
			print('Все ваши данные кроме лога будут удалены.')
			print('Оставьте поле пустым и нажмите Enter, чтобы отменить')
			print('Введите ЛЮБОЕ значение, чтобы подтвердить')
			choice = input('/')
			if choice == '':
				pass
			else:
				f = open("data\\earnmonth.freedata", "w")
				f.write('0')
				f.close()
				f = open("data\\earnhour.freedata", "w")
				f.write('0')
				f.close()
				f = open("data\\dollar_rate.freedata", "w")
				f.write('0')
				f.close()
				f = open("earnings.log", "a")
				f.write(time.strftime('%d.%m.%Y %H:%M Data erased'))
				f.write(probel)
				f.write('                 Cause: user erased it')
				f.write(probel)
				f.close()
				print('\x1b[32mУспешно применено\x1b[0m')
				time.sleep(1)
		if command == 'erslog':
			print('Вы уверены?')
			print('Ваши текущие данные НЕ будут стерты, но история - да')
			print('Оставьте поле пустым и нажмите Enter, чтобы отменить')
			print('Введите ЛЮБОЕ значение, чтобы подтвердить')
			choice = input('/')
			if choice == '':
				pass
			else:
				f = open("earnings.log", "w")
				f.write('')
				f.close()
				print('\x1b[32mУспешно применено\x1b[0m')
				time.sleep(1)
		if command == 'log':
			os.system('cls')
			print('F.R:E.E.MyJob',version)
			print('L O G')
			print()
			f = open('earnings.log') # если не указан режим, по умолчанию подразумевается
						# режим чтения ('r'eading)
			while True:
				line = f.readline()
				if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
					break
				print(line, end='')
				time.sleep(0.025)
			f.close() # закрываем файл
			print()
			input('Нажмите Enter')

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
	print()
	print('Скорее всего, эта ошибка вызвана повреждением данных.')
	print('Мы попробуем ее исправить, вернув данные к стандартным значениям')
	input('Нажмите Enter')
	f = open("data\\earnmonth.freedata", "w")
	f.write('0')
	f.close()
	f = open("data\\earnhour.freedata", "w")
	f.write('0')
	f.close()
	f = open("data\\dollar_rate.freedata", "w")
	f.write('0')
	f.close()
	f = open("earnings.log", "a")
	f.write(time.strftime('%d.%m.%Y %H:%M Data erased'))
	f.write(probel)
	f.write('                 Cause: the data was corrupted')
	f.write(probel)
	f.close()
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
