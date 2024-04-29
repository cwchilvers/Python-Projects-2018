def total_num(item):
    count = 0
    values = item.values()
    for v in values:
        if v != '':
            count += 1
    return count


hammer_dict = {"Hammer 1":"Bob", "Hammer 2":"Suzy"}
ham_num = total_num(hammer_dict)
Hammers = {"Hammers":ham_num}

ladder_dict = {"Ladder 1":"Jerry", "Ladder 2":"Victoria"}
ladder_num = total_num(ladder_dict)
Ladders = {"Ladders":ladder_num}

Inventory = [Hammers, Ladders]

print(Inventory)
