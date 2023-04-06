from bs4 import BeautifulSoup as BSoup
from data import m_list, j_list, json
from utils import exit1337
import typing


# checking person's health status on measurments from input
def health_check(resp: int, h_r: int, b_l: int, p_d: int) -> bool:
	if 4 <= resp <= 80 and 20 <= h_r <= 220 and 1 <= b_l <= 6 and 1 <= p_d <= 12:
		return True
	else:
		return False


# append subject to object
def empathy_append(obj, subj):
	try:
		obj.append(subj)
	except Exception:
		exit1337('Append error!')


# function for qa dictionary creation
def get_qa_dict(qa: BSoup) -> typing.Dict:
	qa_dict: typing.Dict[str, list[str]] = {}
	try:
		q_len = len(qa.find_all('text'))
		for _ in range(q_len):
			tmp_ans = []
			# finding questions text and answers for empathy append
			tmp_text = qa.find('question', {'id': str(_)}).find('text').text
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer1').text)
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer2').text)
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer3').text)
			# trying fourth answer if it exists
			try:
				bonus_answer = qa.find('question', {'id': str(_)}).find('answer4').text
				empathy_append(tmp_ans, bonus_answer)
			except AttributeError:
				pass
			qa_dict[tmp_text] = tmp_ans  # assign tmp text key and tmp answers list in qa_dict
	except AttributeError:
		exit1337('Q&A file corrupted') 	# exit on error
		return
	return qa_dict  # return qa


# get measurments from person
def get_measurments(q: str, a: str):
	resp, h_r, b_l, p_d = 0, 0, 0, 0  # variables
	# try input for ints
	try:
		resp = int(input(' Respiration: '))
		h_r = int(input(' Heart rate: '))
		b_l = int(input(' Blushing level(1 - 6): '))
		p_d = int(input(' Pupillary dilation: '))
	except ValueError:
		exit1337('Expected numeric value')  # exit on error
	# check person's health, append new values to measurments list or exit on unreal values
	if health_check(resp, h_r, b_l, p_d):
		empathy_append(m_list['respiration'], resp)
		empathy_append(m_list['heart_rate'], h_r)
		empathy_append(m_list['blushing_lvl'], b_l)
		empathy_append(m_list['pup_dilation'], p_d)
	else:
		exit1337('This person should be dead or not human at all')
	# generating new message for json and append its dumped form to json list
	j_message = {"question": q, "answer": a, "respiration": resp, "heart_rate": h_r, "blushing_lvl": b_l, "pup_dilation": p_d}
	empathy_append(j_list, json.dumps(j_message))
