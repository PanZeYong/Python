class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The resaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type + "\n")

    def open_restaurant(self):
        print("Then restaurant is openning")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        self.number_served += number

    def get_number_served(self):
        return self.number_served
        

restaurant = Restaurant("外婆家", "客家菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served = 22
print(restaurant.number_served)

restaurant.set_number_served(25)
print(restaurant.number_served)

restaurant.increment_number_served(88)
print(restaurant.get_number_served())

