#cargoship
import random
random.seed(66)
cargolist = [10, 35, 1, 2, 31, 5, 18, 19, 20, 21, 22, 4, 23, 15, 16, 17, 34, 7, 8, 30, 3, 24, 9, 36, 37, 38, 39, 14, 27, 28, 29, 25, 26, 6, 11, 12, 13, 33, 32]
random.shuffle(cargolist)


class stack:
    def __init__(self, list): 
        self.list = list
    def push(self, data):
        self.list.append(data)
    def pop(self):
        if len(self.list) >0:
            pop_data = self.list[-1]
            del self.list[-1]
            return pop_data
    def clear(self):
        self.list.clear()
cargo = stack(cargolist) #위에 있던거 가져옴
small_cargo = stack([])

def cargo_to_cargo():
    count = 1
    print(count)
    while len(cargo.list) >0:
        small_cargo.push(cargo.pop())
        print(cargo.list)
        print(small_cargo.list)
        if len(small_cargo.list) == 5:
            count +=1
            print(count)
            small_cargo.clear()
            print(small_cargo.list)
cargo_to_cargo()
