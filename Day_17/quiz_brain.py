class QuizBrain:
    """I own the quiz"""
    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self) -> None:
        """Get the next question from the list"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f'Q.{self.question_number}: {current_question.question_text} (True/False)?: ')
        self.check_answer(guess, current_question.question_answer)

    def questions_remaining(self) -> None:
        """Check if there are questions remainings"""
        if self.question_number >= len(self.question_list):
            return False
        return True

    def check_answer(self, guess, answer):
        """Check if the users input was correct"""
        if guess.lower() == answer.lower():
            print("You are correct")
            self.score += 1
        else:
            print("Incorrect")
        print("The correct answer was:", answer)
        print(f"Your current score is {self.score}/{self.question_number}")
        print()




