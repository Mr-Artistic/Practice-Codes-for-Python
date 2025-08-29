import Module_Cars as MC

my_car_details = MC.make_car('maruti', 'swift', color='blue', variant='vxi')

for car, value in my_car_details.items():
    print(car, value)

from Module_Cars import make_car as mc

my_car_details = mc('maruti', 'swift', color='blue', variant='vxi')

for car, value in my_car_details.items():
    print(car, value)

