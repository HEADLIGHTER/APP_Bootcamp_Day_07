from core import get_qa_dict, get_measurments, empathy_append
from utils import exit1337, get_file, save_file, print_logo
from random import shuffle, randint
from data import m_list, j_list
from statistics import mean
import argparse
import markdown as marka
from python_markdown_comments import CommentsExtension


def voight_kampff(s: str):
	m_resp = int(mean(m_list['respiration']))
	m_h_r = int(mean(m_list['heart_rate']))
	m_b_l = int(mean(m_list['blushing_lvl']))
	m_p_d = int(mean(m_list['pup_dilation']))

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


def empathy_test(qa, s):
	qa_xml = get_file(qa)
	qa_dict = None
	if qa_xml:
		qa_dict = get_qa_dict(qa_xml)
	else:
		exit1337('Exiting Voight-Kampff test')

	questions = list(qa_dict.keys())
	shuffle(questions)
	q_count = 0
	print('---------------')
	for q in questions:
		q_count += 1
		a = qa_dict[q][randint(0, len(qa_dict[q]) - 1)]
		print('Question #', q_count, ':', q, '\n', 'Answer: ', a, '\nMeasurements:')
		get_measurments(q, a)
		print('---------------')
		if q_count == 10:
			break
	voight_kampff(s)


if __name__ == '__main__':
	pars = argparse.ArgumentParser()
	pars.add_argument('-qa', type=str, default='questions.xml', help='Set Q&A xml file')
	pars.add_argument('-s', type=str, default='results.json')
	args = pars.parse_args()
	file = args.qa
	save = args.s
	try:
		print_logo()
		empathy_test(file, save)
	except KeyboardInterrupt:
		exit1337('\nStopping Voight-Kampff test.')
