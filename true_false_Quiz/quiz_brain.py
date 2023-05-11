class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}: {current_question.text} Is it true or false?')
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_question, correct_answer):
        if user_question.lower() == correct_answer.lower():
            self.score += 1
            print(f'You got it right!')
        else:
            print("That's wrong")
        print(f'The correct answer was: {correct_answer}.'
              f'Your current score is: {self.score}/{self.question_number}.\n')
