import openai
import json


openai.api_key = "Your API key"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[
        {"role": "user", "content": ''' Create 15 questions quiz with 4 answers for each question. 
         Theme should be Python and become harder to the end. Last one is the hardest. 
        It should looks like this{
          "questions": [
            {
              "q": "What is Python?",
              "options": [
                "A high-level programming language",
                "A low-level programming language",
                "A markup language",
                "A style sheet language"
              ],
              "answer": "A high-level programming language"
            },
            {
              "q": "Which of the following is NOT a Python data type?",
              "options": [
                "List",
                "Dictionary",
                "Tuple",
                "Map"
              ],
              "answer": "Map"
             }
          ]
        }'''}
    ])


data_get = completion.choices[0].message.content
data = json.loads(data_get)
data_list = data['questions']
"""Variables with questions and answers"""
all_questions = []
first_option = []
second_option = []
third_option = []
fourth_option = []
correct_answer = []


"""Appending lists"""

for i in range(15):
    all_questions.append(data_list[i]['q'])
    first_option.append(data_list[i]['options'][0])
    second_option.append(data_list[i]['options'][1])
    third_option.append(data_list[i]['options'][2])
    fourth_option.append(data_list[i]['options'][3])
    correct_answer.append(data_list[i]['answer'])

print(all_questions)
print(correct_answer)


