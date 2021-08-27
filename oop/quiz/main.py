from data import question_data
from model import Question
from brain import Brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()



