import os
import pytest

file_path = os.path.abspath('base.txt')

@pytest.fixture(autouse=True)
def clean_text_file():
    with open(file_path, 'w'):
        pass