# 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet(pet_name="willie", animal_type="dog")

def make_shirt(size = "L", message = "I love Python."):
    print("The size of T-shirt is " + size + " and the message is " + message)

def describe_city(name, country = "China"):
    print(name + " is in " + country)

make_shirt("XL", "T-shirt")
make_shirt(size = "XL", message = "T-shirt")
make_shirt()

describe_city("ShenZhen")
describe_city("BeiJing")
describe_city("New York", "America")