"""
Quiz game!

The game should do the following:
1. Have a list of questions and answers
2. Take the users input as an answer to the question
3. Check if the user got the answer right
4. Calculate the score
5. Repeat unti:
    A: 5 questions have been answered
    B: They get a question wrong

Classes
    Quiz brain will hold all the questions

"""
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

quiz_master = QuizBrain(question_bank)

while quiz_master.questions_remaining():
    quiz_master.next_question()

print(f"Game over! You scored {quiz_master.score} out of {quiz_master.question_number}")
