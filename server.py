from flask import Flask, request, jsonify, send_from_directory
import random
import os
import numpy as np
from utils.motion import move
import time
from utils.agent import Agent
from utils.map import Map
from utils.infection import count_status_fun
app = Flask(__name__)

# Struktura do przechowywania danych symulacji
simulation_data = {
    "population": 100,
    "hospitalBeds": 50,
    "income": 100,
    "infectionChance": 20,
    "deathChance": 5,
    "recoverOutsideChance": 50,
    "recoverHospitalChance": 80,
    "agents": [],
    "tick": 0,
    "healthy": 0,
    "sick": 0,
    "dead": 0,
    "earnings": 0
}

# Serwowanie pliku index.html (strona główna)
@app.route("/")
def serve_index():
    return send_from_directory("", "index.html")  # zakładamy, że index.html leży w tym samym katalogu co server.py

# Serwowanie pliku script.js
@app.route("/script.js")
def serve_script():
    return send_from_directory("", "script.js")

# Endpoint do zainicjowania / restartu symulacji
@app.route("/start", methods=["POST"])
def start_simulation():
    data = request.get_json()
    
    # Odczytanie parametrów i zapis do simulation_data
    simulation_data["population"] = int(data["population"])
    simulation_data["hospitalBeds"] = int(data["hospitalBeds"])
    simulation_data["income"] = int(data["income"])
    simulation_data["infectionChance"] = float(data["infectionChance"])
    simulation_data["deathChance"] = float(data["deathChance"])
    simulation_data["recoverOutsideChance"] = float(data["recoverOutsideChance"])
    simulation_data["recoverHospitalChance"] = float(data["recoverHospitalChance"])
    simulation_data["initialSick"] = float(data["initialSick"])
    

    # Inicjalizacja agentów (losowe położenie w obszarze 1000x1000, wszyscy zdrowi)
    global population
    population = [Agent() for _ in range(simulation_data["population"])]
    global map
    global next_day
    global count_status
    count_status={}
    next_day=True
    sick_id = random.sample(range(0, int(simulation_data["population"])), int(simulation_data["initialSick"]))

    for i in range(simulation_data["population"]):
        map = Map(np.ones((100, 100)))
        population[i].get_age()
        population[i].status = "healthy"
        population[i].get_schedule()        
        population[i].get_home_id()
        population[i].get_work_id()
        population[i].make_move(population[i], map, 0)
        if i in sick_id:
            population[i].status='sick'
            # population[i].location="house_3"#map.get_location_from_cords(population[i].x, population[i].y)
            # count_status[population[i].location] = {"healthy": 0, "sick": 1, "dead": 0}

            # population[i].location = map.get_location_from_cords(population[i].x, population[i].y)
            # count_status = count_status_fun(population[i].location, population[i].status, count_status)
            # population[i].get_status(population[i], map, count_status, simulation_data["infectionChance"], simulation_data["deathChance"], simulation_data["recoverOutsideChance"], simulation_data["recoverHospitalChance"])

            # population[i].get_status(population[i], map, {}, simulation_data["infectionChance"], simulation_data["deathChance"], simulation_data["recoverOutsideChance"], simulation_data["recoverHospitalChance"])
    simulation_data["agents"] = []
    for i in range(simulation_data["population"]):

        simulation_data["agents"].append({
            "x": population[i].x+5,
            "y": population[i].y+5,
            "status": "healthy"
        })

    # Reset licznika czasu i statystyk
    simulation_data["tick"] = 0
    simulation_data["healthy"] = simulation_data["population"]
    simulation_data["sick"] = 0
    simulation_data["dead"] = 0
    simulation_data["earnings"] = 0

    return jsonify({"status": "started"}), 200

# Endpoint do zwracania aktualnych danych o symulacji
@app.route("/data", methods=["GET"])
def get_data():
    if "population" in globals():
        # Przykładowa bardzo uproszczona logika symulacji (możesz ją rozbudować wg własnych potrzeb)
        # simulation_data["tick"] += 1
        global count_status
        global next_day
        if next_day == True:
            simulation_data["tick"] += 1
            next_day=False
        else:
            next_day=True

        hour = int(simulation_data["tick"]%24)
        day = int(simulation_data["tick"]//24)+1

        simulation_data["agents"] = []
        count_status={}
        for i in range(simulation_data["population"]):
            map = Map(np.ones((100, 100)))
            if not next_day:
                population[i].make_move(population[i], map, hour)
            else:
                count_status = count_status_fun(population[i].location, population[i].status, count_status)
                population[i].get_status(population[i], map, count_status, simulation_data["infectionChance"], simulation_data["deathChance"], simulation_data["recoverOutsideChance"], simulation_data["recoverHospitalChance"])
        
                if population[i].location in ["work_1", "work_2"] and population[i].age == "adult" and population[i].status!="dead":
                    simulation_data["earnings"] += simulation_data["income"]

            simulation_data["agents"].append({
                "x": population[i].x+5,
                "y": population[i].y+5,
                "status": population[i].status
            })


        # Przykładowe losowe zarażanie i wyzdrowienia
        # for agent in simulation_data["agents"]:
        #     if agent["status"] == "healthy":
        #         # Losowa szansa na zachorowanie (mocno zmniejszona przez '/ 10.0' - tylko przykład)
        #         if random.random() < (simulation_data["infectionChance"] / 100.0 / 10.0):
        #             agent["status"] = "sick"
        #     elif agent["status"] == "sick":
        #         # Losowa szansa na śmierć
        #         if random.random() < (simulation_data["deathChance"] / 100.0 / 10.0):
        #             agent["status"] = "dead"
        #         # Albo losowa szansa na wyzdrowienie
        #         elif random.random() < (simulation_data["recoverOutsideChance"] / 100.0 / 10.0):
        #             agent["status"] = "healthy"

        # Przeliczenie statystyk (healthy, sick, dead)
        healthy_count = sum(1 for a in simulation_data["agents"] if a["status"] == "healthy")
        sick_count = sum(1 for a in simulation_data["agents"] if a["status"] == "sick")
        dead_count = sum(1 for a in simulation_data["agents"] if a["status"] == "dead")

        simulation_data["healthy"] = healthy_count
        simulation_data["sick"] = sick_count
        simulation_data["dead"] = dead_count
        simulation_data["hour"] = hour
        simulation_data["day"] = day
        # Zwracamy dane w formacie JSON
        return jsonify({
            "agents": simulation_data["agents"],
            "healthy": healthy_count,
            "sick": sick_count,
            "dead": dead_count,
            "earnings": simulation_data["earnings"],
            "tick": simulation_data["tick"],
            "hour": simulation_data["hour"],
            "day": simulation_data["day"]
        }), 200

if __name__ == "__main__":
    app.run(debug=True)
