'''
Given the following list of emails

emails = ["kedeisha@example.com", 
          "soanli@example.com", 
          "taamir@example.com", 
          "shawn@dim.com", 
          "frank@dim.com", 
          "mikey@dim.com"],

Write a Python function to filter out all emails 
that belong to the “dim.com” domain.
'''

# I am going to improvise the solution
# Here in my solution, any domain name can be checked

import re

def filterEmail(emails, domain_name):
    ans = []
    for email in emails:
        if re.search(f'{domain_name}$', email):
            ans.append(email)
            
    return ans

if __name__ == "__main__":
    
    emails = ["kedeisha@example.com", 
          "soanli@example.com", 
          "taamir@example.com", 
          "shawn@dim.com", 
          "frank@dim.com", 
          "mikey@dim.com"]
    domain_name = "dim.com"
    
    filteredEmail = filterEmail(emails, domain_name)
    print(filteredEmail)
        