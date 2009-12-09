import re, string
from network import *
from ctypes import *


class Action:
    level = 0
    name = ""
    id = ""
    prerequisites = []
    def __init__(self, lvl=0):
        self.level = lvl
    def __str__(self):
        return "%d" % self.level
    def do(self, state):
        print "Done"
        

class Research(Action):
    def update(self, text):
        regex = r'<a href="infos\.php\?gid=%s">%s</a> \( Stufe (\d+) \)<br>' % (self.id, self.name)
        temp = re.findall(regex, text )[:1]
        if len(temp) == 0:
            self.level = 0
        else:
            temp = re.sub(r'\.', '', temp[0])
            self.level = string.atoi(temp)
    def do(self, state):
        for i in range(len(self.prerequisites)):
            if state[self.prerequisites[i].name].level < self.prerequisites[i].level:
                self.prerequisites[i].do(state)
                print "Built %s to satisfy prerequisites" % self.prerequisites[i].name
                return True
        opener.open(url + 'buildings.php?mode=research&cmd=search&tech=' + self.id)
        print "Researching {0:s} to {1:n}".format(self.name, self.level + 1)
        return True

class Building(Action):
    def update(self, text):
        regex = r'<a href="infos\.php\?gid=%s">%s</a> \(Stufe (\d+)\)<br>' % (self.id, self.name)
        temp = re.findall(regex, text )[:1]
        if len(temp) == 0:
            self.level = 0
        else:
            temp = re.sub(r'\.', '', temp[0])
            self.level = string.atoi(temp)
    def do(self, state):
        for i in range(len(self.prerequisites)):
            if state[self.prerequisites[i].name].level < self.prerequisites[i].level:
                self.prerequisites[i].do(state)
                print "Built %s to satisfy prerequisites" % self.prerequisites[i].name
                return True
        opener.open(url + 'buildings.php?cmd=insert&building=' + self.id)
        print "Built {0:s} to {1:n}".format(self.name, self.level + 1)
        return True
 

class ResearchLab(Building):
    name = "Forschungslabor"
    id = "31"
    
class EnergyTechnology(Research):
    name = "Energietechnik"
    id = "113"
    prerequisites = [ ResearchLab(1) ]
    
class Espionage(Research):
    name = "Spionagetechnik"
    id = "106"
    prerequisites = [ ResearchLab(3) ]
 
class Computer(Research):
    name = "Computertechnik"
    id = "108"
    prerequisites = [ ResearchLab(1) ]
 
class Weapons(Research):
    name = "Waffentechnik"
    id = "109"
    prerequisites = [ ResearchLab(4) ]
 
class Shielding(Research):
    name = "Schildtechnik"
    id = "110"
    prerequisites = [ ResearchLab(6), EnergyTechnology(3) ]
 
class Armour(Research):
    name = "Raumschiffpanzerung"
    id = "111"
    prerequisites = [ ResearchLab(2) ]
 

 
class Hyperspace(Research):
    name = "Hyperraumtechnik"
    id = "114"
    prerequisites = [ ResearchLab(7), EnergyTechnology(5), Shielding(5) ]
 
class CombustionDrive(Research):
    name = "Verbrennungstriebwerk"
    id = "115"
    prerequisites = [ ResearchLab(1), EnergyTechnology(1) ]
 
class ImpulseDrive(Research):
    name = "Impulstriebwerk"
    id = "117"
    prerequisites = [ ResearchLab(2), EnergyTechnology(1) ]
 
class HyperspaceDrive(Research):
    name = "Hyperraumantrieb"
    id = "118"
    prerequisites = [ ResearchLab(7), Hyperspace(3) ]
 
class Laser(Research):
    name = "Lasertechnik"
    id = "120"
    prerequisites = [ ResearchLab(1), EnergyTechnology(2) ]
 
class Ion(Research):
    name = "Ionentechnik"
    id = "121"
    prerequisites = [ ResearchLab(4), Laser(5), EnergyTechnology(4) ]
 
