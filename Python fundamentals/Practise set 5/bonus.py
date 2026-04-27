#1
num = [1, 2, 5, 5, 5, 66, 78, 67, 66]

def list_to_setConverter(num):
    set_num = set(num)
    return set_num

print(list_to_setConverter(num))

#2
products = {"phone": 1200, "watch": 400, "Tv": 9000}

def find_high_priceProduct(prod):
    list_prod = list(prod.items())
    max_price = 0
    max_product = ""
    for product, price in list_prod:
        if price > max_price:
            max_price = price
            max_product = product
    return max_product

print(find_high_priceProduct(products))


#3 merge two dictionaries into one

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)
