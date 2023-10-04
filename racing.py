import random

class Car:
    def __init__(self, name):
      self.name = name
      self.distance = 0

    # Car는 대문자로 시작함 (클래스 이름은 대문자로 시작해야함)

    def move(self):
        random_value = random.randint(0,9)
        if random_value >= 4:
           self.distance +=1
        if random_value < 4:
           self.distance -=1

# def move(self)는 차를 이동시키기 위한 메서드임.
# 0에서 9까지 무작위 값을 생성후, 4이상이면 1씩 움직임. (4가 안넘으면 안움직임)
# 4미만이면 -1칸 움직임 (새로 추가함)

def response(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                raise ValueError()
            return value
        except ValueError:
            print("[ERROR] 시도횟수는 숫자여야 한다.")

#  def response는 사용자로부터 유효한 값을 위한 함수임.
#  message를 출력하고 유효한 숫자가 나올때까지 반복함.
#  유효한 숫자가 안나오면 에러가 나옴
#  ValueError 대문자로 시작해야함.


def main():
    num_cars = response("경주할 자동차 대수를 입력하세요 : ")

# def main은 자동차 경주의 로직을 담은 함수임.
#  response 함수를 이용하여 자동차 대수를 입력받음.


    cars = []
    # cars = [] 자동차 객체를 저장할 빈 리스트임
    for i in range(num_cars):
        car_name = input(f"자동차 이름을 입력하세요 (5자 이하) :")
        if len(car_name) >=5:
            print("[ERROR] 자동차 이름은 5자 이하로 입력하세요.")
            return
        cars.append(Car(car_name))

    # 입력받은 자동차 대수 만큼 반복함. len은 이름길이를 체크하여 5자이하인지 확인함
    # 이름이 유효하면 Car 객체를 생성하고 cars 리스트에 추가가 됨.


    num_moves = response("시도할 횟수를 입력하세요 : ")

    #  이동횟수를 입력받음


    for m in range(num_moves):
        for car in cars:
            car.move()
            print(f"{car.name} : {'-' * car.distance}")
    # 입력받은 이동 횟수만큼 게임을 반복함.
    # move 메서드를 각각 자동차가 호출하여 이동함.
    # print를 통해 현지 위치를 알려줌

    max_dis = max(car.distance for car in cars)
    winner = [car.name for car in cars if car.distance == max_dis]
    # max_dis는 최대 이동거리를 찾음
    # 최대 이동한 자동차의 이름을 winner 리스트에 저장함

    print(f"최종 우승자 : {', ' .join(winner)}")
    #리스트에 저장된 winner를 출력함 우승자가 다수면 , 으로 구분함.

    if len(winner)>1:
        print(f"공동우승입니다.")
    #리스트에서 우승자가 2명이상일때 출력됨.


if __name__ == "__main__":
   main()