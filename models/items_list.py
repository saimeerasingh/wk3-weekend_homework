from models.items import *

item1 = Items('Cookie',2,3,True)
item2 = Items('Tea',3,2,False)
item3 = Items('Milk',4,1,True)
items_list = [item1,item2,item3]

def add_new_item(item):
    items_list.append(item)

