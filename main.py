from data import question_data
from question_format import Question


class Test:
	def __init__(self):
		self.questions = self.generate_questions(question_data)
		self.user_score = 0
		self.questions_count = 0


	def generate_questions(self, data):
		questions = []
		for item in data:
			questions.append(Question(item["text"], item["answer"]))
		return questions


	def check_answer(self, question, users_answer):
			self.questions_count += 1
			if question.answer.lower() == users_answer.lower():
				self.user_score += 1
				return True
			else:
				return False


	def pass_fail(self):
		if self.questions_count == len(self.questions):
			print("Finish!")
			if self.user_score < len(self.questions) / 2:
				print("You fail!")
			else:
				print("You pass!")


	def test_user(self):
		for i in range(0, len(self.questions)):
			print(self.questions[i].question)
			result = self.check_answer(self.questions[i], input("Answer: "))
			print(result)
			print(f"Score: {self.user_score}/{self.questions_count}\n\n")
			self.pass_fail()





obj1 = Test()
obj1.test_user()

