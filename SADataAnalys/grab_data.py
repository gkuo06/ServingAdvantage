from jotform import *
from openai import OpenAI #python3.10 -m pip install openai @gigaComputer

import re
import os
from dotenv import load_dotenv #pip install python-dotenv @gigaComputer
load_dotenv() #.env contains OPENAI_API_KEY variable (check Discord)

#File import
import analysis
from queries import query, role

def main():
    jotformAPIClient = JotformAPIClient('0698fe80cbad87f1efa0d63ba86a63e5')

    submissions = jotformAPIClient.get_form_submissions('240840940974159')

    question = 'Student FIRST NAME (Please ensure correct spelling and capitalization)'
    student = 'Andrew' #Andrew for test

    positive = []
    negative = []
    undetermined = []

    for submission in submissions:
        answers = submission.get('answers', {})
        for key, value in answers.items():
            if value['text'] == question and value['answer'] == student:
                clean_response = {k: v['answer'] for k, v in answers.items() if 'answer' in v}

                for key, value in clean_response.items():
                    if key == '16':
                        undetermined.append(value)
                    elif key == '17':
                        positive.append(value)
                    elif key == '18':
                        negative.append(value)
    positive_sentences = [sentence.strip() for text in positive for sentence in filter(None, re.split(r'(?<!\w\.\w.)(?<![A-Z][a.z]\.)(?<=\.|\?|\!)\s', text))]
    negative_sentences = [sentence.strip() for text in negative for sentence in filter(None, re.split(r'(?<!\w\.\w.)(?<![A-Z][a.z]\.)(?<=\.|\?|\!)\s', text))]
    undetermined_sentences = [sentence.strip() for text in undetermined for sentence in filter(None, re.split(r'(?<!\w\.\w.)(?<![A-Z][a.z]\.)(?<=\.|\?|\!)\s', text))]
    
    print(positive_sentences)
    print(negative_sentences)
    print(undetermined_sentences)

    pos, neg = analysis.sentimentAnalysis(undetermined_sentences)

    print(f'Positive: {pos}')
    print(f'Negative: {neg}')

    positive_sentences.extend(pos)
    negative_sentences.extend(neg)

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_message = {
        'role': 'system',
        'content': role
    }

    behaviors = [
        {'role': 'user', 'content': query}
        #{'role' : 'user', 'content' : f'Positive behaviors: {positive_sentences}'}
        #{'role' : 'user', 'content' : f'Negative behaviors: {negative_sentences}'}
        #{'role' : 'user', 'content' : f'Background information: {background_information}'}
    ]

    completion = client.chat.completions.create(
        model = 'gpt-4-turbo-preview',
        messages = [system_message] + behaviors
    )
    
    print(completion.choices[0].message.content)
    
    return completion.choices[0].message.content


if __name__ == '__main__':
    main()