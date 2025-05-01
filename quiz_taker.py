# Read the quiz questions file
with open("quiz_questions.txt", "r") as quiz_file:
    reader = quiz_file.readlines()
    
for lines in reader:
    print(lines)
    
# Randomly pick a question from the file
# Do not repeat the questions and end it when it's done
# Add points when answera are correct and show it in the end
# Do all this in tkinter
 