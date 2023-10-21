import math
print('lets do some physics exercises')
constant = input('For gravitation problems, choose 1. For electrostatic problems, choose 2: ')
if constant == '1' :
    constant = 6.67 * 10 ** -11
    fieldsymbol = 'g'
    fieldmodule = '/g/'
    fieldunit = 'N/kg'
    print('Enter the mass of the planet in the particle 1 and the mass of the satelite in the particle 2')
    orbitqstn = input('If you want to do a gravitation problem, press 1: ')
    if orbitqstn == '1' :
        orbitradius = input ('enter the radius of the orbit: ')
        order_of_magnitude = input('enter the order of magnitud of the radius (e.g. 10**3 enter 3): ')
        orbitradius = float(orbitradius) * 10 ** float(order_of_magnitude)
else:
    constant = 9 * 10 ** 9
    fieldsymbol = 'E'
    fieldmodule = '/E/'
    fieldunit = 'N/C'
print('lets add some particles to our plane')
part1 = input ('enter the value of particle 1: ')
order_of_magnitude = input('enter the order of magnitud of the particle (e.g. 10**3 enter 3): ')
part1 = float(part1) * 10 ** float(order_of_magnitude)
if orbitqstn != '1' :
    position1x = input('enter the x coordinate of the particle: ')
    position1y = input('enter the y coordinate of the particle: ')
    position1x = float(position1x)
    position1y = float(position1y)
part2 = input ('enter the value of particle 2: ')
order_of_magnitude = input('enter the order of magnitud of the particle (e.g. 10**3 enter 3): ')
part2 = float(part2) * float(order_of_magnitude)
if orbitqstn != '1' :
    position2x = input('enter the x coordinate of the particle: ')
    position2y = input('enter the y coordinate of the particle: ')
    position2x = float(position2x)
    position2y = float(position2y)
    pointpositionx = input('enter the x coordinate of the point: ')
    pointpositiony = input('enter the y coordinate of the point: ')
    pointpositionx = float(pointpositionx)
    pointpositiony = float(pointpositiony)
    radius1 = math.sqrt((position1x - pointpositionx) ** 2 + (position1y - pointpositiony) ** 2)
    radius2 = math.sqrt((position2x - pointpositionx) ** 2 + (position2y - pointpositiony) ** 2)
    radius3 = math.sqrt((position2x - position1x) ** 2 + (position2y - position1y) ** 2)
def calcfield(constant, part1, position1x, position1y, part2, position2x, position2y, radius1, radius2) :
    field1x = (constant * part1 / (radius1 ** 2)) * ((pointpositionx - position1x) / radius1)
    field1y = (constant * part1 / (radius1 ** 2)) * ((pointpositiony - position1y) / radius1)
    field2x = (constant * part2 / (radius2 ** 2)) * ((pointpositionx - position2x) / radius2)
    field2y = (constant * part2 / (radius2 ** 2)) * ((pointpositiony - position2y) / radius2)
    fieldtotalx = field1x + field2x
    fieldtotaly = field1y + field2y
    fieldmodule = math.sqrt(fieldtotalx ** 2 + fieldtotaly ** 2)
    return fieldtotalx, fieldtotaly, fieldmodule
def calcenergy (constant, part1, part2, position1x, position1y, position2x, position2y) :
    ep = (constant * part1 * part2) / math.sqrt((position2x - position1x) ** 2 + (position2y - position1y) ** 2)
    return ep
def calcpotential (constant, part1, part2, radius1, radius2) :
    potential = (constant * part1 / (radius1)) + (constant * part2 / (radius2))
    return potential
def calcorbitalvelocity(constant, part1, orbitradius) :
    orbitalvelocity = math.sqrt((constant * part1 / orbitradius))
    return orbitalvelocity
def calcescapevelocity(constant , part1, orbitradius) :
    escapevelocity = math.sqrt(2* constant * part1 / orbitradius)
    return escapevelocity
def calcforce1(constant, part1, part2, position1x, position1y, position2x, position2y, radius3) :
    forcex = constant * part1 * part2 / ((position2x - position1x) / radius3)
    forcey = constant * part1 * part2 / ((position2y - position1y) / radius3)
    forcemodule = math.sqrt(forcex ** 2 + forcey ** 2)
    return forcex, forcey, forcemodule
#poner resulatdos en notación cientifica
if orbitqstn != '1' :
    print('F = ', calcforce1(constant, part1, part2, position1x, position1y, position2x, position2y, radius3), 'N')
    print(fieldsymbol, '=', calcfield(constant, part1, position1x, position1y, part2, position2x, position2y, radius1, radius2), fieldunit, fieldmodule, fieldunit)
    print('Ep = ', calcenergy(constant, part1, part2, position1x, position1y, position2x, position2y), 'J')
    print('V = ', calcpotential (constant, part1, part2, radius1, radius2), 'V')
if orbitqstn == '1' :
    print('Vo = ', calcorbitalvelocity(constant, part1, orbitradius), 'm/s')
    print('Vo = ', calcescapevelocity(constant, part1, orbitradius), 'm/s')