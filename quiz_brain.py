class QuizzBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        answer = input(f"Q.{self.question_num}: {question.text} (True/False): ").capitalize()
        if answer == "Stop":
            self.question_num = len(self.question_list)
        elif answer == question.answer:
            self.score += 1
            print(f"Your answer is correct! Your score is {self.score}/{self.question_num}")
        else:
            print(f"Your answer is incorrect! Your score is {self.score}/{self.question_num}")
