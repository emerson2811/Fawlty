products = {"Chair": 40, "Sofa": 500, "Table": 90, "Monitor": 100, "Carpet": 200}

newproduct = input('Enter product name')

if (newproduct in products):
    print(get(newproduct))
else:
    print('Product Not Found')

#
# products = {'Mac': 1000, 'HP': 700, 'Dell': 350}
# productrequest = input('What product are you interested in?')
#
# if (productrequest in products):
#     print(products.get(productrequest))
# else:
#     print('Product Not Found')