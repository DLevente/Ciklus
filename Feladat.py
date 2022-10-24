#1.Feladat: Kérjünk be 5 db egész számot és nézzük meg hogy melyik páros és páratlan.

x = 1

while x < 6:
    
    szam = int(input("Kérem a számokat:"))
    
    if szam % 2 == 0:
        print("A szám páros")
    else:
        print("A szám páratlan")
        
    x += 1
