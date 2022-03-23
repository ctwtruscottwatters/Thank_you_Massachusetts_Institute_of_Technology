# -*- coding: utf-8 -*-
# Charles Thomas Wallace Truscott
# All my own work
import numpy.random as random
import math
class Item():
    def __init__(self, value, weight, name):
        self.value = value
        self.weight = weight
        self.name = name
    def get_value(self):
        return float(self.value)
    def get_weight(self):
        return float(self.weight)
    def get_name(self):
        return str(self.name)
    def return_metric(self):
        return self.value / self.weight

def main():
    hamburger = Item(10, 2.0, "Hamburger")
    chips = Item(15, 1.0, "Chips")
    drink = Item(5, 5.0, "Drink")
    print('hamburger weight: {} chips weight: {} drink weight: {}'.format(str(hamburger.get_weight()), str(chips.get_weight()), str(drink.get_weight())))
    x = [hamburger, chips, drink]
    for n in x:
        print(n.get_name())
        print('Weight: ' + str(n.get_weight()))
        print('Value: ' + str(n.get_value()))
        
    max_weight = 5.0
    current_weight = 0
#    for n in range(0, len(x)):
#        print(x[random.randint(0, len(x) - 1)].return_metric())
    for n in x:
        if (current_weight >= max_weight):
            print('Knapsack full')
            break
        else:
            print('Added {} to the knapsack with weight {} and value {}'.format(n.get_name(), n.get_weight(), n.get_value()))
            current_weight += n.get_weight()
            print('Weight of knapsack: {}'.format(current_weight))
            if (current_weight >= max_weight):
                print('Knapsack full removing {}'.format(n.get_name()))
                break

        
if __name__ == "__main__": main()