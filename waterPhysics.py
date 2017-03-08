DRAG_COEFFICIENT_SPHERE = 0.47

# mols^-1 kilograms^-1
GAS_CONSTANT = 8.3144598

# Degrees Celsius
ROOM_TEMPERATURE = 20

# g/cm^3
WATER_DENSITY = 1

# Grams/Mol
MOLAR_MASS_AIR = 29

# Pascals
AIR_PRESSURE_SEA_LEVEL = 101325

def paToBar(pascals):
    return pascals * 0.00001

def barToPa(bar):
    return bar * 100000

def pascalsToPsi(pascals):
    return pascals * 0.000145038

def psiToPa(psi):
    return psi * 6894.76

def m3ToL(m3):
    return m3 * 1000

def lToM3(litres):
    return litres / 1000

def m3ToFt3(m3):
    return m3 * 35.3147

def ft3ToM3(ft3):
    return ft3 * 0.0283168

def gToKg(g):
    return g * 1000

def kgToG(kg):
    return g / 1000

def gToLbs(g):
    return g * 0.00220462

def lbsToG(lbs):
    return lbs * 453.592
# True if the object has water physics
def hasWaterPhysics(obj):
    return 'waterPhysics' in obj and obj['waterPhysics'] == True

def pressure(gravity, density, depth):
    return gravity * density * depth

def drag(density, velocity, area, dragCoefficient):
    # drag equation
    # dragForce = 1/2 * fluidDensity * velocity^2 * referenceArea * dragCoefficient
    return 1.6 * density * velocity ** 2 * area * dragCoefficient

def submerged(obj, fluid):
    fluidZ = fluid.position[2]
    objectZ = obj.position[2]
    return (objectZ <= fluidZ)

