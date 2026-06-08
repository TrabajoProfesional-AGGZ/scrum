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

---

## 👤 Métricas Individuales de Seguimiento

Seleccioná un integrante del equipo para evaluar la evolución de su rendimiento personal y la distribución de sus tareas asignadas:

<select id="selectorMiembro" style="padding: 8px; font-size: 16px; border-radius: 5px; margin-bottom: 20px; cursor: pointer;">
  <option value="axel">Axel</option>
  <option value="lautaro">Lautaro</option>
  <option value="martin">Martín</option>
  <option value="felipe">Felipe</option>
</select>

### Rendimiento e Historias del Integrante
<div style="width: 100%; overflow-x: auto; border: 1px solid #eee; padding: 10px; border-radius: 5px;">
  <div style="width: 1000px; height: 300px;">
    <canvas id="chartIndividual"></canvas>
  </div>
</div>

<script>
  // ---- 1. CONFIGURACIÓN DE GRÁFICOS GRUPALES (MOCK DATA EJEMPLO) ----
  const labelsSprints = ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5', 'Sprint 6', 'Sprint 7', 'Sprint 8', 'Sprint 9', 'Sprint 10'];

  // Burndown total del MVP
  new Chart(document.getElementById('grupalesBurndown'), {
    type: 'line',
    data: {
      labels: labelsSprints,
      datasets: [{ label: 'Puntos Restantes Real', data: [120, 105, 90, 78, 60, 45, 30, 22, 10, 0], borderColor: '#ff4d4d', tension: 0.1 }]
    }
  });

  // Burnup total del MVP
  new Chart(document.getElementById('grupalesBurnup'), {
    type: 'line',
    data: {
      labels: labelsSprints,
      datasets: [
        { label: 'Puntos Completados', data: [0, 15, 30, 42, 60, 75, 90, 98, 110, 120], borderColor: '#2ecc71', fill: false },
        { label: 'Alcance Total (Scope)', data: [120, 120, 120, 120, 120, 120, 120, 120, 120, 120], borderColor: '#34495e', borderDash: [5, 5] }
      ]
    }
  });

  // Velocity con Scroll Lateral (20 columnas totales)
  new Chart(document.getElementById('grupalesVelocity'), {
    type: 'bar',
    data: {
      labels: labelsSprints,
      datasets: [
        { label: 'Puntos Comprometidos', data: [15, 18, 12, 15, 20, 14, 16, 12, 15, 10], backgroundColor: '#3498db' },
        { label: 'Puntos Completados', data: [12, 15, 12, 12, 18, 14, 15, 10, 15, 10], backgroundColor: '#2ecc71' }
      ]
    },
    options: { responsive: true, maintainAspectRatio: false }
  });


  // ---- 2. LÓGICA DE MÉTRICAS INDIVIDUALES DINÁMICAS ----
  const datosIndividuales = {
    axel: { comprometidos: [5, 6, 4, 5, 6, 5, 6, 4, 5, 3], completados: [4, 5, 4, 4, 5, 5, 5, 4, 5, 3] },
    lautaro: { comprometidos: [5, 6, 4, 5, 7, 4, 5, 4, 5, 3], completados: [4, 5, 4, 4, 6, 4, 5, 3, 5, 3] },
    martin: { comprometidos: [5, 6, 4, 5, 7, 5, 5, 4, 5, 4], completados: [4, 5, 4, 4, 7, 5, 5, 3, 5, 4] },
    felipe: { comprometidos: [3, 3, 3, 3, 4, 3, 4, 3, 3, 2], completados: [3, 3, 3, 3, 4, 3, 4, 3, 3, 2] } // Documentación / Tareas estables
  };

  let chartInd; // Variable global para controlar la instancia del gráfico individual

  function renderizarGraficoIndividual(miembro) {
    const ctx = document.getElementById('chartIndividual').getContext('2d');
    
    // Si ya existe un gráfico previo renderizado, lo destruimos para que no se superpongan los datos antiguos
    if (chartInd) { chartInd.destroy(); }

    chartInd = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labelsSprints,
        datasets: [
          { label: 'Puntos Asignados', data: datosIndividuales[miembro].comprometidos, backgroundColor: '#9b59b6' },
          { label: 'Puntos Resolvidos con Éxito', data: datosIndividuales[miembro].completados, backgroundColor: '#1abc9c' }
        ]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  // Escuchamos los cambios del selector
  document.getElementById('selectorMiembro').addEventListener('change', (e) => {
    renderizarGraficoIndividual(e.target.value);
  });

  // Render inicial por defecto con Axel
  renderizarGraficoIndividual('axel');
</script>
