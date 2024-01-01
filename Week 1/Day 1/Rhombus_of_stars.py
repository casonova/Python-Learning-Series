def rhombus_stars(number):
    for row in range(number * 2 -1):
        space = abs(number - row -1)
        stars = number - space
        print(' ' * space + '* ' *stars)
        
num = int(input("Enter number of sides: "))
rhombus_stars(num)        