study = {"computer": 2000, "Iiyama Monitor": 500, "MacBook pro": 2500, "desk": 100, "Camera": 600}
living_room = {"couch": 1600, "LG tv": 4500, "speakers": 400, "chair": 450, "table": 100}
bedroom = {"bed": 700, "mattress": 400, " drawers": 350, "lamp": 50, "Xbox": 300}

rooms = {"Study": study, "Living Room":living_room, "Bedroom": bedroom}

def print_contents(room):
    for k, v in room.items():
        print('\n' + k)
        for key, val in v.items():
            print("{}: ${}".format(key, val))

def sum_of_rooms(room):
    print('\nTotals')
    for k, v in room.items():
        print("{}: ${}".format(k, (sum(v.values()))))

print_contents(rooms)
sum_of_rooms(rooms)