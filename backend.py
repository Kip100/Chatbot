import openai

class Chatbot:
    def __init__(self):
        self.openai_api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about men")
    print(response)






