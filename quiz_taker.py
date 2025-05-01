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

# Necessary variables
score = 0
current_index = 0

for i in range(quiz_length):
    quiz_order.append(question_start)
    question_start += 7    
 
# Randomly pick a question from the file
random.shuffle(quiz_order)

# Load question functions
def load_questions():
    global current_index
    
    if current_index >= quiz_length:
        question_label.config(text = "Quiz is Over!")
        option_a.config(text = "You scored")
        option_b.config(text = score)
        option_c.config(text = "out of")
        option_d.config(text = quiz_length)
        feedback_label.config(text = "Press Exit to end program")
        
        return

    the_question = quiz_order[current_index]
    
    question_label.config(text = reader[the_question])
    option_a.config(text = reader[the_question + 1])
    option_b.config(text = reader[the_question + 2])
    option_c.config(text = reader[the_question + 3])
    option_d.config(text = reader[the_question + 4])

#Button functions
def answered(answer):
    global current_index, score
    
    the_question = quiz_order[current_index]
    
    correct_answer = reader[the_question + 5].split(":")[1].strip()
    
    if answer == correct_answer:
        feedback_label.config(text = "Correct!!")
        score += 1
    else:
        feedback_label.config(text = "Wrong :( ")
        
    # On to the next question
    current_index += 1
    load_questions()

base = tk.Tk()
base.title("Quiz_taker")

# The texts in these labels will be configurated whike the code is running
question_label = tk.Label(base, text = "Hello I am a question", wraplength = 800, font = ("Arial", 10))
question_label.pack(pady = 10)

option_a = tk.Label(base, text = "Option A", wraplength = 800, font = ("Arial", 8))
option_a.pack(pady = 10)

option_b = tk.Label(base, text = "Option B", wraplength = 800, font = ("Arial", 8))
option_b.pack(pady = 10)

option_c = tk.Label(base, text = "Option C", wraplength = 800, font = ("Arial", 8))
option_c.pack(pady = 10)

option_d = tk.Label(base, text = "Option D", wraplength = 800, font = ("Arial", 8))
option_d.pack(pady = 10)

feedback_label = tk.Label(base, text = "", font = ("Arial", 8))
feedback_label.pack(pady = 5)

#Option buttons
button_frame = tk.Frame(base)
button_frame.pack(pady = 10)

button_a = tk.Button(button_frame, text = "A", command = lambda: answered("A"))
button_a.pack(side = "left", padx = 5)

button_b = tk.Button(button_frame, text = "B", command = lambda: answered("B"))
button_b.pack(side = "left", padx = 5)

button_c = tk.Button(button_frame, text = "C", command = lambda: answered("C"))
button_c.pack(side = "left", padx = 5)

button_d = tk.Button(button_frame, text = "D", command = lambda: answered("D"))
button_d.pack(side = "left", padx = 5)

# Exit Button
tk.Button(base, text = "Exit", command = base.quit).pack(pady = 5)

load_questions()
base.mainloop()