def validate_triangle_side(x):

    if (x.isnumeric()):

        if (int(x)>0):

            return True

        else:

            print ("Invalid input")

            return False

    else:

        print ("Invalid input")

        return False

def check_pythagorean_triple(x,y,z):

    if (float(x)**2 + float(y)**2 == float(z)**2):

        print ("Pythagorean Triple found")

        return None

    if (float(x)**2 + float(z)**2 == float(y)**2):

        print ("Pythagorean Triple found")

        return None
    
    if (float(y)**2 + float(z)**2 == float(x)**2):

        print ("Pythagorean Triple found")

        return None

    print ("Pythagorean Triple not found")

    return None
    

while True:

    side_a = input ("Insert size of side A: ")

    if (validate_triangle_side(side_a) == True):

        break

while True:

    side_b = input ("Insert size of side B: ")

    if (validate_triangle_side(side_b) == True):

        break

while True:

    side_c = input ("Insert size of side C: ")

    if (validate_triangle_side(side_c) == True):

        break

check_pythagorean_triple(side_a,side_b,side_c)
