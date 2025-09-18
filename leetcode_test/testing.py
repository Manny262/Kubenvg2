def rental_car_cost(d):
    int(d)
    cost = d * 40 
    match d:
        case days if days >= 7:
            cost -= 50
            return cost
        case days if days >= 3:
            cost -= 20
            return cost
        case _:
            return cost
        
print(rental_car_cost(10))
