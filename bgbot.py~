#! /usr/bin/env python

import re, string, time
from action import *
from ress import *
from network import *
from strategy import *

class Empire:
    planets = []
    research = {}
    
    def __init__(self):
        self.research = getResearch()

    def update(self):
        result = opener.open(url + 'buildings.php').read()
        temp = re.findall(r'value="\?cp=(\d+)&amp;mode=&amp;re=0">([^<]+)</option>', result )
        self.planets = []
        for planet in temp:
            self.planets.append( Planet(planet[1], planet[0]) )
        for planet in self.planets:
            planet.name = re.sub(r'&nbsp;', ' ', temp[0][1])
        
        for planet in self.planets:
            planet.update()
        
        opener.open(url + 'buildings.php?cp=1&mode=&re=0' )
        research_text = opener.open(url + 'buildings.php?mode=research').read()
        for name, research in self.research.iteritems():
            research.update(research_text)
        


    def build(self):
        highest = 0
        buildingState = {}
        for planet in self.planets:
            if planet.buildings['Forschungslabor'].level > highest:
                highest = planet.buildings['Forschungslabor'].level
                buildingState = planet.buildings
            planet.build(self.research)
        if highest == 0:
            buildingState = getBuildings()

        state = {}
        for name, search in self.research.iteritems():
            state[name] = search
        for name, building in buildingState.iteritems():
            state[name] = building
        opener.open(url + 'buildings.php?cp=1&mode=&re=0' )
        result = opener.open(url + 'buildings.php?mode=research').read()
        if string.find(result, 'Abbrechen') == -1:
            lowest = 1000
            nextResearch = self.research['Schildtechnik']
            for name, research in self.research.iteritems():
                if research.level < lowest:
                    if string.find(result, research.name) != -1:
                        if research.name != "Gravitonforschung":
                            nextResearch = research
                            lowest = research.level
            nextResearch.do(state)

    def __str__(self):
        answer = "My empire:\n"
        for planet in self.planets:
            answer += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n%s" % planet
        answer += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        answer += "Current research:\n"
        for name, research in self.research.iteritems():
            answer += "  %s - Level %s\n" % (name, research)
        answer += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        return answer


class Planet:
    name = ""
    id = ""
    buildings = {}
    ressources = { 'Metal': Metal(), 'Crystal': Crystal(), 'Deuterium': Deuterium(), 'Energy': Energy() }
    
    
    def __init__(self, nm, i):
        self.name = nm
        self.id = i
        self.buildings = getBuildings()
    
    def update(self):
        building_text = opener.open(url + 'buildings.php?cp=%s&mode=&re=0' % self.id ).read()
        for name, res in self.ressources.iteritems():
            res.update(building_text)
        for name, build in self.buildings.iteritems():
            build.update(building_text)
       
    
    def __str__(self):
        answer = "Planet %s with id %s \n" % (self.name, self.id)
        answer += "Current ressources:\n"
        for name, res in self.ressources.iteritems():
            answer += "  %s %s\n" % (res, name)
        answer += "Current buildings:\n"
        for name, building in self.buildings.iteritems():
            answer += "  %s - Level %s\n" % (name, building)
        return answer
    
    def build(self, researchState):
        state = {}
        for name, building in self.buildings.iteritems():
            state[name] = building
        for name, research in researchState.iteritems():
            state[name] = research
        result = opener.open(url + 'buildings.php').read()
        opener.open(url + 'buildings.php?cp=%s&mode=&re=0' % self.id )
        if self.ressources['Energy'].amount < 0:
            if self.buildings['Raumschiffwert'].level < 1:
                if string.find(result, 'Raumschiffwerft 1') == -1:
                    self.buildings['Raumschiffwert'].do(state)
            else:
                result = opener.open(url + 'buildings.php?mode=fleet').read()
                temp = re.findall(r"b  = new Array\('([^']*)'(,'[^']*')+\);", result )[:1]
                NoSolarSatsInQue = True
                if len(temp) != 0:
                    for some in temp[0]:
                        if string.find(some, 'Solarsatellit') != -1:
                            NoSolarSatsInQue = False
                            break
                if NoSolarSatsInQue:
                    numOfSats = min(self.ressources['Crystal'].amount / 2000, self.ressources['Deuterium'].amount / 500, (self.ressources['Energy'].amount - 100) / -100)
                    print "Building %d Solar Satellites\n" % numOfSats
                    opener.open(url + 'buildings.php?mode=fleet', 'fmenge[212]=%d' % numOfSats)
       
        if string.find(result, 'Abbrechen') == -1:
            if self.buildings['Deuteriumsynthetisierer'].level < ( self.buildings['Kristallmine'].level - 1):
                self.buildings['Deuteriumsynthetisierer'].do(state)
            elif self.buildings['Kristallmine'].level < (self.buildings['Metallmine'].level - 2):
                self.buildings['Kristallmine'].do(state)
            elif self.buildings['Metallspeicher'].level < (self.buildings['Metallmine'].level / 2):
                self.buildings['Metallspeicher'].do(state)
            elif self.buildings['Kristallspeicher'].level < (self.buildings['Kristallmine'].level / 2):
                self.buildings['Kristallspeicher'].do(state)
            elif self.buildings['Deuteriumtank'].level < (self.buildings['Deuteriumsynthetisierer'].level / 2):
                self.buildings['Deuteriumtank'].do(state)
            elif self.buildings['Roboterfabrik'].level < (self.buildings['Metallmine'].level - 10):
                self.buildings['Roboterfabrik'].do(state)
            elif self.buildings['Forschungslabor'].level < (self.buildings['Metallmine'].level - 10):
                self.buildings['Forschungslabor'].do(state)
            elif self.buildings['Raumschiffwert'].level < (self.buildings['Metallmine'].level - 10):
                self.buildings['Raumschiffwert'].do(state)
            else:
                print "building stupid"
                self.buildings['Metallmine'].do(state)
        
            
        
        

print "Welcome to my browser game bot"

opener.open(url + 'login.php', 'uni_id=1&v=2&is_utf8=0&username=Mononofu&password=alucard&submitInput=Login')
empire = Empire()
empire.update()
print empire
while True:
    empire.update()
    empire.build()
    time.sleep(1)

print planet
cj.save()

