from bs4 import BeautifulSoup as BSoup
from data import logo
import time
import json


# logo
def print_logo():
	for _ in logo:
		if _ != '\n':
			print(_, end='')
		else:  # removing \n
			print(_, end='')
		time.sleep(0.00037)
	print()
# logo


# saving
def save_file(path: str, j_list: [json]):
	try:
		with open(path, 'w', encoding="utf-8") as f:  # open file for writing
			# write line  in for loop
			for _ in range(len(j_list)):
				f.write(str(j_list[_]) + '\n')
		f.close()  # close
	except IOError:  # print message and exit on IO error for save file
		print('Error acquired during save process. ', end='')
		exit1337('Exiting Voight-Kampff test')


# loading
def get_file(path: str) -> BSoup:
	try:
		with open(path) as q:
			qa = BSoup(q, 'lxml')  # converting file to BSoup
			q.close()  # close
			return qa  # return BSoup
	except IOError:  # error and return noting if file corrupted
		print("File error! ", end='')
		return


# exiting
def exit1337(string: str):
	print(string)  # print
	exit(1337)  # 1337
