from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_ice(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand()
ice_cream_stand.show_ice()