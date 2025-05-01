# Imported libraries
import random
import tkinter as tk

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

base = tk.Tk()
base.title("Quiz_taker")

# The texts in these labels will be configurated later
question_label = tk.Label(base, text = "Hello I am a question", wraplength = 800, font = ("Arial", 10))
question_label.pack(pady = 15)

option_a = tk.Label(base, text = "Hello I am a choice", wraplength = 800, font = ("Arial", 8))
option_a.pack(pady = 10)

option_b = tk.Label(base, text = "Hello I am a choice", wraplength = 800, font = ("Arial", 8))
option_b.pack(pady = 10)

option_c = tk.Label(base, text = "Hello I am a choice", wraplength = 800, font = ("Arial", 8))
option_c.pack(pady = 10)

option_d = tk.Label(base, text = "Hello I am a choice", wraplength = 800, font = ("Arial", 8))
option_d.pack(pady = 10)

# Exit Button
tk.Button(base, text = "Exit", command = base.quit).pack(pady = 10)

base.mainloop()


def raw_code():
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
 
 