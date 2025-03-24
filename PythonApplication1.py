import random
my_number = 14
def gen_list(value:int):
    return [random.randint(5,value*100) for x in range(value+10)]
print(gen_list(my_number))
