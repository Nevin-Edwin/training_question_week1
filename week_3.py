import random


class Pet:
    Boredom_thresh = 5
    Hunger_thresh = 5
    boredom_decrement = 2
    hunger_decrement = 2

    def __init__(self, Boredom=random.randint(0, Boredom_thresh), Hunger=random.randint(0, Hunger_thresh), Sounds=[]):
        self.Sounds = Sounds
        self.Boredom = Boredom
        self.Hunger = Hunger
        print('Here you have teach, interact, feed your pet\n')
        self.name = input("Enter the name of pet :")

    def clock_tik(self):
        self.Boredom += 1
        self.Hunger += 1
        return [self.Boredom, self.Hunger, self.Sounds]

    def __str__(self):
        (hun_flag, hun_states) = (0, ["I am not Hunger", "I am Hunger"])
        (bore_flag, bore_state) = (0, ["Happy", "Bored"])
        if self.Hunger > Pet.Hunger_thresh:
            hun_flag = 1
        if self.Boredom > Pet.Boredom_thresh:
            bore_flag = 1
        return f"I am {self.name}. {hun_states[hun_flag]}{self.Hunger} and {bore_state[bore_flag]}{self.Boredom}"

    def reduce_boredom(self):
        if self.Boredom > 0:
            if self.Boredom < Pet.boredom_decrement:
                Pet.boredom_decrement = random.randint(0, self.Boredom)
            self.Boredom -= Pet.boredom_decrement
            return self.Boredom
        else:
            return 0

    def teach(self):
        word = input(f"enter the word for teach your pet {self.name} :")
        self.Sounds.append(word)
        self.Boredom = self.reduce_boredom()
        return [self.Boredom, self.Hunger, self.Sounds]

    def hi(self):
        user_talk = input("Talk :")
        word_index = random.randint(0, len(self.Sounds))
        try:
            print(word_index)
            print(self.Sounds[word_index])
        except:
            print("You didn't teach me anything..")
        self.Boredom = self.reduce_boredom()
        return [self.Boredom, self.Hunger, self.Sounds]

    def reduce_hunger(self):
        if self.Hunger > 0:
            if self.Hunger < Pet.hunger_decrement:
                Pet.hunger_decrement = random.randint(0, self.Hunger)
            self.Hunger -= Pet.hunger_decrement
            return self.Hunger
        else:
            return 0

    def feed(self):
        print("you pet get food")
        self.Hunger = self.reduce_hunger()
        return [self.Boredom, self.Hunger, self.Sounds]


name = ["dummy_name"]
pets = ["dummy_obj"]
Flag = 0
while True:
    flag = 0
    obj = Pet()
    for j in range(len(name)):
        if obj.name in name[j]:
            print(pets[j])
            while True:
                command = [pets[j].teach(), pets[j].hi(), pets[j].feed()]
                user = int(input(f"0 - Teach :\n1 - Interact\n2 - Feed\n3 - Quit\n4 - Another Pet")).lower()
                if user in [0, 1, 2, 3]:
                    result = command[user]
                    pets[j] = Pet(result[0], result[1], result[2])
                elif user == 4 or user == 5:
                    Flag = 1
                    break
                else:
                    print("Enter valid input..")

                continue
            break

    else:
        name.append(obj.name)
        pets.append(obj)
        print(f"{obj.name} added to the list..")

    if Flag == "4":
        break
    else:
        continue
