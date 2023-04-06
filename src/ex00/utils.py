from bs4 import BeautifulSoup as BSoup
from data import logo
import time
import json


def print_logo():
	for _ in logo:
		if _ != '\n':
			print(_, end='')
		else:
			print(_, end='')
		time.sleep(0.00037)
	print()


def save_file(path: str, j_list: [json]) -> bool:
	try:
		with open('results', 'w', encoding="utf-8") as f:
			for _ in range(len(j_list)):
				f.write(str(j_list[_]) + '\n')
		f.close()
		return True
	except IOError:
		print('Error acquired during save process. ', end='')
		exit1337('Exiting Voight-Kampff test')
		return False


def get_file(path: str):
	try:
		with open(path) as q:
			qa = BSoup(q, 'lxml')
			q.close()
			return qa
	except IOError:
		print("File error! ", end='')
		return


def exit1337(string):
	print(string)
	exit(1337)
