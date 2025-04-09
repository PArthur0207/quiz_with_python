# Use append to add content to the quiz_questions.txt file, creates it if it doesn't exist yet
quiz_file = open("quiz_questions.txt", "a")

# Ask the question
question = input("Input your question \n>")

# Ask for 4 options, make a dictionary for the options
for letter in ['a', 'b', 'c', 'd']:
    choice = input(f"Input option {letter} \n>")

# Ask for the answer from the options
answer = input("Input your answer here(a/b/c/d) \n>")

# Write the inputs to the quiz_questions.txt file
# Loop all until the user don't want to input anymore
# Close the file
quiz_file.close()