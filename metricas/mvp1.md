---
layout: default
title: Métricas del primer MVP
parent: Métricas
nav_order: 2
---

# Métricas del primer MVP (Sprint 1 a 10)

**Período:** 07/06/2026 al 13/08/2026

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

## 📊 Métricas grupales

### Release Burndown Chart

Muestra cuántos puntos de historia van quedando pendientes sobre el total planificado para el MVP a lo largo de los 10 sprints.

<div>
  <canvas id="grupalesBurndown" height="100"></canvas>
</div>

### Release Burnup Chart

Muestra la acumulación de puntos completados frente al alcance total trazado para este MVP.

<div>
  <canvas id="grupalesBurnup" height="100"></canvas>
</div>

### Release Velocity Chart

Compara los puntos comprometidos contra los puntos completados en cada iteración.

<div style="width: 100%; overflow-x: auto; border: 1px solid #eee; padding: 10px; border-radius: 5px;">
  <div style="width: 1000px; height: 350px;">
    <canvas id="grupalesVelocity"></canvas>
  </div>
</div>

## 👤 Métricas individuales y Backlog de tareas

Seleccioná un integrante (o el backlog sin asignar) para visualizar la distribución de sus tareas:

*Nota: La opción **"Equipo conjunto"** permite visualizar las tareas que fueron realizadas explícitamente en forma coordinada por los 4 integrantes del equipo.*

<div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
  <select id="selectorMiembro" style="padding: 8px; font-size: 16px; border-radius: 5px; cursor: pointer;">
    <option value="axel">Axel</option>
    <option value="lautaro">Lautaro</option>
    <option value="martin">Martín</option>
    <option value="felipe">Felipe</option>
    <option value="equipo">Equipo conjunto</option>
    <option value="a designar">A designar</option>
  </select>
</div>

### Rendimiento General del Integrante

<div style="width: 100%; overflow-x: auto; border: 1px solid #eee; padding: 10px; border-radius: 5px; margin-bottom: 30px;">
  <div style="width: 1000px; height: 300px;">
    <canvas id="chartIndividual"></canvas>
  </div>
</div>

### Detalle de Tareas por Sprint

Seleccioná un Sprint específico para ver qué tareas se le planificaron a este integrante y cuál es su estado actual:

<div style="margin-bottom: 15px;">
  <select id="selectorSprint" style="padding: 8px; font-size: 16px; border-radius: 5px; cursor: pointer;">
    <option value="1">Sprint 1</option>
    <option value="2">Sprint 2</option>
    <option value="3">Sprint 3</option>
    <option value="4">Sprint 4</option>
    <option value="5">Sprint 5</option>
    <option value="6">Sprint 6</option>
    <option value="7">Sprint 7</option>
    <option value="8">Sprint 8</option>
    <option value="9">Sprint 9</option>
    <option value="10">Sprint 10</option>
  </select>
</div>

<div id="listaTareasContenedor" style="background-color: #f8f9fa; border-left: 4px solid #7253ed; padding: 15px; border-radius: 4px;"></div>

<script type="application/json" id="backlog-data">
{% if site.data.backlog %}{{ site.data.backlog | jsonify }}{% else %}[]{% endif %}
</script>

<script markdown="0">
  (function() {
    let tareasData = [];
    try {
      const jsonText = document.getElementById('backlog-data').textContent;
      tareasData = JSON.parse(jsonText) || [];
    } catch(e) {
      console.error("Error cargando los datos de Jekyll:", e);
    }
    const NUM_SPRINTS = 10;
    const labelsSprints = [];
    for (let i = 1; i <= NUM_SPRINTS; i++) {
      labelsSprints.push("Sprint " + i);
    }
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
      equipo: { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) },
      "a designar": { comprometidos: Array(NUM_SPRINTS).fill(0), completados: Array(NUM_SPRINTS).fill(0) }
    };
    if (tareasData.length > 0) {
      tareasData.forEach(function(tarea) {
        alcanceTotal += tarea.puntos;
        let r = tarea.responsable ? tarea.responsable.toLowerCase() : 'a designar';
        if (!datosIndividuales[r]) r = 'a designar';
        if (tarea.sprint_planificado && tarea.sprint_planificado <= NUM_SPRINTS) {
          let indiceS = tarea.sprint_planificado - 1;
          grupales.comprometidos[indiceS] += tarea.puntos;
          datosIndividuales[r].comprometidos[indiceS] += tarea.puntos;
        }
        if (tarea.sprint_completado && tarea.sprint_completado <= NUM_SPRINTS) {
          let indiceC = tarea.sprint_completado - 1;
          grupales.completados[indiceC] += tarea.puntos;
          datosIndividuales[r].completados[indiceC] += tarea.puntos;
        }
      });
    }
    let burnupData = [];
    let burndownData = [];
    let scopeAcumulado = Array(NUM_SPRINTS).fill(alcanceTotal);
    let puntosAcumulados = 0;
    for (let i = 0; i < NUM_SPRINTS; i++) {
      puntosAcumulados += grupales.completados[i];
      burnupData.push(puntosAcumulados);
      burndownData.push(alcanceTotal - puntosAcumulados);
    }
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
        options: { responsive: true, maintainAspectRatio: false, scales: { y: { beginAtZero: true } } }
      });
    }
    function actualizarListaTareas() {
      const miembro = document.getElementById('selectorMiembro').value;
      const sprintActual = parseInt(document.getElementById('selectorSprint').value);
      const contenedor = document.getElementById('listaTareasContenedor');
      const tareasDelSprint = tareasData.filter(function(t) {
        let resp = t.responsable ? t.responsable.toLowerCase() : 'a designar';
        if (!datosIndividuales[resp]) resp = 'a designar';
        return resp === miembro && t.sprint_planificado === sprintActual;
      });
      if (tareasDelSprint.length === 0) {
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No hay tareas asignadas para este integrante en el Sprint seleccionado.</p>';
        return;
      }
      let html = '<ul style="margin: 0; padding-left: 20px;">';
      tareasDelSprint.forEach(function(t) {
        const estaCompletada = (t.sprint_completado !== null);
        const icono = estaCompletada ? '✅' : '⏳';
        let detalleEstado = estaCompletada ? `<span style="color: #2ecc71; font-weight: bold;">(Completada en Sprint ${t.sprint_completado})</span>` : `<span style="color: #e67e22; font-weight: bold;">(Pendiente)</span>`;
        html += `<li style="margin-bottom: 8px;"><strong>${icono} ${t.titulo}</strong> <br><span style="font-size: 0.9em; color: #666;">ID: <code>${t.id}</code> | Esfuerzo: <strong>${t.puntos} pts</strong> | Estado: ${detalleEstado}</span></li>`;
      });
      html += '</ul>';
      contenedor.innerHTML = html;
    }
    document.getElementById('selectorMiembro').addEventListener('change', function(e) {
      renderizarGraficoIndividual(e.target.value);
      actualizarListaTareas();
    });
    document.getElementById('selectorSprint').addEventListener('change', function() {
      actualizarListaTareas();
    });
    renderizarGraficoIndividual('axel');
    actualizarListaTareas();
  })();
</script>
