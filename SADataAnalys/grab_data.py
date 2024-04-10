from jotform import *

def main():
    jotformAPIClient = JotformAPIClient('0698fe80cbad87f1efa0d63ba86a63e5')

    submissions = jotformAPIClient.get_form_submissions('240840940974159')

    question_label = 'Student FIRST NAME (Please ensure correct spelling and capitalization)'
    positve_statements = []
    negative_statements = []

    for submission in submissions:
        
        #Grab answers
        answers = submission.get('answers', {})
        for key, value in answers.items():

            #Checks for correct student name
            if value.get('text') == question_label and value.get('answer') == "Andrew":
                clean_answers = {k: v['answer'] for k, v in answers.items() if 'answer' in v}
                for key, value in clean_answers.items():
                    if key == '17':
                        positve_statements.append(value)
                    elif key == '18':
                        negative_statements.append(value)

    print(positve_statements)
    print(negative_statements)
    # print(clean_answers)


    # print(submissions)


if __name__ == "__main__":
    main()