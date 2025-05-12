import numpy as np

class Map():

    def __init__(self, map_prob):
        self.count_status = {}
        
        self.size = map_prob.shape[0]
        # Houses
        self.house_1 = map_prob[3:15,3:15] 
        self.house_2 = map_prob[3:15,18:30]
        self.house_3 = map_prob[3:15,33:45]
        self.house_4 = map_prob[3:15,48:60]
        self.house_5 = map_prob[3:15,63:75]
        self.house_6 = map_prob[3:15,78:90]

        # School
        self.school = map_prob[80:95,3:35]

        # Work
        self.work_1 = map_prob[50:65,60:90]
        self.work_2 = map_prob[80:95,60:90]

        # Shop
        self.shop = map_prob[50:65,30:50]

        # Hospital
        self.hospital = map_prob[30:55,3:20]

        # Outsite
        self.mask = np.ones((self.size, self.size), dtype=bool)
        self.mask[3:15,  3:15] = False
        self.mask[3:15, 18:30] = False
        self.mask[3:15, 33:45] = False
        self.mask[3:15, 48:60] = False
        self.mask[3:15, 63:75] = False
        self.mask[3:15, 78:90] = False

        self.mask[80:95, 3:35] = False
        self.mask[50:65,60:90] = False
        self.mask[80:95,60:90] = False
        self.mask[50:65,30:50] = False
        self.mask[30:55,  3:20] = False

        # other = np.zeros_like(map_prob, dtype=int)
        self.outsite = map_prob[self.mask]


    def update_map(self):
        map_prob = np.zeros((self.size, self.size))
        # map_prob = np.full((self.size, self.size), -1, dtype=int)

        map_prob[3:15,3:15]  = self.house_1
        map_prob[3:15,18:30] = self.house_2
        map_prob[3:15,33:45] = self.house_3
        map_prob[3:15,48:60] = self.house_4
        map_prob[3:15,63:75] = self.house_5
        map_prob[3:15,78:90] = self.house_6


        map_prob[80:95,3:35] = self.school

        # Work
        map_prob[50:65,60:90] = self.work_1
        map_prob[80:95,60:90] = self.work_1

        # Shop
        map_prob[50:65,30:50] = self.shop

        # Hospital
        map_prob[30:55,3:20] = self.hospital

        # Outsite
        map_prob[self.mask] = self.outsite
        return map_prob
    
    def get_location_from_cords(self, x, y):
        map_prob = np.zeros((self.size, self.size))
        map_prob[3:15,3:15]  = 1
        map_prob[3:15,18:30] = 2
        map_prob[3:15,33:45] = 3
        map_prob[3:15,48:60] = 4
        map_prob[3:15,63:75] = 5
        map_prob[3:15,78:90] = 6

        map_prob[80:95,3:35] = 7 # school

        # Work
        map_prob[50:65,60:90] = 8 # work_1
        map_prob[80:95,60:90] = 9 # work_1

        # Shop
        map_prob[50:65,30:50] = 10 # shop

        # Hospital
        map_prob[30:55,3:20] = 11 # hospital

        # Outsite
        map_prob[self.mask] = 12 # outsite

        x, y = int(x/10), int(y/10)
        if map_prob[y, x] == 1:
            return "house_1"
        elif map_prob[y, x] == 2:
            return "house_2"
        elif map_prob[y, x] == 3:
            return "house_3"
        elif map_prob[y, x] == 4:
            return "house_4"
        elif map_prob[y, x] == 5:
            return "house_5"
        elif map_prob[y, x] == 6:
            return "house_6"
        elif map_prob[y, x] == 7:
            return "school"
        elif map_prob[y, x] == 8:
            return "work_1"
        elif map_prob[y, x] == 9:
            return "work_2"
        elif map_prob[y, x] == 10:
            return "shop"
        elif map_prob[y, x] == 11:
            return "hospital"
        elif map_prob[y, x] == 12:
            return "outsite"

# mapa=np.zeros((100, 100))
# map=Map(mapa)
# # map.create_map(mapa)
# print(map.house_1)
# map.update_map()

                            # 23: {"home": 95, "school": 0, "work": 0, "shop":0, "outside": 5, "hospital": 0}}
