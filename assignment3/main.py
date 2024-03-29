#815257

class House:
    def __init__(self, rooms=1):
        self.rooms = rooms
        self.value = self.valuate()
        
    def valuate(self):
        return 10000*(self.rooms)
    
    def __str__(self):
        return '[] '*self.rooms    


class Player:
    def __init__(self, name, houses=[]):
        self.name = name
        self.houses = houses
    
    def __str__(self):
        return f'Name: {self.name}\nProperties Owned:{len(self.houses)}'
    
    #Only accept an integer within min(inclusive) and max(exclusive)
    def get_int(self,min,max):
        x = ""
        while not(isinstance(x, int) and x>=min and x<max ):
            try:
                x = int(input("> "))
                if not(x>=min and x<max):
                    print(f'Only values between {str(min)} and {str(max-1)} are allowed!')
            except ValueError:
                print("Invalid value! only integers allowed.")
        return x
    
    #function to create a House
    def new_house(self):
        print("\nEnter the number of rooms in the house:")
        rooms = self.get_int(1,11)
        return House(rooms)
    
    #function to append a House
    def add_house(self):
        house = self.new_house()
        self.houses.append(house)
    
    def display_houses(self):
        i = 1
        print("\nHouse #\t\tRooms")
        for house in self.houses:
            print(f'House {str(i)}   | {str(house)}')
            i+=1

    def del_house(self):
        self.display_houses()
        print("\nChoose the house to Sell")
        choice = self.get_int(1,len(self.houses)+1)
        del self.houses[choice-1]
        print("\Processing the Transaction...")
        self.display_houses()


    def net_worth(self):
        self.display_houses()
        x = 0
        for h in self.houses:
            x+=h.value
        print("Net Worth: $"+str(x)+"\n")
    
    def sort_houses_by_room(self):
        #sort
        n = len(self.houses)
        for i in range(n):
            for j in range(0, n-i-1):
                    if self.houses[j].rooms > self.houses[j+1].rooms:
                        #Swap the houses
                        self.houses[j], self.houses[j+1] = self.houses[j+1], self.houses[j]
        self.display_houses()
        
class Game:
    def __init__(self):
        name = input("Enter name for the Owner:")
        self.player = Player(name)
        
    def display_prompt(self):
        ascii_art = '''
.______       _______     ___       __             _______     _______.___________.    ___   .___________. _______ 
|   _  \     |   ____|   /   \     |  |           |   ____|   /       |           |   /   \  |           ||   ____|
|  |_)  |    |  |__     /  ^  \    |  |           |  |__     |   (----`---|  |----`  /  ^  \ `---|  |----`|  |__   
|      /     |   __|   /  /_\  \   |  |           |   __|     \   \       |  |      /  /_\  \    |  |     |   __|  
|  |\  \----.|  |____ /  _____  \  |  `----.      |  |____.----)   |      |  |     /  _____  \   |  |     |  |____ 
| _| `._____||_______/__/     \__\ |_______|      |_______|_______/       |__|    /__/     \__\  |__|     |_______|
                                                                                                                   
               .___________.____    ____  ______   ______     ______   .__   __.                                   
               |           |\   \  /   / /      | /  __  \   /  __  \  |  \ |  |                                   
               `---|  |----` \   \/   / |  ,----'|  |  |  | |  |  |  | |   \|  |                                   
                   |  |       \_    _/  |  |     |  |  |  | |  |  |  | |  . `  |                                   
                   |  |         |  |    |  `----.|  `--'  | |  `--'  | |  |\   |                                   
                   |__|         |__|     \______| \______/   \______/  |__| \__|                                                           
        '''
        print(ascii_art)

    
    def main_menu(self):
        print("[1] Buy a new house")
        print("[2] Sell a House")
        print("[3] Show Net Worth")
        print("[4] Sort Houses by number of Rooms")
        print("[0] Exit")
        
    def game_loop(self):
        while True:
            self.main_menu()
            i = input("> ").strip()
            if i == '1':
                self.player.add_house()
            elif i == '2':
                self.player.del_house()
            elif i == '3':
                self.player.net_worth()
            elif i == '4':
                self.player.sort_houses_by_room()
            elif i == '0':
                break
            else:
                print("Invalid option, try again...")
        print("\nThank you for using trusting us with your financials.")


g = Game()

g.display_prompt()
g.game_loop()