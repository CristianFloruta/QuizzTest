from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain
from random import shuffle


question_bank = []

for num in range(len(question_data)):
    question_num = Question(question_data[num]["text"], question_data[num]["answer"])
    question_bank.append(question_num)

# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

shuffle(question_bank)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

