def linear_search_product(products, target):
    indices = []
    
    for i, product in enumerate(products):
        if product == target:
            indices.append(i)
    
    return indices

products = ['apple', 'banana', 'orange', 'apple', 'grape']
target = 'apple'
print(linear_search_product(products, target)) # [0, 3]

target = 'peach'
print(linear_search_product(products, target)) # []

 

