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

#Button functions
def answered(answer):
    pass

base = tk.Tk()
base.title("Quiz_taker")

# The texts in these labels will be configurated later
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

base.mainloop()