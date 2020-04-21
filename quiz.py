from Question import Question

question_prompt = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
]

questions = [
    Question(question_prompt[0], 'a'),
    Question(question_prompt[1], 'c'),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + 'correct')

run_quiz(questions)

