'''

Given a list of dictionaries where each dictionary contains 
‘name’ and ‘date_of_birth’ of individuals, 
write a Python function to find the oldest person. For example:

persons = [
{"name": "Kedeisha", "date_of_birth": "1994-05-20"},
{"name": "Homer", "date_of_birth": "1956-05-12"},
{"name": "Bruce", "date_of_birth": "1915-04-07"},
]
'''

from datetime import date

def findAge(dob, nowTime):
    year, month, day = map(int, dob.split("-"))
    
    # print(year, month, day)
    # print(nowTime.year, nowTime.month, nowTime.day)
    
    age = nowTime.year - year - (
            (nowTime.month, nowTime.day) < (month, day))
    
    return age


def findOldest(persons):
    idx = 0
    maxAge = 0
    nowTime = date.today()
    for i, person in enumerate(persons):
        currAge = findAge(person['date_of_birth'], nowTime)
        if currAge > maxAge:
            idx = i
            maxAge = currAge
            
    return idx



if __name__ == "__main__":
    
    persons = [
            {"name": "Kedeisha", "date_of_birth": "1994-05-20"},
            {"name": "Homer", "date_of_birth": "1956-05-12"},
            {"name": "Bruce", "date_of_birth": "1915-04-07"},
            ]
    oldest = findOldest(persons)
    
    print(persons[oldest])