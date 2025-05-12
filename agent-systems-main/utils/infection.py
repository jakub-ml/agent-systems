import random
import numpy as np
from utils.map import Map

def agent_status(agent, map, location, n_sick, infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance):
    
    # infectionChance=infectionChance/100
    # deathChance=deathChance/100
    # recoverOutsideChance=recoverOutsideChance/100
    # recoverHospitalChance=recoverHospitalChance/100

    # print(location)
    if agent.status == "healthy":
        print(infectionChance / map.house_1.sum(), map.house_1.sum(), random.random())
        if n_sick == 1:
            if location=="house_1" and infectionChance / map.house_1.sum() > random.random():
                agent.status = "sick"
            elif location=="house_2" and infectionChance / map.house_2.sum() > random.random():
                agent.status = "sick"
            elif location=="house_3" and infectionChance / map.house_3.sum() > random.random():
                agent.status = "sick"
            elif location=="house_4" and infectionChance / map.house_4.sum() > random.random():
                agent.status = "sick"
            elif location=="house_5" and infectionChance / map.house_5.sum() > random.random():
                agent.status = "sick"
            elif location=="house_6" and infectionChance / map.house_6.sum() > random.random():
                agent.status = "sick"
            elif location=="school" and infectionChance / map.school.sum() > random.random():
                agent.status = "sick"
            elif location=="work_1" and infectionChance / map.work_1.sum() > random.random():
                agent.status = "sick"
            elif location=="work_2" and infectionChance / map.work_2.sum() > random.random():
                agent.status = "sick"
            elif location=="shop" and infectionChance / map.shop.sum() > random.random():
                agent.status = "sick"
            elif location=="outsite" and infectionChance / map.outsite.sum() > random.random():
                agent.status = "sick"

        if n_sick > 1:
            if location=="house_1" and np.log(n_sick + 3) * infectionChance / map.work_1.sum() > random.random():
                agent.status = "sick"
            elif location=="house_2" and np.log(n_sick + 3) * infectionChance / map.house_2.sum() > random.random():
                agent.status = "sick"
            elif location=="house_3" and np.log(n_sick + 3) * infectionChance / map.house_3.sum() > random.random():
                agent.status = "sick"
            elif location=="house_4" and np.log(n_sick + 3) * infectionChance / map.house_4.sum() > random.random():
                agent.status = "sick"
            elif location=="house_5" and np.log(n_sick + 3) * infectionChance / map.house_5.sum() > random.random():
                agent.status = "sick"
            elif location=="house_6" and np.log(n_sick + 3) * infectionChance / map.house_6.sum() > random.random():
                agent.status = "sick"
            elif location=="school" and np.log(n_sick + 3) * infectionChance / map.school.sum() > random.random():
                agent.status = "sick"
            elif location=="work_1" and np.log(n_sick + 3) * infectionChance / map.work_1.sum() > random.random():
                agent.status = "sick"
            elif location=="work_2" and np.log(n_sick + 3) * infectionChance / map.work_2.sum() > random.random():
                agent.status = "sick"
            elif location=="shop" and np.log(n_sick + 3) * infectionChance / map.shop.sum() > random.random():
                agent.status = "sick"
            elif location=="outsite" and np.log(n_sick + 3) * infectionChance / map.outsite.sum() > random.random():
                agent.status = "sick"

    elif agent.status == "sick":
        if location=="hospital":
            if recoverHospitalChance > random.random():
                agent.status = "healthy"
        else:
            elements = ["healthy", "sick", "dead"]
            weights = [recoverOutsideChance, 100-recoverOutsideChance-deathChance, deathChance]
            agent.status = random.choices(elements, weights=weights, k=1)[0]
            
    return agent.status
            
def count_status_fun(location, status, count_status):
    if location not in count_status.keys():
        count_status[location] = {"healthy": 0, "sick": 0, "dead": 0}
    count_status[location][status] += 1
    return count_status


        #dodać całą reszte i wywołać

        #         return "school"
        # elif map_prob[x, y] == 8:
        #     return "work_1"
        # elif map_prob[x, y] == 9:
        #     return "work_2"
        # elif map_prob[x, y] == 10:
        #     return "shop"
        # elif map_prob[x, y] == 11:
        #     return "hospital"
        # elif map_prob[x, y] == 12:
        #     return "outsite"



# from agent import Agent
# agent = Agent()
# agent.get_schedule()
# agent.home_id=1
# agent.work_id=1
# agent.status = "sick"


# m=np.ones((100, 100))
# map = Map(m)

# for _ in range(10):
#     # agent.status = "healthy"
#     agent_status(agent, "house_1", 1, 100, 30, 10, 50)
# agent, location, n_sick, infectionChance, deathChance, recoverOutsideChance, recoverHospitalChance