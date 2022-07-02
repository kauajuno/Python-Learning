class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\n")
        if self.check_answer(user_answer, current_question.answer):
            self.score += 1
            print(f"Correct! The right answer is {current_question.answer}\nScore: {self.score}/{self.question_number}")
            return
        print(f"Incorrect! The right answer is {current_question.answer}\nScore: {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer
