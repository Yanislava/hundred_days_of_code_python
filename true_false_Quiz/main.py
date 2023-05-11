from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_dict in question_data:
    question = Question(q_dict['question'], q_dict['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f'You have completed the quiz.'
      f'Your final score was: {quiz.score}/{quiz.question_number}')
