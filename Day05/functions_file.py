#character counting function
def count_char(text):
    split_text = text.split()
    join_text = "".join(split_text)
    num_char = 0
    for char in join_text:
        num_char+=1
    return(num_char)

#line counting function
def count_lines(text):
    line_count = text.splitlines()
    return len(line_count)

#words counting function
def count_words(text):
    num_words = len(text.split())
    return(num_words)