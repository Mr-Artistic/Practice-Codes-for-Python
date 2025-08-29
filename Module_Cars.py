car_details = {}

def make_car(make, model, **kwargs):
    car_details['make'] = make
    car_details['model'] = model
    car_details['other details'] = kwargs
    return car_details

for car, value in car_details.items():
    print(car, value)