from requests import get
from random import shuffle

total_question = int(input("Enter total questions: "))
print("*****Choose Catagory*****")
print()
while True:
    print("Computer = 18\nMathematics = 19\nMovies = 11\nSports = 21")
    catagory = int(input("Your Prefered Catagory (18/19/11/21): "))
    if catagory not in [18,19,11,21]:
        print("Please enter valid input")
        continue
    break

diffulty = input("Difficulty = (easy/medim/hard): ")

url = f"https://opentdb.com/api.php?amount={total_question}&category={catagory}&difficulty={diffulty.lower()}&type=multiple"
re = get(url)

contents = re.json()
questions = contents["results"]
score = 0

for question in questions:

    print(question["question"])
    options = []
    options.append(question["correct_answer"])

    for i in question["incorrect_answers"]:
        options.append(i)

    shuffle(options)
    
    for option in options:
        print(option)

    ans = input("Answer (Write exact words) = ")
    if ans == question["correct_answer"]:
        score += 1
        print("BINGOO.. You're correct")
    else:
        print("Wrong Answer\nIts",question["correct_answer"])
    print()

print(f"Your Score is {score}")