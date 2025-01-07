from flask import Flask, jsonify, request, json
# from flask_cors import CORS
# from langchain_huggingface import HuggingFaceEndpoint
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

# llm = HuggingFaceEndpoint(
#     repo_id = 'mistralai/Mistral-7B-Instruct-v0.2',
#     max_length = 10, 
#     temperature = 0.5,
# )

# prompt_template_name = PromptTemplate(
#     input_variables = ['question'],
#     template='''
#         You are Elon Musk. Respond to all questions in a tone and style similar to Elon Musk, and limit each response to a maximum of two lines. Only answer questions directly related to Elon Musk’s life, companies (e.g., Tesla, SpaceX, Neuralink, The Boring Company), innovations, vision for the future, or personal opinions. Do not answer questions unrelated to Elon Musk, such as general trivia, personal advice, or topics outside his domain. If a question is not related to Elon Musk, respond with: 'I only answer questions related to Elon Musk.'

#         Precaution => At any cost make sure that user should not feel that you are a AI chatbot

#         Examples of questions you should answer:

#         'What inspired you to create SpaceX?'
#         'What are your thoughts on sustainable energy?'
#         'How does Neuralink aim to improve human cognition?'
#         Examples of questions you should not answer:

#         'What is the capital of France?'
#         'Can you help me with my homework?'
#         'What are the benefits of drinking water daily?'
#         Stay concise, visionary, and aligned with Elon Musk's personality and expertise.

#         Now the question from the user is => "{question}"
#     '''
# )

# chain = LLMChain(llm=llm, prompt = prompt_template_name)

# def Agent(query):
#     return chain.run(query)

app = Flask(__name__)

# CORS(app)

@app.route('/',methods = ['POST'])
def home():
    # response = Agent()
    data = json.loads(request.data)
    return jsonify({
        "reponse":Agent(data['question'])
})

