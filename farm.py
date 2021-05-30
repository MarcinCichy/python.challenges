# Challenge: Model a Farm
# from RealPython, Python Basics, chapter 10.4
#

class Animals:
    
    def __init__(self, name, age, species, color):
        self.name = name
        self.age = age
        self.species = species
        self.color = color

    def speak(self, sound):
        return f"{self.name} says {sound} " 

    def eat(self, hungry, food):
        if hungry:
            return f"{self.name} is eating {food}"
        else:
            return f"{self.name} doesn't looking at the bowl and says every day the same {food}, bleee."
        
    def sleep(self, where):
        return f"{self.name} says goodnight. I go to sleep in {where}"

    def walk(self, place):
        return f"I walk around the {place}. I got somewhere? Nowhere!!!! "

class Bird(Animals):
    def flying (self):
        return f"{self.name} sings I believe, I can fly!"      

class Cattle(Animals):
    def milking(self):
        return "my udders are full and I want to be milked. "

class Flock(Animals):
    def rolling_in_mud(self, weather):
        if weather == "raining":
            return f" I love rolling in the mud like I was 2 years old not {self.age}."
        else:
            return f"boring weather"

class Dog(Animals):
    def bite(self):
        return f"Mniam! Fresh flesh."
    def growl(self):
        return f"Grrrrrr!!! Go away!!!"

class Cat(Animals):
    def catch_mouse(self, victim ):
        if victim:
            return f"I see you {victim}!. My baby, you'll be mine."
        else:
            return f"What I do here?"


dog = Dog("Burek",3,"promenaden miszung", "czarny")
cow1 = Cattle("Krasula",2,"holenderka","laciata")
cow2 = Cattle("Mucka",5,"holenderka","black")
pig1 = Flock("Piggy",10,"tucznik", "pink")
rooster = Bird("BraveHeart",4,"pieniacz","mulicolor")
chicken = Bird("Lollypop",1,"zoltodziub","white")
little_cat = Cat("Mruczek",15,"siersciuch","striped")
cow1 = Cattle("Krasula",2,"holenderka","laciata")
cow2 = Cattle("Mucka",5,"holenderka","black")

print("-"*40)
print(dog.speak("WOOOF!!!"))
print("I'm ",dog.species)
print(dog.growl())
print(dog.bite())
print("-"*40)
print(dog.sleep("doghouse"))
print("-"*40)
print("-"*40)
print(cow1.speak("Muuu" ), end="")
print(cow1.milking())
print(f"{cow2.speak('MuuuMan')}, I'm {cow2.color}!")
print("-"*40)
print(f"{pig1.speak('Chrum')}, {pig1.rolling_in_mud('raining')}")
print("-"*40)
print(f"{rooster.eat('','seeds')}")
print(f"{rooster.walk('fence')}")
print(f"{chicken.eat('hungry','seeds')} and {chicken.flying()}")
print("-"*40)
print(f"{little_cat.catch_mouse('rat')}")
