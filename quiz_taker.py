# Imported libraries
import random

# Read the quiz questions file
with open("quiz_questions.txt", "r") as quiz_file:
    reader = quiz_file.readlines()
    
quiz_length = len(reader)  // 7
print(quiz_length)

# Do not repeat the questions and end it when it's done
quiz_order = []
question_start = 0

for i in range(quiz_length):
    question_start += 7
    print(question_start)
    quiz_order.append(question_start)
 
# Randomly pick a question from the file
random.shuffle(quiz_order)

# Add points when answera are correct and show it in the end
# Do all this in tkinter
 