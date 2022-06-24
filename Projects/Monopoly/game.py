import random
import math
import time

# import util

# simulation settings
nPlayers = 4
nMoves = 1000
nSimulations = 1000
seed = ""  # "" for none
shufflePlayers = True
realTime = False # Allow step by step execution via space/enter key
num_threads = 8

# some game rules
settingStartingMoney = 1500
settingsSalary = 200
settingsLuxuryTax = 100
settingsPropertyTax = 200
settingJailFine = 50
settingHouseLimit = 32
settingHotelLimit = 12
settingsAllowUnEqualDevelopment = False
settingsBankruptcyAlwaysGoesToBank = False

# players behaviour settings
behaveUnspendableCash = 0
behaveUnmortgageCoeff = 3
behaveDoTrade = True
behaveDoThreeWayTrade = True
behaveBuildCheapest = False
behaveBuildRandom = False





