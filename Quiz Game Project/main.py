from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question_list in question_data:

    # question_obj = Question(question_list["text"], question_list["answer"])
    question_obj = Question(question_list["question"], question_list["correct_answer"])
    question_bank.append(question_obj)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():

    quiz_brain.next_question()

print("Congratulations! You've completed the Quiz")
print(f"Your Final Score is: {quiz_brain.score}/{quiz_brain.question_number}")






























































# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
#
# question_bank = []
# for question_list in question_data:
#     text = question_list['text']
#     answer = question_list['answer']
#     new_question = Question(text, answer)
#     question_bank.append(new_question)
#
# quiz_brain_data = QuizBrain(question_bank)
#
# quiz_brain_data.next_question()
# # print(ques_list)
