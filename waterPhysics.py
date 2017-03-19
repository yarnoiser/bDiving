DRAG_COEFFICIENT_SPHERE = 0.47

# mols^-1 kilograms^-1
GAS_CONSTANT = 8.3144598

def cToK(c):
    return c + 273.15

def kToC(k):
    return k - 273.15

# Degrees Celsius
ROOM_TEMPERATURE = cToK(20)

# g/cm^3
WATER_DENSITY = 1

# Grams/Mol
MOLAR_MASS_AIR = 0.029

# Pascals
AIR_PRESSURE_SEA_LEVEL = 101325

def paToBar(pascals):
    return pascals / 100000

def barToPa(bar):
    return bar * 100000

def paToPsi(pascals):
    return pascals / 6894.76

def psiToPa(psi):
    return psi * 6894.76

def m3ToL(m3):
    return m3 * 1000

def lToM3(litres):
    return litres / 1000

def m3ToFt3(m3):
    return m3 * 35.3147

def ft3ToM3(ft3):
    return ft3 / 35.3147

def kgToLbs(kg):
    return kg * 2.20462

def lbsToKg(lbs):
    return lbs / 2.20462

# True if the object has water physics
def hasWaterPhysics(obj):
    return 'waterPhysics' in obj and obj['waterPhysics'] == True

def pressure(gravity, density, depth):
    return (gravity * density * depth) + AIR_PRESSURE_SEA_LEVEL

def drag(density, velocity, area, dragCoefficient):
    # drag equation
    # dragForce = 1/2 * fluidDensity * velocity^2 * referenceArea * dragCoefficient
    return 1.6 * density * velocity ** 2 * area * dragCoefficient

def submerged(obj, fluid):
    fluidZ = fluid.position[2]
    objectZ = obj.position[2]
    return (objectZ <= fluidZ)

def depth(obj, fluid):
    return fluid.worldPosition[2] - obj.worldPosition[2]