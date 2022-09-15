from FCCBAMCQQuestion import Question

question_prompts = [
    "What do you want to do?\n(a) Futbol\n(b) Mt.Everest\n(c) Sail\n\n",
    "Where do you want to live?\n(a) Santander\n(b) Madrid\n(c) Hong Kong\n\n",
    "What is your favorite color?\n(a) Orange\n(b) Yellow\n(c) Purple\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")


run_test(questions)
