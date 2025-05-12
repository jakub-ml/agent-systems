import numpy as np
import matplotlib.pyplot as plt

def move(map_size=100):
    map_prob=np.ones((map_size, map_size))

    # Houses
    map_prob[3:15,3:15]  = map_prob[3:15,3:15] / map_prob[3:15,3:15].sum()
    map_prob[3:15,18:30] = map_prob[3:15,18:30] / map_prob[3:15,18:30].sum()
    map_prob[3:15,33:45] = map_prob[3:15,33:45] / map_prob[3:15,33:45].sum()
    map_prob[3:15,48:60] = map_prob[3:15,48:60] / map_prob[3:15,48:60].sum()
    map_prob[3:15,63:75] = map_prob[3:15,63:75] / map_prob[3:15,63:75].sum()
    map_prob[3:15,78:90] = map_prob[3:15,78:90] / map_prob[3:15,78:90].sum()

    # School
    map_prob[80:95,3:35] = map_prob[80:95,3:35] / map_prob[80:95,3:35].sum()

    # Work
    map_prob[50:65,60:90] = map_prob[50:65,60:90] / map_prob[50:65,60:90].sum()
    map_prob[80:95,60:90] = map_prob[80:95,60:90] / map_prob[80:95,60:90].sum()

    # Shop
    map_prob[50:65,30:50] = map_prob[50:65,30:50] / map_prob[50:65,30:50].sum()

    # Hospital
    map_prob[30:55,3:20] = map_prob[30:55,3:20] / map_prob[30:55,3:20].sum()

    # Outsite
    map_prob[map_prob==1.0] = map_prob[map_prob==1.0] / map_prob[map_prob==1.0].sum()

    plt.imshow(map_prob)
    plt.show()
    #                             5: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0},

move(map_size=100)
