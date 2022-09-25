class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len( self.question_list ):
            return True
        else:
            return False

    def next_question(self):
        questions = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {questions.text} (Ture/False)?: ")
        self.check_answer(user_answer, questions.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right answer :)")
        else:
            print("Wrong answer!")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")
























































# class QuizBrain:
#
#     def __init__(self, ques_list):
#         self.question_num = 0
#         self.question_list = ques_list
#
#
#
#     def next_question(self):
#         question = self.question_list[self.question_num]
#         print(question.text)
#         # print(f"Q.{self.question_num}: {self.question.text} (True/False): ")
#         # print(question.text)
