class QuizzBrain:

    # QuizzBrain is creating the game logic for question and answer game

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):

        # setting the stop for game running loop
        """
            if self.question_num < len(self.question_list):
                return True
            else:
                return False
        """
        return self.question_num < len(self.question_list)

    def next_question(self):

        # Ask and verify the answer for a question from the class list.

        question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {question.text} (True/False): ").capitalize()
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):

        """
        Count the questions asked.
        Break the game loop when 'Stop' is chosen

        :param user_answer: is the answer given by the user when next_question method is run,
        :param correct_answer: is the value of answer attribute of question object (question.answer) given by,
        :return: print the answer status  -> 'correct' or 'incorrect' as well as the score status
        """

        if user_answer == "Stop":
            self.question_num = len(self.question_list)
        elif user_answer == correct_answer:
            self.score += 1
            print(f"Your answer is correct! Your score is {self.score}/{self.question_num}")
            print("\n")
        else:
            print(f"Your answer is incorrect! Your score is {self.score}/{self.question_num}")
            print(f"The correct answer was: {correct_answer}. ")
            print("\n")