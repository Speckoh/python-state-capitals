import random
from capitals import states

player_input = ''
correct_score = 0
num_of_questions = 10

random.shuffle(states)

print('Welcome! Name the capital of each State!')

for state in states[0:num_of_questions]:
    player_input = input(f'What is the capital of {state["name"]}? ').lower()
    if player_input == state["capital"].lower():
        print("correct!")
        correct_score += 1
    else:
        print("wrong!")

print(f'You got {correct_score} / {num_of_questions} correct!')
