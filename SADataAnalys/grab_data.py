from jotform import *

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

    print(positive)
    print(negative)
    print(undetermined)

if __name__ == "__main__":
    main()