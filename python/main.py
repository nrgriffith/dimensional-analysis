# The goal of this project is to aid the user in dimensional analysis.
# Dimensional analysis is commonly used as a "sanity check" for physical
# science problems (chemistry, physics, etc.) Some of the more advanced
# topics can have units that aren't as obviously interconnected.
# This program will provide a comparison of units by simplifying each
# unit into its SI base units

# SI base unit names
SI_BASE = {
		2: ("m", "meter"),
		3: ("kg", "kilogram"),
		5: ("s", "second"),
		7: ("a", "ampere"),
		11: ("k", "kelvin"),
		13: ("mol", "mole"),
		17: ("cd", "candela")
		}

class CompoundUnit():
	def getName(self):
		return self.name

	def getSymbol(self):
		return self.symbol

	def getValue(self):
		return self.value

	def getK(self):
		return self.k

	def __init__(self, name, symbol, value, k):
		self.name = name
		self.symbol = symbol
		self.value = value
		self.k = k

# Variables
unitCombined = 1
unitFactors = []

# Get input
def get_raw_input(unitList = []):
	unit = raw_input("Enter a number: ")
	if int(unit) == 0:
		print "Error."
	else:
		unitList.append(int(unit))

# Combine units, returns a multiple of the units
def combine_units(unitList = []):
	combinedUnit = 1
	for n in unitList:
		combinedUnit *= n
	return combinedUnit

# Checks to see if a unit is a base unit
def is_base_unit(unit):
	for n in SI_BASE:
		if unit % n == 0 and unit / n != 1:
			return False
	else:
		return True

# Reset the unitFactors list
def reset_factors(rfactors = []):
	del rfactors[:]

# Returns a list of prime factors
def factor_units(unit, factors = []):
	reset_factors(factors)
	for n in SI_BASE:
		while unit % n == 0 and unit / n != 1:
			unit/=n
			factors.append(n)
	factors.append(unit)

# Print the unit combination in SI base units
def print_in_base_units(factors = []):
	print "SI Base Units: ",
	for n in SI_BASE:
		if factors.count(n) != 0:
			print "(",
			print SI_BASE[n][0],
			print ")^%d" %factors.count(n),
	print "\n"

# Initial testing...

get_raw_input(unitFactors)
get_raw_input(unitFactors)
get_raw_input(unitFactors)
get_raw_input(unitFactors)
get_raw_input(unitFactors)
get_raw_input(unitFactors)

unitCombined = combine_units(unitFactors)

factor_units(unitCombined, unitFactors)

print "Combined unit number: %d" %(unitCombined)

print "Factors:",

print unitFactors

print_in_base_units(unitFactors)
