def chat_bot():
    while True:
        user = input("Enter your message :").capitalize()
        if user == "Bye":
            print("Bot: GoodBye")
            break

        if user == "Hello":
            print("Bot: Hi!")
        
        elif user == "Hi how are you":
            print("Bot: I am fineThanks")

        elif user == "Hi":
            print("Bot: Hello!")

        elif user == "How are you":
            print("Bot: I am fine Thanks!")

        elif user == "What is your name":
            print("Bot: My name is Python ChatBot")

        elif user == "Who made you":
            print("Bot: I was made using Python")

        elif user == "Good morning":
            print("Bot: Good Morning!")

        elif user == "Good afternoon":
            print("Bot: Good Afternoon!")

        elif user == "Good evening":
            print("Bot: Good Evening!")

        elif user == "Good night":
            print("Bot: Good Night Take care!")

        elif user == "Thanks":
            print("Bot: You're Welcome!")

        elif user == "Thank you":
            print("Bot: Happy to help!")

        elif user == "What can you do":
            print("Bot: I can answer simple questions")

        elif user == "Help":
            print("Bot: Ask me something simple")

        elif user == "Who are you":
            print("Bot: I am a basic chatbot")

        elif user == "Tell me a joke":
            print("Bot: Why did the computer go to the doctor? Because it had a virus!")

        elif user == "How old are you":
            print("Bot: I don't have an age")

        elif user == "Where are you":
            print("Bot: I live inside your Python program")

        elif user == "Are you real":
            print("Bot: I am a computer program")

        elif user == "What is python":
            print("Bot: Python is a programming language")

        elif user == "Who is your friend":
            print("Bot: Every programmer is my friend")

        elif user == "Nice":
            print("Bot: Thank you!")

        elif user == "Ok":
            print("Bot: Alright!")

        elif user == "Cool":
            print("Bot: Glad you think so!")

        elif user == "What is ai":
            print("Bot: AI means Artificial Intelligence")

        elif user == "Do you like coding":
            print("Bot: Yes! Coding is fun")

        elif user == "Can you code":
            print("Bot: Yes, I can help with coding")

        elif user == "What is your favorite language":
            print("Bot: Python, of course!")

        elif user == "What time is it":
            print("Bot: Sorry, I cannot check the current time")

        elif user == "What day is today":
            print("Bot: Sorry, I cannot tell today's date")

        elif user == "See you":
            print("Bot: See you later!")

        elif user == "Take care":
            print("Bot: You too! Take care")
        else:
            print("Sorry, I did not Understand ")

chat_bot()