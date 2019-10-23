import top_5_words_in_a_file as top5

import pytest
from os import path

@pytest.fixture(name="simple_test_data")
def simple_test_data_file_provider():
    file_path = path.join(path.dirname(__file__), 'test_data.txt')
    return file_path

def test_parsing_file_contents(simple_test_data):
    word_dict = top5._parsing_file_contents(simple_test_data)
    assert word_dict
    for key, value in word_dict.items():
        print(key, value)