class Plasma(Research):
    name = "Plasmatechnik"
    id = "122"
    prerequisites = [ ResearchLab(5), Ion(5), Laser(10), EnergyTechnology(8) ]
 
class IntergalacticResearchNetwork(Research):
    name = "Intergalaktisches Forschungsnetzwerk"
    id = "123"
    prerequisites = [ ResearchLab(10), Hyperspace(8), Computer(8) ]
    
class Expedition(Research):
    name = "Expeditionstechnik"
    id = "124"
    prerequisites = [ ResearchLab(3), ImpulseDrive(3), Computer(4) ]
 
class Graviton(Research):
    name = "Gravitonforschung"
    id = "1"
    prerequisites = [ ResearchLab(12) ]
    
    
class MetalMine(Building):
    name = "Metallmine"
    id = "1"

class CrystalMine(Building):
    name = "Kristallmine"
    id = "2"

class DeuteriumSynthesizer(Building):
    name = "Deuteriumsynthetisierer"
    id = "3"

class SolarPlant(Building):
    name = "Solarkraftwerk"
    id = "4"

class FusionReactor(Building):
    name = "Atomkraftwerk"
    id = "12"
    prerequisites = [ DeuteriumSynthesizer(5), EnergyTechnology(3) ]

class RoboticsFactory(Building):
    name = "Roboterfabrik"
    id = "14"

class NaniteFactory(Building):
    name = "Nanitenfabrik"
    id = "15"
    prerequisites = [ RoboticsFactory(10), Computer(10) ]

class Shipyard(Building):
    name = "Raumschiffwerft"
    id = "21"
    prerequisites = [ RoboticsFactory(2) ]

class MetalStorage(Building):
    name = "Metallspeicher"
    id = "22"

class CrystalStorage(Building):
    name = "Kristallspeicher"
    id = "23"

class DeuteriumTank(Building):
    name = "Deuteriumtank"
    id = "24"


class Terraformer(Building):
    name = "Terraformer"
    id = "33"
    prerequisites = [ NaniteFactory(1), EnergyTechnology(12) ]

class AllianceDepot(Building):
    name = "Allianzdepot"
    id = "34"

class MissileSilo(Building):
    name = "Raketensilo"
    id = "44"
    
def getBuildings():
    buildings = {
                'Metallmine': MetalMine(), 
                'Kristallmine': CrystalMine(), 
                'Deuteriumsynthetisierer': DeuteriumSynthesizer(), 
                'Solarkraftwerk': SolarPlant(), 
                'Atomkraftwerk': FusionReactor(),
                'Roboterfabrik': RoboticsFactory(),
                'Nanitenfabrik': NaniteFactory(),
                'Raumschiffwert': Shipyard(),
                'Metallspeicher': MetalStorage(),
                'Kristallspeicher': CrystalStorage(),
                'Deuteriumtank': DeuteriumTank(),
                'Forschungslabor': ResearchLab(),
                'Terraformer': Terraformer(),
                'Allianzdepot': AllianceDepot(),
                'Raketensilo': MissileSilo()
                }
    return buildings

def getResearch():
    research = {
                'Spionagetechnik': Espionage(),
                'Computertechnik': Computer(),
                'Waffentechnik': Weapons(),
                'Schildtechnik': Shielding(),
                'Raumschiffpanzerung': Armour(),
                'Energietechnik': EnergyTechnology(),
                'Hyperraumtechnik': Hyperspace(),
                'Verbrennungstriebwerk': CombustionDrive(),
                'Impulstriebwerk': ImpulseDrive(),
                'Hyperraumantrieb': HyperspaceDrive(),
                'Lasertechnik': Laser(),
                'Ionentechnik': Ion(),
                'Plasmatechnik': Plasma(),
                'Intergalaktisches Forschungsnetzwerk': IntergalacticResearchNetwork(),
                'Expeditionstechnik': Expedition(),
                'Gravitonforschung': Graviton()
                }
    return research
