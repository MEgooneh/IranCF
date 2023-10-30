import requests as r
from bs4 import BeautifulSoup
import logging

def convert_problem_to_id(problem):

    """Converting problem dictionrat to plain text id.
    """

    return str(problem["contestId"]) + " " + problem["index"]

def get_problems_objects(handle):
    
    """Getting unique problems infos.

    type: dictionary
    """

    problems_objects_dict = {}
    missed = 0
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    try:
        res = r.get(url).json()["result"]
        for subm in res :
            problem = subm["problem"]
            try :
                problems_objects_dict[convert_problem_to_id(problem)] = problem
            except : 
                missed += 1
        logging.info(handle + f" -> {missed} problems missed!")
    except Exception as e:
        logging.error(str(e) + " " + handle)
    return problems_objects_dict

def get_problems(handle) :

    """Getting the problem id of all unique problems 
    submitted by some one.

    type: plain text
    """

    problems = get_problems_objects(handle)
    return problems.keys()

def get_iranian_users(count=50) :
    url = "https://codeforces.com/ratings/country/Iran"
    res = r.get(url).text
    soup = BeautifulSoup(res, "lxml").find('div', {'class': 'ratingsDatatable'})
    handle_blocks = soup.find_all('a', {'class': 'rated-user'}, limit=count)
    handles = [block.text for block in handle_blocks]
    return handles


