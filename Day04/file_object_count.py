import sys

def count_file_stats(filename):
    with open(filename, 'r') as file:
        content = file.read()
        char_count = len(content)
        line_count = content.count('\n') + 1  
        word_count = len(content.split())

        print(f"Number of characters: {char_count}")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    else:
        filename = sys.argv[1]
        count_file_stats(filename)

main()