import random


random_puzzle = [0, 1, 2, 3, 4, 5, 6, 7]
file_content = ''
for i in range(50):
    random.shuffle(random_puzzle)
    for i in random_puzzle:
        file_content += str(i) + ' '
    file_content += '\n'

with open('random_puzzles.txt', 'w') as random_puzzles_file:
    random_puzzles_file.write(file_content)


