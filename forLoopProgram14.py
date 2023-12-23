bus1 = 10
bus2 = 30
total_bus = 10

for i in range(bus1 , bus2):
    if(i%3) == 0:
        total_bus = total_bus -1
    else:
        total_bus = total_bus + 3
    print(total_bus)