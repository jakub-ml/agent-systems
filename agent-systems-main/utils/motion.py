import numpy as np
import matplotlib.pyplot as plt

def move(agent, map, hour):
    # Houses
    if agent.home_id == 1:
        map.house_1  = map.house_1 * agent.schedule[hour]['home'] / map.house_1.sum()
        map.house_2, map.house_3, map.house_4, map.house_5, map.house_6 = 0, 0, 0, 0, 0
    elif agent.home_id == 2:
        map.house_2  = map.house_2 * agent.schedule[hour]['home'] / map.house_2.sum()
        map.house_1, map.house_3, map.house_4, map.house_5, map.house_6 = 0, 0, 0, 0, 0
    elif agent.home_id == 3:
        map.house_3  = map.house_3 * agent.schedule[hour]['home'] / map.house_3.sum()
        map.house_1, map.house_2, map.house_4, map.house_5, map.house_6 = 0, 0, 0, 0, 0
    elif agent.home_id == 4:
        map.house_4  = map.house_4 * agent.schedule[hour]['home'] / map.house_4.sum()
        map.house_1, map.house_2, map.house_3, map.house_5, map.house_6 = 0, 0, 0, 0, 0
    elif agent.home_id == 5:
        map.house_5  = map.house_5 * agent.schedule[hour]['home'] / map.house_5.sum()
        map.house_1, map.house_2, map.house_3, map.house_4, map.house_6 = 0, 0, 0, 0, 0
    elif agent.home_id == 6:
        map.house_6  = map.house_6 * agent.schedule[hour]['home'] / map.house_6.sum()
        map.house_1, map.house_2, map.house_3, map.house_4, map.house_5 = 0, 0, 0, 0, 0
        
    # School
    map.school = map.school * agent.schedule[hour]['school'] / map.school.sum()

    # Work
    if agent.work_id == 1:
        map.work_1  = map.work_1 * agent.schedule[hour]['work'] / map.work_1.sum()
        map.work_2= map.work_2 * 0
    elif agent.work_id == 2:
        map.work_2  = map.work_2 * agent.schedule[hour]['work'] / map.work_2.sum()
        map.work_1=map.work_1*0
    else:
        map.work_1=map.work_1*0
        map.work_2=map.work_2*0

    # Shop
    map.shop = map.shop * agent.schedule[hour]['shop'] / map.shop.sum()

    # Hospital
    map.hospital  = map.hospital * agent.schedule[hour]['hospital'] / map.hospital.sum()

    # Outsite
    map.outsite = map.outsite * agent.schedule[hour]['outside'] / map.outsite.sum()

    new_map=map.update_map()
    # plt.imshow(new_map)
    # plt.show(block=False)   # Uruchamiamy okno z wykresem w trybie "nieblokującym"
    # plt.pause(0.1)          # Przerwa na 0.5 sekundy, w tym czasie okno jest widoczne
    # plt.close()             # Zamykamy okno z wykresem

    normalized_matrix = new_map / new_map.sum()
    flat_prob_matrix = normalized_matrix.flatten()
    index = np.random.choice(len(flat_prob_matrix), p=flat_prob_matrix)
    # result_matrix = np.zeros_like(flat_prob_matrix)
    # final_matrix = result_matrix.reshape(new_map.shape)

    # x, y = index%100, index//100
    x, y = 10*(index%100), 10*(index//100)
    return x, y

