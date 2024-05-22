from functions_file import count_char, count_lines, count_words

def test_count_char():
    with open("File1.py") as text_1:
        assert count_char(text_1.read()) == 1028
    with open("File2.py") as text_2:
        assert count_char(text_2.read()) == 32

def test_count_lines():
    with open("File1.py") as text_1:
        assert count_lines(text_1.read()) == 1028
    with open("File2.py") as text_2:
        assert count_lines(text_2.read()) == 42

def test_count_lines():
    with open("File1.py") as text_1:
        assert count_words(text_1.read()) == 181
    with open("File2.py") as text_2:
        assert count_words(text_2.read()) == 253
