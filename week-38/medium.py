'''
Consider the following list of dictionaries

products = [{"product": "A", "price": 12.20}, 
            {"product": "B", "price": 15.60}, 
            {"product": "C", "price": 9.10}]
Write a Python function to find the most expensive product.
'''

def findMostExp(products):
    max_val = 0
    res_index = 0
    
    for i in range(len(products)):
        
        if products[i]['price'] > max_val:
            max_val = products[i]['price'] 
            res_index = i
            
    return res_index


if __name__ == "__main__":
    products = [{"product": "A", "price": 12.20}, 
                {"product": "B", "price": 15.60}, 
                {"product": "C", "price": 9.10}]
    
    idx = findMostExp(products)
    
    print(products[idx])