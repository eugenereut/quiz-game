import json
from question_model import Question
from quiz_brain import QuizBrain
import requests

trivia_data = json.loads(
    requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean").text
)["results"]


question_bank = []

for qa in trivia_data:
    question_bank.append(
        Question(
            category=qa["category"],
            question=qa["question"].replace("&quot;", "`"),
            answer=qa["correct_answer"])
    )

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
