# Imported libraries
import random

# Read the quiz questions file
with open("quiz_questions.txt", "r") as quiz_file:
    reader = quiz_file.readlines()
    
quiz_length = len(reader)  // 7

# Do not repeat the questions and end it when it's done
quiz_order = []
question_start = 0

score = 0

for i in range(quiz_length):
    quiz_order.append(question_start)
    question_start += 7
    
 
# Randomly pick a question from the file
random.shuffle(quiz_order)

#Ask the questions
for asking in quiz_order:
    print(reader[asking])
    print(reader[asking + 1])
    print(reader[asking + 2])
    print(reader[asking + 3])
    print(reader[asking + 4])
    
    correct_answer = reader[asking + 5].split(":")[1].strip()
    
    answer = input("What is your answer? \n(A/B/C/D): ")
    
    if answer == correct_answer:
        score += 1
        print("Correct!")
        
    else:
        print("Wrong")
    
# Add points when answers are correct and show it in the end
print(f"You scored {score} out of {quiz_length}")

# Do all this in tkinter
 