#미션1: 

class Queue:
    def __init__(self):
        self.q_array = [None]
    def enqueue(self, data):
        self.q_array.append(data)
    def dequeue(self):
        returned_data=self.q_array[1] 
        del self.q_array[1]
        return returned_data
        
############## data ###############
cargo_list=[]

import random
random.seed(20201216)
import datetime
departure_time=datetime.datetime(2050, 2, 27, 10, 00)

class Cargo:
    def __init__(self):
        self.number=random.randint(10000, 99999) # 화물번호(50230)
        self.truck_number=random.randint(0, 9) #트럭 번호 
        self.departure_time=datetime.datetime(2050,2,27,10,00) #출발 시간

while len(cargo_list)!=100:
    cargo=Cargo() 
    if cargo not in cargo_list:
        cargo_list.append(cargo)

round_num_list=[0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0]
time_per_round_list=[40, 50, 60, 30, 20, 25, 10, 5, 55, 25]

############## data ###############

#트럭의 출발 시간 찾기
truck_list = [] #트럭 리스트
for truck in range(10):
    new_truck = Queue() #new truck
    truck_list.append(new_truck)

# 트럭에 화물 차례대로 싣기
for i in range(len(cargo_list)):
    truck_number = cargo_list[i].truck_number
    truck_list[truck_number].enqueue(cargo_list[i])
#화물을 담은 트럭이 full이면 출발하고, 출발 시각을 leaveorder에 기록
    if len(truck_list[truck_number].q_array)-1 ==3:
        while(len(truck_list[truck_number].q_array)-1 !=0):
            dequeue_data=truck_list[truck_number].dequeue()
           #출발 시각 계산 
            dequeue_data.departure_time+=datetime.timedelta(minutes=time_per_round_list[truck_number]*round_num_list[truck_number])
            if (dequeue_data.number==50230):
                answer = dequeue_data.departure_time
                print(answer)
           #한 바퀴 돈 후
        round_num_list[truck_number]+=1
