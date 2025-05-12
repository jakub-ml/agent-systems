const background = new Image();
background.src = 'static/images/background1.png';

const personSick = new Image();
personSick.src = 'static/images/sick.png';
const personHealthy = new Image();
personHealthy.src = 'static/images/healthy.png';
const personDead = new Image();
personDead.src = 'static/images/dead.png';
const schoolIcon = new Image();
schoolIcon.src = 'static/images/school1.png';
const hospitalIcon = new Image();
hospitalIcon.src = 'static/images/hospital.png';
const officeIcon = new Image();
officeIcon.src = 'static/images/office2.jpg';
const shopIcon = new Image();
shopIcon.src = 'static/images/shop2.png';
const houseIcon = new Image();
houseIcon.src = 'static/images/home2.png';

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
    
    const sliders = [
      { sliderId: "population", valueId: "populationValue" },
      { sliderId: "hospitalBeds", valueId: "hospitalBedsValue" },
      { sliderId: "income", valueId: "incomeValue" },
      { sliderId: "infectionChance", valueId: "infectionChanceValue" },
      { sliderId: "deathChance", valueId: "deathChanceValue" },
      { sliderId: "recoverOutsideChance", valueId: "recoverOutsideValue" },
      { sliderId: "recoverHospitalChance", valueId: "recoverHospitalValue" },
      { sliderId: "initialSick", valueId: "initialValue" }
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
            label: "Zdrowi",
            data: [],
            borderColor: "green",
            fill: false
          },
          {
            label: "Chorzy",
            data: [],
            borderColor: "red",
            fill: false
          },
          {
            label: "Martwi",
            data: [],
            borderColor: "black",
            fill: false
          },
          // {
          //   label: "Zarobki",
          //   data: [],
          //   borderColor: "blue",
          //   fill: false
          // }
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
            // {
            //   label: "Zdrowi",
            //   data: [],
            //   borderColor: "green",
            //   fill: false
            // },
            // {
            //   label: "Chorzy",
            //   data: [],
            //   borderColor: "red",
            //   fill: false
            // },
            // {
            //   label: "Martwi",
            //   data: [],
            //   borderColor: "black",
            //   fill: false
            // },
            {
              label: "Zarobki",
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
    //drawGrid(ctx, canvas.width, canvas.height, 10);
    ctx.drawImage(background, 0, 0, canvas.width, canvas.height);

    ctx.globalAlpha = 0.65;
    ctx.drawImage(schoolIcon, 3, 720, 300, 200);
    ctx.drawImage(hospitalIcon, 3, 190, 170, 200);
    ctx.drawImage(officeIcon, 650, 720, 300, 250);
    ctx.drawImage(officeIcon, 650, 500, 300, 250);
    ctx.drawImage(shopIcon, 250, 400, 250, 300);// i think it is better to change coordinates
    ctx.drawImage(houseIcon, 3, 15, 150, 150);
    ctx.drawImage(houseIcon, 155, 15, 150, 150);
    ctx.drawImage(houseIcon, 310, 15, 150, 150);
    ctx.drawImage(houseIcon, 465, 15, 150, 150);
    ctx.drawImage(houseIcon, 615, 15, 150, 150);
    ctx.drawImage(houseIcon, 765, 15, 150, 150);
    ctx.globalAlpha = 1.0;

    // Rysowanie agentów...
    agents.forEach(agent => {
      /*if (agent.status === "healthy") {
        ctx.fillStyle = "green";
        ctx.beginPath();
        ctx.arc(agent.x, agent.y, 5, 0, 5 * Math.PI);
        ctx.fill();
        ctx.drawImage(personHealthy, agent.x - 16, agent.y - 16, 20, 20);
      } else if (agent.status === "sick") {
        ctx.drawImage(personSick, agent.x - 16, agent.y - 16, 20, 20);
      } else if (agent.status === "dead") {
        ctx.drawImage(personDead, agent.x - 16, agent.y - 16, 20, 20);*/
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
          initialSick
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
      setInterval(fetchSimulationData, 100);
    } catch (err) {
      console.error("Błąd:", err);
    }
  }
  
  window.addEventListener("DOMContentLoaded", () => {
    initSliders();
    initChart();
    initChart2();
    document.getElementById("startSimulation").addEventListener("click", startSimulation);
  });
  