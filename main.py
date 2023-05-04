import json
import os


def run_quiz(quiz: list[dict]):
    score = 0
    for q in quiz:
        print(q["question"])
        for variant, answer in q["options"].items():
            print(f"{variant}) {answer}")
        user_answer = input("Your answer: ")
        if user_answer == q["answer"]:
            score += 1
    return score

def read_quiz_from_json(filename: str) -> list[dict]:
    quiz = []
    with open(filename, 'r') as f:
        quiz = json.load(f)
    return quiz

def save_results_to_json(filename: str, quiz_result: dict):
    quiz_results = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                quiz_results = json.load(f) or []
            except json.decoder.JSONDecodeError:
                pass
    quiz_results.append(quiz_result)
    with open(filename, 'w') as f:
        json.dump(quiz_results, f, indent=2)

quiz = read_quiz_from_json("quiz.json")
score = run_quiz(quiz)
first_name = input("Enter your name: ")
save_results_to_json("results.json", {"first_name": first_name, "score": score})
print(f"Your score is {score}")