class Plants:

    def __init__(self, name, type, category , price = 0 ):
        self.name = name
        self.type = type
        self.category  = category 
        self.price = price


class PlantStore:


    plants = []
    selectedPlant = []


    def __init__(self, name, type, category , price ):
        p = Plant(name,type,category  = category , price = price)
        self.plants.append(p)
    
    def show(self):
        print("******************* AVAILBALE PLANTS *******************")
        
        pos=1


        for plant in self.plants:
            print("*******************", pos, " *******************")
            pos += 1   
            self.display(plant)
            
    
    def select(self):
        print("***********SELECT A PLANT *************")
        print("***********HOW MANY PLANT YOU WANT? ************")
        neededPlants = int(input())


        for i in range(0, neededPlants ):
            print("************ INPUT THE PLANT NO ***********")
            selectedPlant = int(input())
            print("************* SELECTED A PLANT ************")
            p = self.getPlantById(selectedPlant - 1)
            self.selectedPlant.append(p)
            print(self.display(p))


    def getPlantById(self, position):
        return self.plants[position]


    def display(self, plant):
        print("Plant name : ", plant.name)
        print("Plant CATEGORY  : ", plant.category )
        print("Plant Price : ", plant.price)
        print("Plant Type : ",plant.type)


    def selectedPlants(self):
        retur+n self.selectedPlant




class BillCounter:


    plants = []
    def __init__(self, myPlants):
        self.plants = myPlants
    
    def display(self):
        pos = 1
        for plant in self.plants:
            print("*********** BILL COUNTER PLANTS************")
            pos += 1
            print("********** PLANT NO", pos," **********")
            print("Plant Name : ", plant.name)
            print("Plant Category  : ", plant.category )
            print("Plant Price : ", plant.price)
            print("Plant Type : ",plant.type)


    def getTotal(self):
        total = sum(map(lambda p : p.price, self.plants))
        print("************ TOTAL PRICE ***********")
        print(total)
    
    def getMax(self):
        total = max(map(lambda p : p.price, self.plants))
        print("************* MAX PRICE ***************")
        print(total)


    def getMin(self):
        total = min(map(lambda p : p.price, self.plants))
        print("************** MIN PRICE **************")
        print(total)


    def getTypes(self):
        print("******************* TYPES *******************")
        types = map(lambda a : a.type, self.plants)
        for type in types:
            print(type)
    


    def delete(self):
        print("******************* IF YOU WANT DELETE PRESS 1 ELSE 0 *******************")
        choice = int(input())
        if (choice == 1):
            print("*******************ENTER PLANT NUMBER *******************")
            position = int(input())
            self.plants.remove(self.getPlantById(position))
        else:
            print("******************* NO PLANTS IN THE CART *******************")


    def getPlantById(self, position):
        return self.plants[position - 1]


    
if "__MAIN__":


    print("************ WELCOME TO PLANT STORE ************")


    ps = PlantStore("GRAPE", "FRUIT", "CLIMBER", 129)
    ps = PlantStore("LILAC", "FLOWER", "SHRUB", 289)
    ps = PlantStore("WATERMELON", "FRUIT", "CREEPER", 99)
    ps = PlantStore("SPINACH", "VEGETABLE", "HEBERS", 89)
    
    ps.show()


    ps.select()


    selectedPlants = ps.selectedPlants()
    
    print(selectedPlants)


    bc = BillCounter(selectedPlants)


    bc.display()

    bc.getTypes()



    bc.getTotal()


    bc.getMax()


    bc.getMin()