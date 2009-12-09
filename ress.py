import re, string

class Ressource:
    """merly the amount of the ressource and a method to obtain it"""
    amount = 0
    def __str__(self):
        return "{0:n}".format(self.amount)
    def update(self, text):
        self.amount = 0

class Metal(Ressource):
    def update(self, text):
        temp = re.findall(r'<td class="header" align="center" width="150"><font>(<font color="#ff0000">)?(\d+(\.\d\d\d)*)(</font>)?</font></td>', text )[:1]
        temp = re.sub(r'\.', '', temp[0][1])
        self.amount = long(temp)

class Crystal(Ressource):
    def update(self, text):
        temp = re.findall(r'<td class="header" align="center" width="150"><font>(<font color="#ff0000">)?(\d+(\.\d\d\d)*)(</font>)?</font></td>', text )[1:2]
        temp = re.sub(r'\.', '', temp[0][1])
        self.amount = long(temp)

class Deuterium(Ressource):
    def update(self, text):
        temp = re.findall(r'<td class="header" align="center" width="150"><font>(<font color="#ff0000">)?(\d+(\.\d\d\d)*)(</font>)?</font></td>', text )[2:3]
        temp = re.sub(r'\.', '', temp[0][1])
        self.amount = long(temp)

class Energy(Ressource):
    maximum = 0
    def __str__(self):
        return "{0:n} / {1:n}".format(self.amount, self.maximum)
    def update(self, text):
        result = re.findall(r'<td class="header" align="center" width="150"><font>(<font color="#ff0000">)?(<font color="#00ff00">)?(-?\d+(\.\d+)*)(</font>)?</font></td>', text )[3:4]
        cur = re.sub(r'\.', '', result[0][2])
        self.amount = long(cur)
        result = re.findall(r'<td class="header" align="center" width="150">(<font color="#ff0000">)?(<font color="#00ff00">)?(-?\d+(\.\d\d\d)*)</font></td>', text )
        max = re.sub(r'\.', '', result[0][2])
        self.maximum = long(max)