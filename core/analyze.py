import cfscraper
import json 

handles = cfscraper.get_iranian_users(50)
print(handles)
problems = {}

# The filtering formula is explained in the README.md

for handle in handles :
    user_problems = cfscraper.get_problems(handle)
    for problem in user_problems :
        score = 2e3 / len(user_problems)
        if problem in problems.keys(): 
            problems[problem] += score
        else :
            problems[problem] = score
    print(handle, " completed...")

srt = dict(sorted(problems.items(), key=lambda x : x[1] , reverse=True))
print(srt)
with open('table.json', 'w') as f:
    json.dump(srt, f)
