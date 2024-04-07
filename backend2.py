import openai
import time


class Chatbot:
    def __init__(self, api_key):
        self.openai_api_key = api_key
        openai.api_key = api_key

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=user_input,
                max_tokens=3000,
                temperature=0.5
            ).choices[0].text
            return response
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Waiting for reset: {e}")
            time.sleep(60)
            return self.get_response(user_input)


if __name__ == "__main__":

    api_key = "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"

    chatbot = Chatbot(api_key)
    response = chatbot.get_response("Write a joke about men")
    print(response)
