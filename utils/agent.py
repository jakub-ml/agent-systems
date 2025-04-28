from utils.motion import move
from utils.map import Map
from utils.infection import agent_status

import random 

class Agent():
    def __init__(self):
        self.agent_id = None
        self.x = None
        self.y = None
        self.age = None
        self.status = None
        self.schedule = None
        self.home_id = None
        self.work_id = None
        self.location = None

    def make_move(self, agent, map, hour, free_beds):
        self.x, self.y = move(agent, map, hour, free_beds)
        self.location = map.get_location_from_cords(self.x, self.y)

    def get_age(self):
        self.age = random.choice(["child", "adult", "elder"])

    def get_status(self, agent, map, count_status, infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance):
        self.location = map.get_location_from_cords(agent.x, agent.y)
        if count_status!={}:
            self.status = agent_status(agent, map, self.location, count_status[self.location]['sick'], infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance)
        else:
            self.status = agent_status(agent, map, self.location, 1, infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance) # jeśli dodam początkową liczbe chorych trzeba to usunąć
# def agent_status(agent, map, location, n_sick, infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance):

    def get_schedule(self):
        if self.age == "child":
            self.schedule = {0: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            1: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            2: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            3: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            4: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
                            5: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
                            6: {"home": 85, "school": 10, "work": 0, "shop":0, "outside": 5, "hospital": 0},
                            7: {"home": 30, "school": 20, "work": 0, "shop":20, "outside": 30, "hospital": 0},
                            8: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            9: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            10: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            11: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            12: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            13: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
                            14: {"home": 10, "school": 60, "work": 0, "shop":15, "outside": 15, "hospital": 0},
                            15: {"home": 20, "school": 40, "work": 0, "shop":15, "outside": 25, "hospital": 0},
                            16: {"home": 25, "school": 10, "work": 0, "shop":10, "outside": 55, "hospital": 0},
                            17: {"home": 20, "school": 0, "work": 0, "shop":15, "outside": 65, "hospital": 0},
                            18: {"home": 20, "school": 0, "work": 0, "shop":15, "outside": 65, "hospital": 0},
                            19: {"home": 40, "school": 0, "work": 0, "shop":15, "outside": 45, "hospital": 0},
                            20: {"home": 55, "school": 0, "work": 0, "shop":10, "outside": 35, "hospital": 0},
                            21: {"home": 75, "school": 0, "work": 0, "shop":0, "outside": 25, "hospital": 0},
                            22: {"home": 90, "school": 0, "work": 0, "shop":0, "outside": 10, "hospital": 0},
                            23: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0}}
                
        elif self.age == "adult":
            self.schedule = {0: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            1: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            2: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            3: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            4: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
                            5: {"home": 95, "school": 0, "work": 5, "shop":0, "outside": 5, "hospital": 0},
                            6: {"home": 75, "school": 0, "work": 20, "shop":0, "outside": 5, "hospital": 0},
                            7: {"home": 30, "school": 0, "work": 40, "shop":0, "outside": 30, "hospital": 0},
                            8: {"home": 10, "school": 0, "work": 80, "shop":5, "outside": 5, "hospital": 0},
                            9: {"home": 5, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            10: {"home": 5, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            11: {"home": 5, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            12: {"home": 5, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            13: {"home": 5, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            14: {"home": 10, "school": 0, "work": 90, "shop":5, "outside": 0, "hospital": 0},
                            15: {"home": 10, "school": 0, "work": 50, "shop":25, "outside": 15, "hospital": 0},
                            16: {"home": 25, "school": 0, "work": 20, "shop":35, "outside": 20, "hospital": 0},
                            17: {"home": 60, "school": 0, "work": 5, "shop":15, "outside": 20, "hospital": 0},
                            18: {"home": 65, "school": 0, "work": 0, "shop":15, "outside": 15, "hospital": 0},
                            19: {"home": 70, "school": 0, "work": 0, "shop":10, "outside": 15, "hospital": 0},
                            20: {"home": 80, "school": 0, "work": 0, "shop":10, "outside": 10, "hospital": 0},
                            21: {"home": 90, "school": 0, "work": 0, "shop":0, "outside": 10, "hospital": 0},
                            22: {"home": 90, "school": 0, "work": 0, "shop":0, "outside": 10, "hospital": 0},
                            23: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0}}
       
        elif self.age == "elder":
            self.schedule = {0: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            1: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            2: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            3: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            4: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            5: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            6: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            7: {"home": 80, "school": 0, "work": 0, "shop":10, "outside": 10, "hospital": 0},
                            8: {"home": 70, "school": 0, "work": 0, "shop":15, "outside": 15, "hospital": 0},
                            9: {"home": 60, "school": 0, "work": 0, "shop":20, "outside": 20, "hospital": 0},
                            10: {"home": 60, "school": 0, "work": 0, "shop":15, "outside": 25, "hospital": 0},
                            11: {"home": 60, "school": 0, "work": 0, "shop":15, "outside": 25, "hospital": 0},
                            12: {"home": 50, "school": 0, "work": 0, "shop":20, "outside": 30, "hospital": 0},
                            13: {"home": 40, "school": 0, "work": 0, "shop":20, "outside": 40, "hospital": 0},
                            14: {"home": 40, "school": 0, "work": 0, "shop":15, "outside": 45, "hospital": 0},
                            15: {"home": 40, "school": 0, "work": 0, "shop":15, "outside": 45, "hospital": 0},
                            16: {"home": 55, "school": 0, "work": 0, "shop":10, "outside": 35, "hospital": 0},
                            17: {"home": 60, "school": 0, "work": 0, "shop":15, "outside": 25, "hospital": 0},
                            18: {"home": 60, "school": 0, "work": 0, "shop":15, "outside": 25, "hospital": 0},
                            19: {"home": 70, "school": 0, "work": 0, "shop":10, "outside": 20, "hospital": 0},
                            20: {"home": 85, "school": 0, "work": 0, "shop":5, "outside": 10, "hospital": 0},
                            21: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
                            22: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0},
                            23: {"home": 100, "school": 0, "work": 0, "shop":0, "outside": 0, "hospital": 0}}
        
    def get_home_id(self):
        self.home_id = random.randint(1,6)

    def get_work_id(self):
        if self.age == "adult":
            self.work_id = random.randint(0,1)
        else:
            self.work_id = None


# from utils.map import Map
# import numpy as np

# agent = Agent()
# agent.get_schedule()
# agent.home_id=1
# agent.work_id=1



# m=np.ones((100, 100))
# map = Map(m)
# hour = 12




# # map_prob = move(agent, map, hour)
#         # population[i].make_move(population[i], map, 0)
# agent.x, agent.y=22,33
# agent.get_status(map, agent.x, agent.y)
# print(agent.status)
# # print(map_prob)