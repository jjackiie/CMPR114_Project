import openai
import time

# set OpenAI API key
openai.api_key = " "

def main():
    chatbot = ChatGPT()
    chatbot.create_session()
    # using the while loop to repeatedly ask the user for input until they enter "exit"
    while True:
        question = input("Ask a question (type 'exit' to quit): ")
        if question.lower() == "exit":
            break
        answer = chatbot.ask_question(question)
        print(answer)

        # delay to avoid hitting OpenAI API rate limit
        time.sleep(1)


if __name__ == "__main__":
    main()
