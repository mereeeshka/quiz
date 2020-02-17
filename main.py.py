class Quiestion():
    def __init__(self, ques_name, answer_list, right_answer):
        self.question = ques_name
        self.answers = answer_list
        self.right_answer = right_answer
        if right_answer not in answer_list:
            print('Right answer not in answers list!')

    self.question
    self.answers = []
    self.right_answer


class Quiz():
    def __init__(self, title):
        self.title = title

    self.title
    self.questions = []

    def add_question(self, ques_name, answer_list, right_answer):
        new_ques = Quiestion(ques_name, answer_list, right_answer)
        self.questions.append(new_ques)




q1 = Quiz('Любимый Виктор')
print(q1.title)
q1.add_question('Кто из них Тима?', ['Андрей', "Иван", "Ал-еша"], "Ал-еша")
q2.add_question("...?", ['..', '///'], '..')
print()

