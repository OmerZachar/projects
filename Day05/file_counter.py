import sys
from functions_file import count_char, count_lines, count_words

def file_input():
    if len(sys.argv) !=2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
        filename = sys.argv[1]
        return filename

def main():
    filename = file_input(filename)
    with open(filename) as fn:
        text_file = fn.read()

        num_characters = count_char(text_file)
        print(f"The number of characters is: {num_characters}")

        num_lines = count_lines(text_file)
        print(f"nubmer of lines: {num_lines}")

        num_words = count_words(text_file)
        print(f"nubmer of words: {num_words}")
main()