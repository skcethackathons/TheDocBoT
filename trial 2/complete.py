import infermedica_api

api = infermedica_api.API(app_id='bfdd6ddf', app_key='ccd593a6b534da1593df17aa3945bfea')

# Create diagnosis object with initial patient information.
# Note that time argument is optional here as well as in the add_symptom function
request = infermedica_api.Diagnosis(sex='male', age=35)

request.add_symptom('s_21', 'present')
request.add_symptom('s_98', 'present')
request.add_symptom('s_107', 'absent')

# call diagnosis
request = api.diagnosis(request)

# Access question asked by API
print(request.question)
print(request.question.text)  # actual text of the question
print(request.question.items)  # list of related evidences with possible answers
print(request.question.items[0]['id'])
print(request.question.items[0]['name'])
print(request.question.items[0]['choices'])  # list of possible answers
print(request.question.items[0]['choices'][0]['id'])  # answer id
print(request.question.items[0]['choices'][0]['label'])  # answer label

# Access list of conditions with probabilities
print(request.conditions)
print(request.conditions[0]['id'])
print(request.conditions[0]['name'])
print(request.conditions[0]['probability'])

'''
# Next update the request and get next question:
# Just example, the id and answer shall be taken from the real user answer
request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])

# call diagnosis method again
request = api.diagnosis(request)
'''
