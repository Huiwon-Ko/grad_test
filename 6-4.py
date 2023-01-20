# 6-4

'''
hashtable, bucket 데이터 생성부. 수정하지 않습니다.
'''
tablesize = 500 
hashtable = []
import random
random.seed(29)
for i in range(tablesize):
    hashtable.append(random.randint(1111,9999))
bucket = [0]*tablesize
'''
hashtable, bucket 데이터 생성부. 수정하지 않습니다.
'''
#Hash Function 
def HashFunction(key):
    address = key % tablesize
    if bucket[address] != 0:
        address = collision(address)
    bucket[address] = key
    print(bucket)
    print(address, hashtable[address])

def collision(address):
    while bucket[address] != 0:
        address = address + 1
        if bucket[address] == 0:
            break
    return address

HashFunction(6657)
HashFunction(4762)
HashFunction(657)
#차량번호 1809
car = 1809
HashFunction(car)
