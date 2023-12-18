from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    qi = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(qi)


brain = QuizBrain(question_bank)

while brain.q_number < len(brain.list):
    answer = brain.new_question()
    brain.check_answer(answer)

print(f""" You've completed the quiz
your final score is {brain.score}/{brain.q_number}""")