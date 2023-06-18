import openai
import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from keys import openai_key

def create_video(topic: str, ):
        print("made it to function! ", topic)
        return topic

def main():
    openai.api_key = openai_key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", 
        messages=[{"role": "user", "content": "Could you create a video that explains 10 tips to find a new job?"}],
        functions=[
            {
                "name": "create_video",
                "description": "Create a video about a given topic",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {
                            "type": "string",
                            "description": "What the video will be about",
                        }
                    },
                    "required": ["topic"],
                }
            }
        ],
        function_call="auto")

    print(completion.choices[0])

    reply_content = completion.choices[0].message

    funcName = reply_content.to_dict()['function_call']['name']
    args = json.loads(reply_content.to_dict()['function_call']['arguments'])
    
    print(funcName, args)

    func = globals()[funcName]

    func(args['topic'])

    

if __name__ == "__main__":
    main()