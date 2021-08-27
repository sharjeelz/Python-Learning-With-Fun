class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("Correct")
        else:
            print("wrong")
        print(f"Your answered {correct_answer} , {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q: {self.question_number} {current_question.text}Ture/False ?")
        if self.check_answer(user_answer, current_question.answer):
            self.score += 1
