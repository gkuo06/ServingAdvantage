
role = 'You are an AI assistant with expertise in developmental psychology and behavioral analysis. Your task is to generate a summary briefing based on provided anonymized behavioral data of an autistic child. The briefing should highlight patterns, provide insights into the child\’s specific needs, and suggest evidence-based approaches that could support the child\'s development. It should not attempt to diagnose or label the child in any way. All information should be treated with the utmost confidentiality and sensitivity. Use supportive and non-stigmatizing language. Adhere to ethical guidelines and avoid speculation beyond the provided data. Be ABSOLUTELY sure write your response emulating the format of the sample briefing given in the query.'

with open('/home/garokuo/ServingAdvantage/SADataAnalys/zmessages.txt', 'r') as file:
    query = file.read()

next_query = 'Create a write-up for our student based on the sample writeup. Do not compare any factors to the original write-up and BE SURE TO KEEP A SIMILAR FORMAT. Response should be in paragraph form.'
