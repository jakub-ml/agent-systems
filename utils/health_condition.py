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

    # Hospital
    map_prob[30:80,3:30] = map_prob[30:80,3:30] / map_prob[30:80,3:30].sum()

    # Work
    map_prob[45:55,60:90] = map_prob[45:55,60:90] / map_prob[45:55,60:90].sum()
    map_prob[85:95,40:80] = map_prob[85:95,40:80] / map_prob[85:95,40:80].sum()

    # Outsite
    map_prob[map_prob==1.0] = map_prob[map_prob==1.0] / map_prob[map_prob==1.0].sum()

    # TODO zrobione jest prawdopodobieństwo na podstawie wielkości pomieszczenia w którym ktoś się znajduje, teraz  trzeba zrobić ta że prawdopodobieństwo przelicza się na podstawie
    #  preferencji agenta oraz godziny w czasie dnia a następnie wyświetlone na mapie jako kolejne ruchy

    normalized_matrix = map_prob / map_prob.sum()
    flat_prob_matrix = normalized_matrix.flatten()
    index = np.random.choice(len(flat_prob_matrix), p=flat_prob_matrix)
    result_matrix = np.zeros_like(flat_prob_matrix)
    final_matrix = result_matrix.reshape(map_prob.shape)

    x, y = 10*(index%100), 10*(index//100)
    return x, y