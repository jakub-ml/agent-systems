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
    simulation_data["customInput"] = str(data["customInput"])
    simulation_data["longSlider"] = int(data["longSlider"])
    simulation_data["customReduce"] = data["customReduce"]
    simulation_data["tempSlider"] = float(data["tempSlider"])
    simulation_data["customOutput"] = str(data["customOutput"])

    simulation_data['save_data'] = {}


    # Inicjalizacja agentów (losowe położenie w obszarze 1000x1000, wszyscy zdrowi)
    global population
    population = [Agent() for _ in range(simulation_data["population"])]
    global map
    global next_day
    global count_status
    global first_send
    first_send = True
    count_status={}
    next_day=True
    sick_id = random.sample(range(0, int(simulation_data["population"])), int(simulation_data["initialSick"]))
    curr_hospital_beds=0
    for i in range(simulation_data["population"]):
        map = Map(np.ones((100, 100)))
        population[i].get_age()
        population[i].status = "healthy"
        population[i].get_schedule()        
        population[i].get_home_id()
        population[i].get_work_id()
        population[i].agent_id = i
        population[i].make_move(population[i], map, 0, simulation_data["hospitalBeds"] > curr_hospital_beds)
        if i in sick_id:
            population[i].status='sick'
    simulation_data["agents"] = []
    for i in range(simulation_data["population"]):

        simulation_data["agents"].append({
            "agent_id": population[i].agent_id,
            "x": population[i].x+5,
            "y": population[i].y+5,
            "age": population[i].age,
            "home_id": population[i].home_id,
            "work_id": population[i].work_id,
            "location": population[i].location,
            "status": population[i].status,
            "schedule": population[i].schedule[0]
        })
    simulation_data['save_data'][f"day: {1}, hour: {0}"] = simulation_data["agents"]


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
        global count_status
        global next_day
        curr_hospital_beds = 0
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
                population[i].make_move(population[i], map, hour, simulation_data["hospitalBeds"]>curr_hospital_beds)
                # limit for hospital bed
                if population[i].location == "hospital":
                    curr_hospital_beds+=1

            else:
                count_status = count_status_fun(population[i].location, population[i].status, count_status)
                population[i].get_status(population[i], map, count_status, simulation_data["infectionChance"], simulation_data["deathChance"], simulation_data["recoverOutsideChance"], simulation_data["recoverHospitalChance"])

                # count earning rate
                if population[i].location in ["work_1", "work_2"] and population[i].age == "adult" and population[i].status!="dead":
                    simulation_data["earnings"] += simulation_data["income"]


            simulation_data["agents"].append({
                "agent_id": population[i].agent_id,
                "x": population[i].x+5,
                "y": population[i].y+5,
                "age": population[i].age,
                "home_id": population[i].home_id,
                "work_id": population[i].work_id,
                "location": population[i].location,
                "status": population[i].status,
                "schedule": population[i].schedule[hour]
            })

        # Przeliczenie statystyk (healthy, sick, dead)
        healthy_count = sum(1 for a in simulation_data["agents"] if a["status"] == "healthy")
        sick_count = sum(1 for a in simulation_data["agents"] if a["status"] == "sick")
        dead_count = sum(1 for a in simulation_data["agents"] if a["status"] == "dead")
        
        simulation_data["healthy"] = healthy_count
        simulation_data["sick"] = sick_count
        simulation_data["dead"] = dead_count
        simulation_data["hour"] = hour
        simulation_data["day"] = day

        simulation_data['save_data'][f"day: {day}, hour: {hour}"] = simulation_data["agents"]

        if simulation_data["longSlider"]==day and hour == 0:
            with open(f'simulated_annealing\data\{simulation_data["customInput"]}.json', 'w') as f:
                json.dump(simulation_data['save_data'], f, indent=4)

            with open(f'simulated_annealing\data\{simulation_data["customInput"]}_metadata.json', 'w') as f:
                json.dump(simulation_data, f, indent=4)
            
            with open(f'simulated_annealing\data\{"temporary_file"}.txt', 'w', encoding='utf-8') as f:
                f.write(simulation_data["customInput"])

            import evolution_alg

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


loaded_scenario = None
scenario_keys = []
current_index = 0

@app.route("/load", methods=["POST"])
def load_scenario():
    global loaded_scenario, scenario_keys, current_index, earnings
    earnings = 0

    data = request.get_json()
    custom_output = data.get("customOutput")

    if not custom_output:
        return jsonify({"error": "Brak nazwy pliku"}), 400

    try:
        with open(f'simulated_annealing/data/{custom_output}.json', 'r') as f:
            loaded_scenario = json.load(f)

        scenario_keys = list(loaded_scenario.keys())
        current_index = 0

        return jsonify({"status": "loaded", "totalSteps": len(scenario_keys)}), 200

    except Exception as e:
        return jsonify({"error": "Nie udało się wczytać pliku"}), 500


@app.route("/next", methods=["GET"])
def get_next_step():
    global loaded_scenario, scenario_keys, current_index, earnings

    if loaded_scenario is None or current_index >= len(scenario_keys)-1:
        return jsonify({"finished": True}), 200

    key = scenario_keys[current_index]
    agents_data = loaded_scenario[key]

    healthy = sum(1 for agent in agents_data if agent["status"] == "healthy")
    sick = sum(1 for agent in agents_data if agent["status"] == "sick")
    dead = sum(1 for agent in agents_data if agent["status"] == "dead")
    for agent in agents_data:
        if agent.get("location") in ["work_1", "work_2"] and agent.get("age") == "adult" and agent.get("status") != "dead":
            earnings += 100  # UWAGA: tutaj musisz dać ile wynosi "income" z symulacji

    current_index += 1
    print("AA")
    if current_index!=1:
        return jsonify({
            "agents": agents_data,
            "healthy": healthy,
            "sick": sick,
            "dead": dead,
            "earnings": earnings,
            "step": current_index-1
        }), 200


if __name__ == "__main__":
    app.run(debug=True)
