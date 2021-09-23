import random


class Pet:
    Boredom_thresh = 5
    Hunger_thresh = 5
    boredom_decrement = 2
    hunger_decrement = 2

    def __init__(self, names,  Sounds,  Boredom=random.randint(0, Boredom_thresh), Hunger=random.randint(0, Hunger_thresh)):
        self.Sounds = Sounds
        self.Boredom = Boredom
        self.Hunger = Hunger
        self.name = names

    def clock_tik(self):
        self.Boredom += 1
        self.Hunger += 1
        return [self.name, self.Boredom, self.Hunger, self.Sounds]

    def __str__(self):
        (hun_flag, hun_states) = (0, ["I'm not Hunger", "I'm Hunger"])
        (bore_flag, bore_state) = (0, ["I'm Happy", " I'm Bored"])
        if self.Hunger > Pet.Hunger_thresh:
            hun_flag = 1
        if self.Boredom > Pet.Boredom_thresh:
            bore_flag = 1
        return f"\nMy name is  {self.name}.\n{hun_states[hun_flag]} and {bore_state[bore_flag]}\nWords that I learn {self.Sounds}\n"

    def reduce_boredom(self):
        if self.Boredom > 0:
            if self.Boredom < Pet.boredom_decrement:
                Pet.boredom_decrement = random.randint(0, self.Boredom)
            self.Boredom -= Pet.boredom_decrement
            return self.Boredom
        return 0

    def teach(self):
        word = input(f"Enter word for teach your pet {self.name} :")
        self.Sounds.append(word)
        self.Boredom = self.reduce_boredom()
        return [self.name, self.Boredom, self.Hunger, self.Sounds]

    def hi(self):
        input("Talk :")
        try:
            word_index = random.randint(0, len(self.Sounds) - 1)
            print(f"\n{self.Sounds[word_index]}")
        except:
            print("You didn't teach me anything..")
        self.Boredom = self.reduce_boredom()
        return [self.name, self.Boredom, self.Hunger, self.Sounds]

    def reduce_hunger(self):
        if self.Hunger > 0:
            if self.Hunger < Pet.hunger_decrement:
                Pet.hunger_decrement = random.randint(0, self.Hunger)
            self.Hunger -= Pet.hunger_decrement
            return self.Hunger
        return 0

    def feed(self):
        print("Yummy...!")
        self.Hunger = self.reduce_hunger()
        return [self.name, self.Boredom, self.Hunger, self.Sounds]


name = ["dummy_name"]
pets = ["dummy_obj"]
FLAG = 0
while True:
    print(f"\nowned pets {name[1:]}")
    print('Here you can teach, interact, feed your pet')
    pet_name = input("Enter the name of pet :")
    result = []
    obj = Pet(pet_name, result)
    for j, val in enumerate(name):
        if obj.name in val:
            print(pets[j])
            while True:
                user = input("0 - Teach \n1 - Interact\n2 - Feed\n3 - Quit\n4 - Another Pet   :\n")
                if user not in ["0", "1", "2"]:
                    if user == "3":
                        FLAG = 1
                    elif user == "4":
                        FLAG = 0
                    else:
                        print("Enter valid input..")
                        continue
                else:
                    if user == "0":
                        result = pets[j].teach()
                    elif user == "1":
                        result = pets[j].hi()
                    elif user == "2":
                        result = pets[j].feed()
                    pets[j] = Pet(result[0], result[3], result[1], result[2])
                    for time in range(1, len(pets)):
                        if pets[j] == pets[time]:
                            value = pets[j].clock_tik()
                            pets[j] = Pet(value[0], value[3], value[1], value[2])
                        else:
                            value = pets[time].clock_tik()
                            pets[time] = Pet(value[0], value[3], value[1], value[2])
                    print(pets[j])
                    continue
                break
            break
    else:
        name.append(pet_name)
        pets.append(obj)
        print(f"{obj.name} added to the list..\n")
        for time in range(1, len(pets)):
            value = pets[time].clock_tik()
            pets[time] = Pet(value[0], value[3], value[1], value[2])

    if FLAG == 1:
        break
