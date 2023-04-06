from core import get_qa_dict, get_measurments, empathy_append
from utils import exit1337, get_file, save_file, print_logo
from random import shuffle, randint
from data import m_list, j_list
from statistics import mean
import argparse


# Voight-Kampf test
def voight_kampff(s: str):
	# finding mean respiration, heart rate, blushing level and pupillary dilation
	m_resp = int(mean(m_list['respiration']))
	m_h_r = int(mean(m_list['heart_rate']))
	m_b_l = int(mean(m_list['blushing_lvl']))
	m_p_d = int(mean(m_list['pup_dilation']))

	# append human or replicant on json, saving results to file and and exit
	if 12 <= m_resp <= 16 and 60 <= m_h_r <= 100 and 2 <= m_b_l <= 4 and 2 <= m_p_d <= 8:
		print('HUMAN')
		empathy_append(j_list, "HUMAN")
		save_file(s, j_list)
		exit1337('Exiting Voight-Kampff test')
	else:
		print('!REPLICANT!')
		empathy_append(j_list, "!REPLICANT!")
		save_file(s, j_list)
		exit1337('Exiting Voight-Kampff test')


# empathy test
def empathy_test(qa, s):
	print('Starting Voight-Kampff test...')
	qa_xml = get_file(qa)  # getting qa file as BSoup
	qa_dict = None  # define qa dictionary
	if qa_xml:
		qa_dict = get_qa_dict(qa_xml)  # parsing
	else:
		exit1337('Exiting Voight-Kampff test')  # exit on file error

	questions = list(qa_dict.keys())  # creating list of questions
	shuffle(questions)  # shuffle
	q_count = 0  # questions counter
	print('---------------')
	for q in questions:  # starting survey
		q_count += 1
		a = qa_dict[q][randint(0, len(qa_dict[q]) - 1)]  # processing answers and getting measurments
		print('Question #', q_count, ':', q, '\n', 'Answer: ', a, '\nMeasurements:')
		get_measurments(q, a)
		print('---------------')
		if q_count == 10:  # stop test on 10 question
			break
	voight_kampff(s)  # voight-kampff process with output file path


# script start part
if __name__ == '__main__':
	# python3 main.py -qa questions2.xml -s answers.json
	pars = argparse.ArgumentParser()  # creating argument parser
	pars.add_argument('-qa', type=str, default='questions.xml', help='Set Q&A xml file')  # adding -qa argument for custom qa dictionaries
	pars.add_argument('-s', type=str, default='results.json')  # same procedure to select result file on -s argument
	# parse arguments and appending to save and qa file values
	args = pars.parse_args()
	file = args.qa
	save = args.s
	try:
		print_logo()  # printin logo
		empathy_test(file, save)  # Sending paths to Voight-Kampff Empathy Test
	except KeyboardInterrupt:  # Exit on keyboard interrupt
		exit1337('\nStopping Voight-Kampff test.')
