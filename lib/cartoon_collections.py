def roll_call_dwarves(dwarves):
    
    n = 1
    
    for dwarf in dwarves:
        print(f'{n}. {dwarf}')
        n += 1

def summon_captain_planet(list):
    return [f"{call.capitalize()}!" for call in list]

def long_planeteer_calls(list):

    long_calls = []

    for call in list:
        if len(call) > 4:
            long_calls.append(call)
        else: 
            pass
    
    if len(long_calls) != 0:
        return True
    else:
        return False

def find_the_cheese(snacks):
    cheese = ["cheddar", "gouda", "camembert"]

    for snack in snacks:
        if snack in cheese:
            return snack
        else:
            pass
