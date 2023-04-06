class QuizBrain:
    def __init__(self,question_list:list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    
    def next_question(self):
        question =  self.question_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q: {self.question_number}. {question.text} (True/False)")
        self.check_answer(answer,question.answer)


    def check_answer(self, u_ans,cor_answer):
        if u_ans.lower() == cor_answer.lower():
            self.score +=1
            print(f"Correct, your score is {self.score}/{self.question_number}\n")
        else:
            print(f"Wrong,your score is {self.score}/{self.question_number}")
            print(f"Correct answer is {cor_answer}\n")


    def return_score(self):
        return f"{self.score}/{self.question_number}"
    

