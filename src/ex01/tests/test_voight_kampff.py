from src.ex01.utils import print_logo, save_file, get_file, exit1337
from src.ex01.data import m_list, j_list, logo
from src.ex01.core import health_check, empathy_append, get_qa_dict, get_measurments
from src.ex01.main import voight_kampff, empathy_test
import pytest


def test_voight_kampff():
	assert get_file('./bad_q_file.xml') == 'File error! '
