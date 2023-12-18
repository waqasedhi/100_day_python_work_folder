class QuizBrain:

    def __init__(self, q_list):
        self.list = q_list
        self.q_number = 0
        self.score = 0

    def new_question(self):
        self.q_number += 1
        answer = input(f"q{self.q_number}: {self.list[self.q_number - 1].text} (True / False): ").title()
        return answer

    def check_answer(self, p_answer):
        answer = p_answer
        if answer == "True" or answer == "False":
            if answer == self.list[self.q_number - 1].answer.title():
                print("you are right.")
                self.score += 1
            else:
                print("your answer is wrong.")
            print(f"correct answer was:{self.list[self.q_number - 1].answer}")
            print(f"Your current score is {self.score}/{self.q_number}\n")
        else:
            print("Plz enter valid Input\n")
            self.q_number -= 1

