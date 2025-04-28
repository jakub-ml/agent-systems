from flask import Flask, request, jsonify, send_from_directory
import random
import os
import numpy as np
from utils.motion import move
import time
from utils.agent import Agent
from utils.map import Map
from utils.infection import count_status_fun
import json
app = Flask(__name__)


def change_schedule(agent, random_day_hour):
    if agent.age == "child":
        lista = list(agent.schedule[random_day_hour].values())
        wybrany_indeks = random.randint(0, len(lista) - 1)
        do_przeniesienia = 30
        if lista[wybrany_indeks]>=100-do_przeniesienia or wybrany_indeks==2:
            return agent.schedule
        lista[wybrany_indeks] += do_przeniesienia
        pozostale_indeksy = [i for i in range(len(lista)) if i != wybrany_indeks]
        while do_przeniesienia > 0:
            for i in pozostale_indeksy:
                if lista[i] > 0:
                    lista[i] -= 1
                    do_przeniesienia -= 1
                    if do_przeniesienia == 0:
                        break

        agent.schedule[random_day_hour] = {"home": lista[0], "school": lista[1], "work": lista[2], "shop": lista[3], "outside": lista[4], "hospital": lista[5]}
            
    elif agent.age == "adult":
        lista = list(agent.schedule[random_day_hour].values())
        wybrany_indeks = random.randint(0, len(lista) - 1)
        do_przeniesienia = 30
        if lista[wybrany_indeks]>=100-do_przeniesienia:
            return agent.schedule
        lista[wybrany_indeks] += do_przeniesienia
        pozostale_indeksy = [i for i in range(len(lista)) if i != wybrany_indeks]
        while do_przeniesienia > 0:
            for i in pozostale_indeksy:
                if lista[i] > 0:
                    lista[i] -= 1
                    do_przeniesienia -= 1
                    if do_przeniesienia == 0:
                        break

        agent.schedule[random_day_hour] = {"home": lista[0], "school": lista[1], "work": lista[2], "shop": lista[3], "outside": lista[4], "hospital": lista[5]}
    
    elif agent.age == "elder":
        lista = list(agent.schedule[random_day_hour].values())
        wybrany_indeks = random.randint(0, len(lista) - 1)
        do_przeniesienia = 30
        if lista[wybrany_indeks]>=100-do_przeniesienia or wybrany_indeks==2 or wybrany_indeks==3:
            return agent.schedule
        lista[wybrany_indeks] += do_przeniesienia
        pozostale_indeksy = [i for i in range(len(lista)) if i != wybrany_indeks]
        while do_przeniesienia > 0:
            for i in pozostale_indeksy:
                if lista[i] > 0:
                    lista[i] -= 1
                    do_przeniesienia -= 1
                    if do_przeniesienia == 0:
                        break

        agent.schedule[random_day_hour] = {"home": lista[0], "school": lista[1], "work": lista[2], "shop": lista[3], "outside": lista[4], "hospital": lista[5]}
    return agent.schedule


with open('simulated_annealing/data/temporary_file.txt', 'r', encoding='utf-8') as f:
    file = f.read()
print(file)

# Wczytanie pliku a.json
file_path = f'simulated_annealing/data/{file}.json'
file_path_metadata = f'simulated_annealing/data/{file}_metadata.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(file_path_metadata, 'r', encoding='utf-8') as file:
    data_metadata = json.load(file)


simulation_data={}
simulation_data["population"] = int(data_metadata["population"])
simulation_data["hospitalBeds"] = int(data_metadata["hospitalBeds"])
simulation_data["income"] = int(data_metadata["income"])
simulation_data["infectionChance"] = float(data_metadata["infectionChance"])
simulation_data["deathChance"] = float(data_metadata["deathChance"])
simulation_data["recoverOutsideChance"] = float(data_metadata["recoverOutsideChance"])
simulation_data["recoverHospitalChance"] = float(data_metadata["recoverHospitalChance"])
simulation_data["initialSick"] = float(data_metadata["initialSick"])
simulation_data["customInput"] = str(data_metadata["customInput"])
simulation_data["longSlider"] = int(data_metadata["longSlider"])
simulation_data["customReduce"] = data_metadata["customReduce"]
simulation_data["tempSlider"] = float(data_metadata["tempSlider"])

