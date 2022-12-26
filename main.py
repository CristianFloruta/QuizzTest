from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain
from random import shuffle


question_bank = []

for num in range(len(question_data)):
    question_num = Question(question_data[num]["text"], question_data[num]["answer"])
    question_bank.append(question_num)

shuffle(question_bank)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("congratulation! You finalized the quizz!")
print(f"Your final score is: {quizz.score}/{quizz.question_num}")

