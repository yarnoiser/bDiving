import bge
from waterPhysics import *

class AirCylinder:
    # maxPressure: pascals
    # volume: meters cubed
    # emptyMass: grams
    def __init__(self, maxPressure, volume, emptyMass):
        self.maxPressure = maxPressure
        self.volume = volume
        self.emptyMass = emptyMass
        self.moles = 0.0

    # Pressure in pascals
    # temperature: degrees celsius
    def pressure(self, temperature):
        return (self.moles * GAS_CONSTANT * temperature) / self.volume

    # Mass in grams
    def mass(self):
        return (self.moles * MOLAR_MASS_AIR) + self.emptyMass

    # Fills the cylinder to capacity at the given temperature
    # temperature: degrees celsius
    def fill(self, temperature):
        self.moles = (self.maxPressure * self.volume) / (GAS_CONSTANT * temperature)

    def fillDefualt(self):
        self.fill(ROOM_TEMPERATURE)

    # empties the cylinder
    def empty(self):
        self.moes = 0.0

    # removes air from the cylinder
    # moles: air to remove in moles
    def removeAir(self, moles):
        newAir = self.moles - moles
        if (newAir < 0):
            molesLeft = self.moles
            self.moles = 0
            return molesLeft
        else:
            self.moles = newAir
            return moles

# Generic Cylinder
# Based off of "Aluminum S80"
# 3000 psi maximum pressure
# 0.39 cubic foot volume
# 35 pounds empty
def genericCylinder():
    return AirCylinder(psiToPa(3000), ft3ToM3(0.39), lbsToKg(35))

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
        return ((pressure * self.maxVolume) / (GAS_CONSTANT * temperature)) - self.moles

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
            molesLeft = self.moles
            self.moles = 0
            return molesLeft
        else:
            self.moles = newAir
            moles

    # fills BCD to capacity at this pressure and temperature
    def fill(self, pressure, temperature):
        self.moles += self.molesToCapacity(pressure, temperature)

    # empties all air out of the BCD
    def empty(self):
        self.moles = 0

# Generic BCD
# 0.01 m3 empty
# 0.3 m3 full
# 500 grams empty
def genericBcd():
    return BCD(0, 0.02, 0)

def equip(diver, bcd, airCylinder, weight):
    diver['bcd'] = bcd
    bcd.fill(AIR_PRESSURE_SEA_LEVEL, ROOM_TEMPERATURE)
    diver['airCylinder'] = airCylinder
    airCylinder.fill(ROOM_TEMPERATURE)
    diver['weight'] = weight

