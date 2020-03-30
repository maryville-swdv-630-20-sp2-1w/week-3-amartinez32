
class Apartment:
    def __init__(self, num_of_bedrooms, price):
        self.num_of_bedrooms = num_of_bedrooms
        self.price = price
        
    def __str__(self):
        return "Number of bedrooms:  " + str(self.num_of_bedrooms) + '\n' + "Price of apartment: $" + str(self.price)
        
    def getPrice(self):
        return str(self.price)

    def getBedroom(self):
        return self.num_of_bedrooms   


class SingleApartment(Apartment):
    
    def __init__(self,animal):
        self.animal = animal
        Apartment.__init__(self, 1, 1050)
        
    def getFloorLevel(self):
        level = input("What floor level do you want to live on? Bottom or top:")
        if level == 'top':
            print( "Congrats you are on the top level.")
        elif level == 'bottom':
            print( "Congrats you are on the bottom level.")
        else:
            print( "I am sorry that is not an option. Please choose from top or botton floor level.")
            

class DoubleApartment(Apartment):
    
    def __init__(self):
        Apartment.__init__(self, 2, 1500)
         
    def addWasherAndDryer(self):
        add = input("Do you want to add a washer and dryer?")
        if add == 'yes':
            print("Your total with the addition of the washer and dryer is: $" + str(50 + self.price))
        elif add == 'no': 
            print("Your total is: $" + str(self.price))
        else:
            print("Invalid response")
    
            

       

class Townhome(Apartment):
    
    def __init__(self):
          Apartment.__init__(self, 3, 2500)
          
    def addBathroom(self):
        bathroom = input("Do you want to add an addition bathroom?")
        if bathroom == 'yes':
           print( "Your total with the addition of the bathroom is: $" + str(125 + self.price))
        elif bathroom == 'no':
            print( "Your total with the addition of the bathroom is: $" + str(self.price))
        else:
            print("Invalid response")
    
   
                                      

single = SingleApartment("dog")
print(single.animal)
single.getFloorLevel()
#print(single)
double = DoubleApartment()
double.addWasherAndDryer()
#print(double)

home = Townhome()
#print(home)
home.addBathroom()
    
