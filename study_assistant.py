# Lab Activity 2
# Study Assistant and Intelligent FAQ Assistant

# Common student questions and answers
faq = {
    "python": "Python is a high-level programming language.",
    "linked list": "A linked list is a data structure made of nodes.",
    "tcp": "TCP is a connection-oriented protocol that provides reliable data transfer.",
    "udp": "UDP is a connectionless protocol that sends data without guaranteeing delivery.",
    "exam": "Prepare a timetable, revise important topics, and practise previous questions.",
    "prompt engineering": "Prompt engineering is the process of designing instructions to get useful AI responses."
}
# Function to answer a question
def get_answer(question):
    question = question.lower()

    for keyword, answer in faq.items():
        if keyword in question:
            return answer

    return "Sorry, I don't have an answer for that question yet."


# Main program
while True:
    print("\n===== STUDY ASSISTANT =====")
    print("1. Zero-shot Prompting")
    print("2. Few-shot Prompting")
    print("3. Role Prompting")
    print("4. Intelligent FAQ Assistant")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        question = input("Enter your question: ")

        # Zero-shot: no examples are provided
        print("\nZero-shot Prompt:")
        print("Answer this student question:", question)
        print("Answer:", get_answer(question))

    elif choice == "2":
        question = input("Enter your question: ")

        # Few-shot: provide examples before the question
        print("\nFew-shot Prompt:")
        print("Example: What is TCP? -> Reliable data transfer.")
        print("Example: What is UDP? -> Connectionless data transfer.")
        print("New question:", question)
        print("Answer:", get_answer(question))

    elif choice == "3":
        question = input("Enter your question: ")

        # Role prompting: assign a teacher role
        print("\nRole Prompt:")
        print("You are a friendly computer science teacher.")
        print("Student question:", question)
        print("Teacher's answer:", get_answer(question))

    elif choice == "4":
        question = input("Ask a student FAQ: ")
        print("\nFAQ Answer:", get_answer(question))

    elif choice == "5":
        print("Thank you for using Study Assistant!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")