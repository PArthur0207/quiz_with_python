# Add wow factor (Tkinter inputs)
import tkinter as tk

# Functions for the buttons
def save_question():
    question = entry_question.get()
    option_a = entry_a.get()
    option_b = entry_b.get()
    option_c = entry_c.get()
    option_d = entry_d.get()
    answer = entry_answer.get().upper()

    if not (question and option_a and option_b and option_c and option_d and answer):
        status_label.config(text = "Please input all that is necessary", fg = 'red')
        return
    
    valid_answers = ['A', 'B', 'C', 'D']
    if answer not in valid_answers:
        status_label.config(text = "Please input only A/B/C/D for the answer", fg = 'red')
        return

    # Use append to add content to the quiz_questions.txt file, creates it if it doesn't exist yet
    quiz_file = open("quiz_questions.txt", "a")
    # Write the inputs to the quiz_questions.txt file
    quiz_file.write(f"Question: {question} \n")
    quiz_file.write(f"A.) {option_a} \n")
    quiz_file.write(f"B.) {option_b} \n")
    quiz_file.write(f"C.) {option_c} \n")
    quiz_file.write(f"D.) {option_d} \n")
    quiz_file.write(f"Answer: {answer} \n")
    quiz_file.write("------------------------ \n")

    # Close the text file
    quiz_file.close()

    # Remove the inputtted labels from the grids
    entry_question.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    entry_answer.delete(0, tk.END)
    status_label.config(text = "")

def exit_program():
    base.destroy()

# Make a base for the tkinter
base = tk.Tk()
base.title("Quiz Creator")

# Make a label for each inputs
tk.Label(base, text = "Enter Question here:").pack()
entry_question = tk.Entry(base, width = 50)
entry_question.pack()

tk.Label(base, text = "Enter Option A here:").pack()
entry_a = tk.Entry(base, width = 50)
entry_a.pack()

tk.Label(base, text = "Enter Option B here:").pack()
entry_b = tk.Entry(base, width = 50)
entry_b.pack()

tk.Label(base, text = "Enter Option C here:").pack()
entry_c = tk.Entry(base, width = 50)
entry_c.pack()

tk.Label(base, text = "Enter Option D here:").pack()
entry_d = tk.Entry(base, width = 50)
entry_d.pack()

tk.Label(base, text = "Enter Correct Answer (A/B/C/D) here: ").pack()
entry_answer = tk.Entry(base, width = 50)
entry_answer.pack()

# Add a save question button and its functions
tk.Button(base, text = "Save Question", command = save_question).pack(pady = 5)

# Add an exit input
tk.Button(base, text = "Exit", command = exit_program).pack(pady = 5)

status_label = tk.Label(base, text = "")
status_label.pack()

base.mainloop()