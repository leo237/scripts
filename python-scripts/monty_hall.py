import random

RUN_EXPERIMENT_NUMBER_OF_TIMES = 100000

SWITCH_STRATEGY = True


GOAT = 'goat'
CAR = 'car'

class MontyHall:
    def __init__(self):
        self.door_with_car = random.randint(0,2)
        """
        below, for visualization purposes only.
        """
        self.doors = [GOAT, GOAT, GOAT]
        self.doors[self.door_with_car] = CAR
    
    def is_car(self,door_number):
        if door_number == self.door_with_car :
            return True
        return False

    def reveal_one_goat(self,chosen_door_number):
        all_doors = [i for i in range(3)]
        all_doors.remove(self.door_with_car)
        if chosen_door_number in all_doors:
            all_doors.remove(chosen_door_number)
        return random.choice(all_doors)


if __name__ == "__main__":

    winner = 0
    loser = 0

    for i in range(RUN_EXPERIMENT_NUMBER_OF_TIMES):
        monthy_hall = MontyHall()
        
        all_possible_options = [i for i in range(3)]
        guessed_door = random.randint(0,2)
        
        goat_door = monthy_hall.reveal_one_goat(guessed_door)
        all_possible_options.remove(guessed_door)
        if goat_door in all_possible_options:
            all_possible_options.remove(goat_door)
        
        if SWITCH_STRATEGY:
            changed_door = all_possible_options[0]
        else:
            changed_door = guessed_door

        if monthy_hall.is_car(changed_door):
            winner+=1
        else:
            loser+=1
        
        # type casting for making it python2 compatible.
    print("Win percentage : {}".format(float(winner)/RUN_EXPERIMENT_NUMBER_OF_TIMES))
    print("Loss percentage : {}".format(float(loser)/RUN_EXPERIMENT_NUMBER_OF_TIMES))
