1//
def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'your_file.txt' 
file_content = read_entire_file(file_path)
print(file_content)
2//
def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = [next(file) for _ in range(n)]
    return lines

file_path = 'your_file.txt'
n = 7 
first_n_lines = read_first_n_lines(file_path, n)
for line in first_n_lines:
    print(line, end='')
  3//
def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines[-n:]

file_path = 'your_file.txt'
n = 9
last_n_lines = read_last_n_lines(file_path, n)
for line in last_n_lines:
    print(line, end='')
4//
def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
    return len(words)

file_path = 'your_file.txt'
word_count = count_words(file_path)
print("Number of words:", word_count)
5//
def read_last_n_lines_bonus(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines[-n:]

file_path = 'your_file.txt'
n = 4
last_n_lines = read_last_n_lines_bonus(file_path, n)
for line in last_n_lines:
    print(line, end='')