def run_simulation(data):
    population = [Agent() for _ in range(simulation_data["population"])]
    curr_hospital_beds=0

    init=True
    sum_status={"healthy" : 0, "sick": 0, "dead": 0, "earnings": 0}
    count_status={}

    # Reacreate initial states
    day_hour = "day: 1, hour: 0"
    for i in range(simulation_data["population"]):
        population[i].age = data[day_hour][i]['age']
        population[i].work_id = data[day_hour][i]["work_id"]
        population[i].home_id = data[day_hour][i]["home_id"]
        population[i].agent_id = data[day_hour][i]["agent_id"]

        map = Map(np.ones((100, 100)))
        population[i].schedule = {day_hour: data[day_hour][i]["schedule"]}
        population[i].status = data[day_hour][i]["status"]
        population[i].make_move(population[i], map, day_hour, simulation_data["hospitalBeds"] > curr_hospital_beds)
        
        if population[i].status=="healthy":
            sum_status['healthy']+=1
        elif population[i].status=="sick":
            sum_status['sick']+=1
        elif population[i].status=="dead":
            sum_status['dead']+=1
        if population[i].location in ["work_1", "work_2"] and population[i].age == "adult" and population[i].status!="dead":
            sum_status["earnings"] += simulation_data["income"]


    day_l=list(data.keys())
    random_day_hour = random.choice(day_l)

    for i in range(simulation_data["population"]):
        for day_hour in day_l[day_l.index(random_day_hour):]:
            count_status={}

            map = Map(np.ones((100, 100)))
            population[i].schedule = {day_hour: data[day_hour][i]["schedule"]}
            population[i].status = data[day_l[day_l.index(day_hour)-1]][i]["status"]

            population[i].make_move(population[i], map, day_hour, simulation_data["hospitalBeds"] > curr_hospital_beds)
            if population[i].location == "hospital":
                curr_hospital_beds+=1
            count_status = count_status_fun(population[i].location, population[i].status, count_status)
            population[i].get_status(population[i], map, count_status, simulation_data["infectionChance"], simulation_data["deathChance"], simulation_data["recoverOutsideChance"], simulation_data["recoverHospitalChance"])
            population[i].schedule = change_schedule(population[i], day_hour)

            # change data
            data[day_hour][i]['status'] = population[i].status
            data[day_hour][i]["schedule"] = population[i].schedule[day_hour]
            data[day_hour][i]['x'] = population[i].x
            data[day_hour][i]['y'] = population[i].y
            data[day_hour][i]['location'] = population[i].location

            if population[i].status=="healthy":
                sum_status['healthy']+=1
            elif population[i].status=="sick":
                sum_status['sick']+=1
            elif population[i].status=="dead":
                sum_status['dead']+=1

            if population[i].location in ["work_1", "work_2"] and population[i].age == "adult" and population[i].status!="dead":
                sum_status["earnings"] += simulation_data["income"]

    reduce = simulation_data["customReduce"]
    cost = cost_function(reduce, sum_status)
    return cost, data, reduce
    

def cost_function(reduce, sum_status):
    if reduce == "max healthy":
        cost = sum_status['healthy']
    
    elif reduce =="max income":
        cost = sum_status['earnings']

    elif reduce =="min sick":
        cost = sum_status['sick']

    elif reduce =="min dead":
        cost = sum_status['dead']

    return cost

def simulated_annealing(data, end_temp=simulation_data["tempSlider"], start_temp=1):
    cost=np.inf
    temp=start_temp
    while True:
        new_cost, new_data, reduce = run_simulation(data)
        if reduce in ['max healthy', 'max income']:
            if cost < new_cost or random.random() < temp:
                cost, data = new_cost, new_data
            print(cost, temp)
            temp=temp/2

        elif reduce in ['min sick', 'min dead']:
            if cost > new_cost or random.random() < temp:
                cost, data = new_cost, new_data
            print(cost, temp)
            temp=temp/2
                
        if temp<end_temp:
            with open(f'simulated_annealing\data\{simulation_data["customInput"]}_opt.json', 'w') as f:
                json.dump(data, f, indent=4)
            break
simulated_annealing(data)

