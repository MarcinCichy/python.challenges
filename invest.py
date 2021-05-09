# Challenge: Track Your Investments
# from RealPython, Python Basics, chapter 6.5
#


# take datas from user and assign them to variables
amount = float(input ("Podaj wartość początkową inwestycji: "))
rate = float(input ("Podaj oprocentowanie roczne (w procentach): "))
years = int(input ("Podaj okres inwestycji (w latach): "))

def invest(amount, rate, years):
    """ The function counts growing amount of an investment over time """
    rate = rate*0.01
    amount_of_invest = amount
    for i in range(years):
        amount_of_invest = amount_of_invest * rate + amount_of_invest
        print (f"year {i+1}: ${amount_of_invest:.2f}")                  
        i=+1

print("\nRoczna stopa zwrotu wynosi: \n")
invest(amount, rate, years)         