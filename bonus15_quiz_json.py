import json

with open("questions.json", "r") as questions_file:
    content = questions_file.read()



data = json.loads(content)
# print(type(content))
# print(type(data))


for question in data:
    print(question["question"])

    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, " - ", alternative)

    user_input = int(input("Enter your choice: "))
    question["user_choice"] = user_input

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer!"
    else:
        result = "Wrong Answer!"

    message = (f'{result} Your answer: {question["user_choice"]}, ' \
               f'Correct answer: {question["correct_answer"]}')
    print(message)

final_score = str(score/len(data)*100) + "%"
print(final_score)

# print(data)