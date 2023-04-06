from bs4 import BeautifulSoup as BSoup
from data import m_list, j_list, json
from utils import exit1337
import typing


def health_check(resp, h_r, b_l, p_d) -> bool:
	if 4 <= resp <= 80 and 20 <= h_r <= 220 and 1 <= b_l <= 6 and 1 <= p_d <= 12:
		return True
	else:
		return False


def empathy_append(obj, subj):
	try:
		obj.append(subj)
	except Exception:
		exit1337('Append error!')


def get_qa_dict(qa: BSoup):
	qa_dict: typing.Dict[str, list[str]] = {}
	try:
		q_len = len(qa.find_all('text'))
		for _ in range(q_len):
			tmp_ans = []
			tmp_text = qa.find('question', {'id': str(_)}).find('text').text
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer1').text)
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer2').text)
			empathy_append(tmp_ans, qa.find('question', {'id': str(_)}).find('answer3').text)
			try:
				bonus_answer = qa.find('question', {'id': str(_)}).find('answer4').text
				empathy_append(tmp_ans, bonus_answer)
			except AttributeError:
				pass
			qa_dict[tmp_text] = tmp_ans
	except Exception:
		exit1337('Q&A file corrupted')
		return
	return qa_dict


def get_measurments(q: str, a: str):
	try:
		resp = int(input(' Respiration: '))
		h_r = int(input(' Heart rate: '))
		b_l = int(input(' Blushing level(1 - 6): '))
		p_d = int(input(' Pupillary dilation: '))
	except ValueError:
		exit1337('Expected numeric value')
	if health_check(resp, h_r, b_l, p_d):
		empathy_append(m_list['respiration'], resp)
		empathy_append(m_list['heart_rate'], h_r)
		empathy_append(m_list['blushing_lvl'], b_l)
		empathy_append(m_list['pup_dilation'], p_d)
	else:
		exit1337('This person should be dead or not human at all')
	j_message = {"question": q, "answer": a, "respiration": resp, "heart_rate": h_r, "blushing_lvl": b_l, "pup_dilation": p_d}
	empathy_append(j_list, json.dumps(j_message))
