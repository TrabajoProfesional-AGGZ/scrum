---
layout: default
title: Métricas del Primer MVP
parent: Métricas
nav_order: 2
---

# Métricas del Primer MVP (Sprint 1 a 10)

**Período:** 07/06/2026 al 13/08/2026

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

## 📊 Métricas Grupales

### 1. Sprint Burndown Histórico (Evolución sobre el Total)

Muestra cuántos puntos de historia van quedando pendientes sobre el total planificado para el MVP a lo largo de los 10 sprints.

<div>
  <canvas id="grupalesBurndown" height="100"></canvas>
</div>

### 2. Release Burnup Chart

Muestra la acumulación de puntos completados frente al alcance total trazado para este MVP.

<div>
  <canvas id="grupalesBurnup" height="100"></canvas>
</div>

### 3. Velocity Chart (Con desplazamiento lateral)

Compara los puntos comprometidos vs. completados en cada iteración. Deslizá horizontalmente para ver el historial completo.

<div style="width: 100%; overflow-x: auto; border: 1px solid #eee; padding: 10px; border-radius: 5px;">
  <div style="width: 1000px; height: 350px;">
    <canvas id="grupalesVelocity"></canvas>
  </div>
</div>

## 👤 Métricas Individuales de Seguimiento

Seleccioná un integrante del equipo para evaluar la evolución de su rendimiento personal y la distribución de sus tareas asignadas:

<select id="selectorMiembro" style="padding: 8px; font-size: 16px; border-radius: 5px; margin-bottom: 20px; cursor: pointer;">
  <option value="axel">Axel</option>
  <option value="lautaro">Lautaro</option>
  <option value="martin">Martín</option>
  <option value="felipe">Felipe</option>
  <option value="equipo">Equipo Conjunto</option>
</select>

### Rendimiento e Historias del Integrante
<div style="width: 100%; overflow-x: auto; border: 1px solid #eee; padding: 10px; border-radius: 5px;">
  <div style="width: 1000px; height: 300px;">
    <canvas id="chartIndividual"></canvas>
  </div>
</div>

<script>
  // 1. OBTENCIÓN DINÁMICA DE DATOS DESDE YAML (Vía Jekyll Liquid)
  const tareasData = {{ site.data.mvp1 | jsonify }};
  const NUM_SPRINTS = 10;
  const labelsSprints = Array.from({length: NUM_SPRINTS}, (_, i) => `Sprint ${i + 1}`);

  // 2. ESTRUCTURAS DE PROCESAMIENTO
  let alcanceTotal = 0;
  let grupales = {
    comprometidos: Array(NUM_SPRINTS).fill(0),
    completados: Array(NUM_SPRINTS).fill(0)
  };

  const datosIndividuales = {
    axel: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) },
    lautaro: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) },
    martin: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) },
    felipe: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) },
    equipo: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) }
  };

  // 3. MOTOR DE CÁLCULO
  tareasData.forEach(tarea => {
    alcanceTotal += tarea.puntos;
    let r = tarea.responsable ? tarea.responsable.toLowerCase() : '';

    // Asignar puntos comprometidos
    if (tarea.sprint_planificado && tarea.sprint_planificado <= NUM_SPRINTS) {
      let indiceS = tarea.sprint_planificado - 1;
      grupales.comprometidos[indiceS] += tarea.puntos;
      if (datosIndividuales[r]) {
        datosIndividuales[r].comprometidos[indiceS] += tarea.puntos;
      }
    }

    // Asignar puntos completados
    if (tarea.sprint_completado && tarea.sprint_completado <= NUM_SPRINTS) {
      let indiceC = tarea.sprint_completado - 1;
      grupales.completados[indiceC] += tarea.puntos;
      if (datosIndividuales[r]) {
        datosIndividuales[r].completados[indiceC] += tarea.puntos;
      }
    }
  });

  // Cálculo de Burnup y Burndown
  let burnupData = [];
  let burndownData = [];
  let scopeAcumulado = Array(NUM_SPRINTS).fill(alcanceTotal); // Linea plana del tope
  let puntosAcumulados = 0;

  for (let i = 0; i < NUM_SPRINTS; i++) {
    puntosAcumulados += grupales.completados[i];
    burnupData.push(puntosAcumulados);
    burndownData.push(alcanceTotal - puntosAcumulados);
  }

  // 4. RENDERIZADO DE GRÁFICOS
  new Chart(document.getElementById('grupalesBurndown'), {
    type: 'line',
    data: {
      labels: labelsSprints,
      datasets: [{ label: 'Puntos Pendientes (Burndown)', data: burndownData, borderColor: '#ff4d4d', tension: 0.1 }]
    }
  });

  new Chart(document.getElementById('grupalesBurnup'), {
    type: 'line',
    data: {
      labels: labelsSprints,
      datasets: [
        { label: 'Puntos Completados Acumulados', data: burnupData, borderColor: '#2ecc71', fill: false },
        { label: 'Alcance Total (Scope)', data: scopeAcumulado, borderColor: '#34495e', borderDash: [5, 5] }
      ]
    }
  });

  new Chart(document.getElementById('grupalesVelocity'), {
    type: 'bar',
    data: {
      labels: labelsSprints,
      datasets: [
        { label: 'Puntos Comprometidos', data: grupales.comprometidos, backgroundColor: '#3498db' },
        { label: 'Puntos Completados', data: grupales.completados, backgroundColor: '#2ecc71' }
      ]
    },
    options: { responsive: true, maintainAspectRatio: false }
  });

  // 5. CONTROLADOR DEL GRÁFICO INDIVIDUAL
  let chartInd;
  function renderizarGraficoIndividual(miembro) {
    const ctx = document.getElementById('chartIndividual').getContext('2d');
    if (chartInd) { chartInd.destroy(); }

    chartInd = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labelsSprints,
        datasets: [
          { label: 'Puntos Asignados', data: datosIndividuales[miembro].comprometidos, backgroundColor: '#9b59b6' },
          { label: 'Puntos Completados', data: datosIndividuales[miembro].completados, backgroundColor: '#1abc9c' }
        ]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  document.getElementById('selectorMiembro').addEventListener('change', (e) => {
    renderizarGraficoIndividual(e.target.value);
  });

  renderizarGraficoIndividual('axel'); // Iniciar con Axel
</script>
