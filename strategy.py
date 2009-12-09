from action import Action

class Target:
    action = Action()
    
class Strategy:
    targets = []


class Condition:
    cond = '' # like: "SomeBuilding > ( SomeOtherBuilding - 10 )"