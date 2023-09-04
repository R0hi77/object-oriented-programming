from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question()
    new_question.text = question_text
    new_question.answer = question_answer
    question_bank.append(new_question)

start = QuizBrain()
start.question_list = question_bank
start.next_question()

