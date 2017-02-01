import bge

# mols^-1 kilograms^-1
def GAS_CONSTANT = 8.3144598

# Degrees Celsius
def ROOM_TEMPERATURE = 20

# Grams/Mol
def MOLAR_MASS_AIR = 29

# Pascals
def AIR_PRESSURE_SEA_LEVEL = 101325

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

def lToM3(litres)
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

class AirCylinder:
    # maxPressure: pascals
    # volume: meters cubed
    # emptyMass: grams
    def __init__(self, maxPressure, volume, emptyMass):
        self.volume = volume
        self.emptyMass = emptyMass
        self.moles = 0.0

    # Pressure in pascals
    # temperature: degrees celsius
    def pressure(self, temperature):
        return (self.moles * GAS_CONSTANT * temperature) / self.volume

    # Mass in grams
    def mass(self):
        return (self.moles * MOLAR_MASS_AIR) + emptyMass

    # Fills the cylinder to capacity at the given temperature
    # temperature: degrees celsius
    def fill(self, temperature):
        self.moles = (maxPressure * volume) / (GAS_CONSTANT * temperature)

    def fill(self):
        self.fill(ROOM_TEMPERATURE)

    # empties the cylinder
    def empty(self):
        self.moes = 0.0

# Generic Cylinder
# 3000 psi maximum pressure
# 6 cubic foot volume
# 2.6 pounds empty
genericCylinder = AirCylinder(psiToPa(3000), ftToM3(6), lbsToG(2.6))

class BCD:
    # minVolume: meters cubed
    # maxVolume: meters cubed
    # maxPressure: pascals
    # emptyMass: grams
    def __init__(self, minVolume, maxVolume, emptyMass):
        self.minVolume = minVolume
        self.maxVolume = maxVolume
        self.emptyMass = emptyMass
        self.moles = 0.0

    # Volume in meters cubed
    # pressure: pascals
    # temperature: degrees celsius
    def volume(self, pressure, temperature):
        return ((self.moles * GAS_CONSTANT * temperature) / pressure) + self.minVolume

    # Mass in grams
    def mass(self):
        return (self.moles * MOLAR_MASS_AIR) + self.emptyMass

    def molesToCapacity(self, pressure, temperature):
        return ((pressure * volume) / (GAS_CONSTANT * temperature)) - self.moles

    # Add's air to the BCD
    # Returns amount of air released due to overfilling in moles
    # moles: air to add in moles
    # pressure: pascals
    # temperature: degrees celsius
    def addAir(self, moles, pressure, temperature):
       remainingCapacity = self.molesToCapacity(pressure, temperature)
       if (moles > remainingCapacity):
           self.moles += remainingCapacity
           return moles - remainingCapacity
       else:
           self.moles += moles
           return 0.0

    # removes air from bcd
    # moles: air to remove in moles
    def removeAir(self, moles):
        newAir = self.moles - moles
        if (newAir < 0):
            self.moles = 0
        else:
            self.moles = newAir

    # fills BCD to capacity at this pressure and temperature
    def fill(self, pressure, temperature):
        self.moles += self.molesToCapacity(self, pressure, temperature)

    # empties all air out of the BCD
    def empty(self):
        self.moles = 0

# Generic BCD
# 0.01 m3 empty
# 0.3 m3 full
# 500 grams empty
genericBcd = BCD(0.1, 0.4, 500)

def equip(self, bcd, airCylinder, weight):
    self.bcd = bcd
    self.airCylinder = airCylinder
    self.weight = weight

bge.types.KX_GameObject.equip = equip

