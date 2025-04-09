# Use append to add content to the quiz_questions.txt file, creates it if it doesn't exist yet
quiz_file = open("quiz_questions.txt", "a")

while True: # Loop all until the user don't want to input anymore
    # Ask the question
    question = input("Input your question \n>")

    options = {} # Added the dictionary for seperating each letter option
    # Ask for 4 options, make a dictionary for the options
    for letter in ['a', 'b', 'c', 'd']:
        choice = input(f"Input option {letter} \n>")
        options[letter] = choice

    # Ask for the answer from the options
    answer = input("Input your answer here(a/b/c/d) \n>")

    # Write the inputs to the quiz_questions.txt file
    quiz_file.write(f"Question: {question} \n")
    for letter in ['a', 'b', 'c', 'd']:
        quiz_file.write(f"{letter}.) {options[letter]} \n")
    quiz_file.write(f"Answer: {answer} \n")
    quiz_file.write("------------------------ \n")

    again = input("Would you like to input another question? Press 'y' if yes, press any other key if no: ")
    if again != 'y':
        print("Thank you for using this quiz creator")
        break

# Close the file
quiz_file.close()

# Add wow factor (Tkinter inputs)