import os
import sys
sys.path.append('D:\\coding\\pytest\\funcs')
import file_worker
import pytest

file_path = os.path.abspath('base.txt')

def create_test_data(test_data):
    with open(file_path, 'a') as f:
        f.writelines(test_data)

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data) 
    assert test_data == file_worker.file_worker(file_path)


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_test_data(test_data) 
    assert test_data == file_worker.file_worker(file_path)

