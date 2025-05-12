import random 
a = random.sample(range(0, 101), 4)

print(a)



# import numpy as np
# import matplotlib.pyplot as plt

# def move(map_size=100):
#     map_prob=np.ones((map_size, map_size))

#     # Houses
#     map_prob[3:15,3:15]  = map_prob[3:15,3:15] / map_prob[3:15,3:15].sum()
#     map_prob[3:15,18:30] = map_prob[3:15,18:30] / map_prob[3:15,18:30].sum()
#     map_prob[3:15,33:45] = map_prob[3:15,33:45] / map_prob[3:15,33:45].sum()
#     map_prob[3:15,48:60] = map_prob[3:15,48:60] / map_prob[3:15,48:60].sum()
#     map_prob[3:15,63:75] = map_prob[3:15,63:75] / map_prob[3:15,63:75].sum()
#     map_prob[3:15,78:90] = map_prob[3:15,78:90] / map_prob[3:15,78:90].sum()

#     # Hospital
#     map_prob[30:80,3:30] = map_prob[30:80,3:30] / map_prob[30:80,3:30].sum()

#     # Work
#     map_prob[45:55,60:90] = map_prob[45:55,60:90] / map_prob[45:55,60:90].sum()
#     map_prob[85:95,40:80] = map_prob[85:95,40:80] / map_prob[85:95,40:80].sum()

#     # Outsite
#     map_prob[map_prob==1.0] = map_prob[map_prob==1.0] / map_prob[map_prob==1.0].sum()

#     plt.imshow(map_prob)
#     plt.show()
#     # TODO zrobione jest prawdopodobieństwo na podstawie wielkości pomieszczenia w którym ktoś się znajduje, teraz  trzeba zrobić ta że prawdopodobieństwo przelicza się na podstawie
#     #  preferencji agenta oraz godziny w czasie dnia a następnie wyświetlone na mapie jako kolejne ruchy

#     normalized_matrix = map_prob / map_prob.sum()
#     flat_prob_matrix = normalized_matrix.flatten()
#     index = np.random.choice(len(flat_prob_matrix), p=flat_prob_matrix)
#     result_matrix = np.zeros_like(flat_prob_matrix)
#     final_matrix = result_matrix.reshape(map_prob.shape)
    
# move(map_size=100)
# # def move(map_size, schedule):
# #     map_prob=np.ones((map_size, map_size))
# #                             # 1: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},


# #     schedule[0]["home"]


# #     # Houses
# #     map_prob[3:15,3:15]  = map_prob[3:15,3:15] / map_prob[3:15,3:15].sum()
# #     map_prob[3:15,18:30] = map_prob[3:15,18:30] / map_prob[3:15,18:30].sum()
# #     map_prob[3:15,33:45] = map_prob[3:15,33:45] / map_prob[3:15,33:45].sum()
# #     map_prob[3:15,48:60] = map_prob[3:15,48:60] / map_prob[3:15,48:60].sum()
# #     map_prob[3:15,63:75] = map_prob[3:15,63:75] / map_prob[3:15,63:75].sum()
# #     map_prob[3:15,78:90] = map_prob[3:15,78:90] / map_prob[3:15,78:90].sum()

# #     # Hospital
# #     map_prob[30:80,3:30] = map_prob[30:80,3:30] / map_prob[30:80,3:30].sum()

# #     # Work
# #     map_prob[45:55,60:90] = map_prob[45:55,60:90] / map_prob[45:55,60:90].sum()
# #     map_prob[85:95,40:80] = map_prob[85:95,40:80] / map_prob[85:95,40:80].sum()

# #     # Outsite
# #     map_prob[map_prob==1.0] = map_prob[map_prob==1.0] / map_prob[map_prob==1.0].sum()


# # # move(map_size=100)

# # schedule = {0: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             1: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             2: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             3: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             4: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             5: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             6: {"home": 85, "school": 10, "work": 0, "shop":0, "outside": 5, "hospital": 0},
# #                             7: {"home": 30, "school": 20, "work": 0, "shop":20, "outside": 30, "hospital": 0},
# #                             8: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             9: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             10: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             11: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             12: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             13: {"home": 5, "school": 85, "work": 0, "shop":5, "outside": 5, "hospital": 0},
# #                             14: {"home": 10, "school": 60, "work": 0, "shop":15, "outside": 15, "hospital": 0},
# #                             15: {"home": 20, "school": 40, "work": 0, "shop":15, "outside": 25, "hospital": 0},
# #                             16: {"home": 25, "school": 10, "work": 0, "shop":10, "outside": 55, "hospital": 0},
# #                             17: {"home": 20, "school": 0, "work": 0, "shop":15, "outside": 65, "hospital": 0},
# #                             18: {"home": 20, "school": 0, "work": 0, "shop":15, "outside": 65, "hospital": 0},
# #                             19: {"home": 40, "school": 0, "work": 0, "shop":15, "outside": 45, "hospital": 0},
# #                             20: {"home": 55, "school": 0, "work": 0, "shop":10, "outside": 35, "hospital": 0},
# #                             21: {"home": 75, "school": 0, "work": 0, "shop":0, "outside": 25, "hospital": 0},
# #                             22: {"home": 90, "school": 0, "work": 0, "shop":0, "outside": 10, "hospital": 0},
# #                             23: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0}}


# # map_size=100

# # map_prob=np.ones((map_size, map_size))
# # # map_prob[3:15,3:15]  = map_prob[3:15,3:15] / map_prob[3:15,3:15].sum()

# # # Houses
# # map_prob[3:15,3:15] = schedule[0]["home"] / map_prob[3:15,3:15].sum()
# # map_prob[3:15,3:15]  = schedule[0]["home"] / map_prob[3:15,3:15].sum()
# # map_prob[3:15,18:30] = schedule[0]["home"] / map_prob[3:15,18:30].sum()
# # map_prob[3:15,33:45] = schedule[0]["home"] / map_prob[3:15,33:45].sum()
# # map_prob[3:15,48:60] = schedule[0]["home"] / map_prob[3:15,48:60].sum()
# # map_prob[3:15,63:75] = schedule[0]["home"] / map_prob[3:15,63:75].sum()
# # map_prob[3:15,78:90] = schedule[0]["home"] / map_prob[3:15,78:90].sum()

# # # School

# # # Hospital
# # map_prob[30:80,3:30] = schedule[0]["hospital"] / map_prob[30:80,3:30].sum()

# # # Work
# # map_prob[45:55,60:90] = schedule[0]["work"] / map_prob[45:55,60:90].sum()
# # map_prob[85:95,40:80] = schedule[0]["work"] / map_prob[85:95,40:80].sum()

# # # Outsite
# # map_prob[map_prob==1.0] = schedule[0]["outside"] / map_prob[map_prob==1.0].sum()


# # plt.imshow(map_prob)
# # plt.show()

# print(201%10)