const bgImage = new Image();
bgImage.src = "C:/Users/ADMIN/Desktop/Agent systems/python_java/background.jpg";
let playbackSpeed = 100; // Domyślnie 100 ms

// Wyświetlanie aktualnych wartości suwaków obok etykiet
function updateSliderValue(sliderId, valueId) {
    
    const slider = document.getElementById(sliderId);
    const valueSpan = document.getElementById(valueId);
    valueSpan.textContent = slider.value;  

  }
  
  function updateClock(hourValue) {
    const clockElement = document.getElementById("clock");
    if (clockElement) {
        clockElement.textContent = "Godzina: " + hourValue;
    }
  }

  function updateDay(dayValue) {
    const clockElement = document.getElementById("kalendar");
    if (clockElement) {
        clockElement.textContent = "Dzień: " + dayValue;
    }
  }

  function initSliders() {
    updateSliderValue("population", "populationValue");
    updateSliderValue("hospitalBeds", "hospitalBedsValue");
    updateSliderValue("income", "incomeValue");
    updateSliderValue("infectionChance", "infectionChanceValue");
    updateSliderValue("deathChance", "deathChanceValue");
    updateSliderValue("recoverOutsideChance", "recoverOutsideValue");
    updateSliderValue("recoverHospitalChance", "recoverHospitalValue");
    updateSliderValue("initialSick", "initialValue");
    updateSliderValue("speedSlider", "speedValue");
    updateSliderValue("longSlider", "long_save");
    updateSliderValue("tempSlider", "temp");
    
    const sliders = [
      { sliderId: "population", valueId: "populationValue" },
      { sliderId: "hospitalBeds", valueId: "hospitalBedsValue" },
      { sliderId: "income", valueId: "incomeValue" },
      { sliderId: "infectionChance", valueId: "infectionChanceValue" },
      { sliderId: "deathChance", valueId: "deathChanceValue" },
      { sliderId: "recoverOutsideChance", valueId: "recoverOutsideValue" },
      { sliderId: "recoverHospitalChance", valueId: "recoverHospitalValue" },
      { sliderId: "initialSick", valueId: "initialValue" },
      { sliderId: "speedSlider", valueId: "speedValue" },
      { sliderId: "longSlider", valueId: "long_save" },
      { sliderId: "tempSlider", valueId: "temp" }

    ];
  
    sliders.forEach(obj => {
      document.getElementById(obj.sliderId).addEventListener("input", () => {
        updateSliderValue(obj.sliderId, obj.valueId);
      });
    });

  }
  
  function drawGrid(ctx, width, height, cellSize) {
    // Ustaw styl linii (np. delikatny szary)
    ctx.strokeStyle = "rgba(0, 0, 0, 0.1)";
    ctx.lineWidth = 1;
  
    // Rysuj pionowe linie co cellSize pikseli
    for (let x = 0; x <= width; x += cellSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
  
    // Rysuj poziome linie co cellSize pikseli
    for (let y = 0; y <= height; y += cellSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }
  }
  
  // Inicjalizacja wykresu za pomocą Chart.js
  let statsChart;
  function initChart() {
    const ctx = document.getElementById("statsChart").getContext("2d");
    statsChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: [], // Tutaj można wstawiać np. numer iteracji (tick) lub czas
        datasets: [
          {
            label: "Healthy",
            data: [],
            borderColor: "green",
            fill: false
          },
          {
            label: "Sick",
            data: [],
            borderColor: "red",
            fill: false
          },
          {
            label: "Dead",
            data: [],
            borderColor: "black",
            fill: false
          },
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
  
  // Funkcja do aktualizacji wykresu na podstawie nowych danych
  function updateChartData(healthy, sick, dead, earnings, timeLabel) {
    statsChart.data.labels.push(timeLabel);
    statsChart.data.datasets[0].data.push(healthy);
    statsChart.data.datasets[1].data.push(sick);
    statsChart.data.datasets[2].data.push(dead);
    // statsChart.data.datasets[3].data.push(earnings);
    statsChart.update();
  }

    // Inicjalizacja wykresu za pomocą Chart.js
    let statsChart2;
    function initChart2() {
      const ctx = document.getElementById("statsChart2").getContext("2d");
      statsChart2 = new Chart(ctx, {
        type: "line",
        data: {
          labels: [], // Tutaj można wstawiać np. numer iteracji (tick) lub czas
          datasets: [
            {
              label: "Earnings",
              data: [],
              borderColor: "blue",
              fill: false
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
    
    // Funkcja do aktualizacji wykresu na podstawie nowych danych
    function updateChartData2(healthy, sick, dead, earnings, timeLabel) {
      statsChart2.data.labels.push(timeLabel);
      // statsChart.data.datasets[0].data.push(healthy);
      // statsChart.data.datasets[1].data.push(sick);
      // statsChart.data.datasets[2].data.push(dead);
      statsChart2.data.datasets[0].data.push(earnings);
      statsChart2.update();
    }
  
  // Rysowanie mapy miasta (szachownicy 1000x1000) i agentów
  function drawMap(agents) {
    const canvas = document.getElementById("cityMap");
    const ctx = canvas.getContext("2d");
  
    // Wyczyść całe płótno
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    // RYSUJEMY SIATKĘ (przed rysowaniem agentów)
    drawGrid(ctx, canvas.width, canvas.height, 10);
  
    // Rysowanie agentów...
    agents.forEach(agent => {
      if (agent.status === "healthy") {
        ctx.fillStyle = "green";
        ctx.beginPath();
        ctx.arc(agent.x, agent.y, 5, 0, 5 * Math.PI);
        ctx.fill();
      } else if (agent.status === "sick") {
        ctx.fillStyle = "red";
        ctx.beginPath();
        ctx.arc(agent.x, agent.y, 5, 0, 5 * Math.PI);
        ctx.fill();
      } else if (agent.status === "dead") {
        ctx.strokeStyle = "black";
        ctx.beginPath();
        ctx.moveTo(agent.x - 2, agent.y - 2);
        ctx.lineTo(agent.x + 2, agent.y + 2);
        ctx.moveTo(agent.x + 2, agent.y - 2);
        ctx.lineTo(agent.x - 2, agent.y + 2);
        ctx.stroke();
      }
    });
  }
  
  
  // Funkcja wywoływana w interwale, aby pobierać aktualne dane z serwera
  let fetchCounter = 0;
  async function fetchSimulationData() {
    try {
      const response = await fetch("/data");
      if (!response.ok) {
        console.error("Błąd podczas pobierania danych z serwera.");
        return;
      }
      const data = await response.json();
      
      // DODANE: wywołanie funkcji aktualizującej zegar
      updateClock(data.hour);
      updateDay(data.day);

      if (fetchCounter % 2 === 0) {
        drawMap(data.agents);
      } else {
        // Tylko wykresy, bez mapy
        updateChartData(data.healthy, data.sick, data.dead, data.earnings, data.tick);
        updateChartData2(data.healthy, data.sick, data.dead, data.earnings, data.tick);
      }
      fetchCounter++;

      } catch (err) {
      console.error("Błąd:", err);
    }
  }
  
  let simulationInterval = null; 
  function startSimulationLoop() {
    if (simulationInterval) clearInterval(simulationInterval); // Kasuj stary interwał
  
    const speed = document.getElementById("speedSlider").value;
    simulationInterval = setInterval(fetchSimulationData, speed);
  }
  

  // Funkcja, która rozpoczyna symulację po kliknięciu przycisku
  async function startSimulation() {
    // Pobierz wartości suwaków
    const population = document.getElementById("population").value;
    const hospitalBeds = document.getElementById("hospitalBeds").value;
    const income = document.getElementById("income").value;
    const infectionChance = document.getElementById("infectionChance").value;
    const deathChance = document.getElementById("deathChance").value;
    const recoverOutsideChance = document.getElementById("recoverOutsideChance").value;
    const recoverHospitalChance = document.getElementById("recoverHospitalChance").value;
    const initialSick = document.getElementById("initialSick").value;
    const customInput = document.getElementById("customInput").value; 
    const longSlider = document.getElementById("longSlider").value; 
    const customReduce = document.getElementById("customReduce").value; 
    const tempSlider = document.getElementById("tempSlider").value; 
    const customOutput = document.getElementById("customOutput").value; 

    // Wyślij dane do serwera
    try {
      const response = await fetch("/start", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          population,
          hospitalBeds,
          income,
          infectionChance,
          deathChance,
          recoverOutsideChance,
          recoverHospitalChance,
          initialSick,
          customInput,
          longSlider,
          customReduce,
          tempSlider,
          customOutput
        })
      });
      if (!response.ok) {
        console.error("Błąd podczas inicjalizacji symulacji.");
        return;
      }
      // Reset wykresu (opcjonalnie, jeśli chcesz czyścić poprzednie dane)
      statsChart.data.labels = [];
      statsChart.data.datasets.forEach(ds => ds.data = []);
      statsChart.update();

      statsChart2.data.labels = [];
      statsChart2.data.datasets.forEach(ds => ds.data = []);
      statsChart2.update();

      // Uruchom pętlę (np. co 1 sekundę) do odświeżania danych symulacji
      startSimulationLoop();
    } catch (err) {
      console.error("Błąd:", err);
    }
  }
  
let loadedScenario = null;
let playbackInterval = null;
let scenarioKeys = [];
let currentScenarioIndex = 0;


async function loadScenario() {
  const customOutput = document.getElementById("customOutput").value;

  if (!customOutput) {
    alert("Podaj nazwę pliku!");
    return;
  }

  try {
    const response = await fetch("/load", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ customOutput })
    });

    const data = await response.json();

    if (data.status === "loaded") {
      console.log("Plik wczytany, rozpoczynamy odtwarzanie...");
      startPlayback(); // automatycznie startujemy odtwarzanie
    } else {
      console.error("Błąd ładowania pliku.");
    }
  } catch (err) {
    console.error("Błąd:", err);
  }
}


function startPlayback() {
  if (playbackInterval) clearInterval(playbackInterval);

  playbackInterval = setInterval(async () => {
    try {
      const response = await fetch("/next");
      const data = await response.json();

      if (data.finished) {
        clearInterval(playbackInterval);
        console.log("Odtwarzanie zakończone");
        return;
      }

      const agents = data.agents.map(agent => ({
        x: agent.x,
        y: agent.y,
        status: agent.status
      }));

      drawMap(agents);

      updateChartData(data.healthy, data.sick, data.dead, data.earnings, data.step);
      updateChartData2(data.healthy, data.sick, data.dead, data.earnings, data.step);
      
    } catch (error) {
      console.error("Błąd podczas pobierania kroku symulacji:", error);
    }
  }, playbackSpeed);
}

  
  window.addEventListener("DOMContentLoaded", () => {
    initSliders();
    initChart();
    initChart2();
    document.getElementById("startSimulation").addEventListener("click", startSimulation);
    document.getElementById("playbackSpeedSlider").addEventListener("input", () => {
      playbackSpeed = parseInt(document.getElementById("playbackSpeedSlider").value);
      document.getElementById("playbackSpeedValue").textContent = playbackSpeed;

      if (playbackInterval) {        startPlayback();      }    });
    
    document.getElementById("loadScenario").addEventListener("click", loadScenario);

  });
  