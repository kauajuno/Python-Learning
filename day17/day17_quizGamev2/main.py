from random import shuffle
from db import database
from question import Question
from quizbrain import QuizBrain

question_bank = []

for q in database:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

shuffle(question_bank)
manage = QuizBrain(question_bank)

while manage.still_has_questions():
    manage.next_question()
