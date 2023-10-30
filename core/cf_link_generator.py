import json

def generate_link_for_problem(problem) :
    contest , index = problem.split(' ')
    return f"https://codeforces.com/problemset/problem/{contest}/{index}"

with open("table.json", "r") as f:
    x = json.load(f)
txt = '\n'.join([generate_link_for_problem(problem) for problem in x.keys()])

with open("links.txt", "w") as f:
    f.write(txt)