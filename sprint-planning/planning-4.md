---
layout: default
title: Sprint planning N°4
parent: Sprint planning
nav_order: 4
---

# Sprint planning N°4

**Fecha:** Jueves 25/06/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Iniciar con el desarrollo de las épicas 4 y 5, asumiendo el compromiso de terminarlas. A su vez, se comenzará a trabajar en el diseño responsive de la página web, distribuyendo este esfuerzo entre el presente sprint y el siguiente para asegurar el avance continuo del proyecto profesional.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana del sprint en **1 semana**.
* **Ajuste de capacidad y flexibilidad:** Dado que el equipo se encuentra en época de exámenes finales en FIUBA, se acordó una modalidad de trabajo más flexible. Cada integrante distribuirá sus tiempos y tareas a lo largo de estas dos semanas como le resulte más conveniente, evitando frenar el desarrollo pero sin descuidar las evaluaciones universitarias.
* **Foco técnico:** El objetivo técnico de esta iteración es terminar definitivamente con todas las features de la plataforma web. Esto permitirá que dentro de dos semanas el equipo pueda cambiar el enfoque y comenzar a trabajar íntegramente sobre la aplicación móvil.

## 📦 Sprint Backlog (Tareas Comprometidas)

*(Las tareas específicas se listan a continuación, filtradas por miembro del equipo).*

<div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
  <select id="selectorMiembroBacklog" style="padding: 8px; font-size: 16px; border-radius: 5px; cursor: pointer;">
    <option value="todos">Vista General</option>
    <option value="axel">Axel</option>
    <option value="lautaro">Lautaro</option>
    <option value="martin">Martín</option>
    <option value="felipe">Felipe</option>
    <option value="equipo">Equipo conjunto</option>
  </select>
</div>

<div id="backlogTareasContenedor" style="background-color: #f8f9fa; border-left: 4px solid #7253ed; padding: 15px; border-radius: 4px; margin-bottom: 25px;"></div>

## ⚠️ Riesgos y dependencias

* **Disponibilidad por finales:** El riesgo principal es la limitación en la disponibilidad horaria del equipo debido a la carga de estudio por los exámenes.
* **Mitigación:** La organización autónoma de los tiempos a lo largo de dos sprints garantiza que el desarrollo no se estanque, dándole a cada integrante la libertad de manejar sus responsabilidades de forma eficiente.

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
      console.error("Error decodificando la base de datos de tareas:", e);
    }
    const SPRINT_ACTUAL = 4;
    const tareasDelSprint = tareasData.filter(function(t) {
      return t.sprint_planificado === SPRINT_ACTUAL;
    });
    function actualizarVistaBacklog() {
      const miembroFiltrado = document.getElementById('selectorMiembroBacklog').value;
      const contenedor = document.getElementById('backlogTareasContenedor');
      const tareasAMostrar = tareasDelSprint.filter(function(t) {
        let resp = t.responsable ? t.responsable.toLowerCase() : 'a designar';
        if (resp.includes('conjunto')) resp = 'equipo';
        if (miembroFiltrado === 'todos') return true;
        return resp === miembroFiltrado;
      });
      if (tareasAMostrar.length === 0) {
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°4.</p>';
        return;
      }
      let html = '<ul style="margin: 0; padding-left: 20px;">';
      tareasAMostrar.forEach(function(t) {
        const estaCompletada = (t.sprint_completado !== null);
        const icono = estaCompletada ? '✅' : '⏳';
        let stringEstado = estaCompletada ? `<span style="color: #2ecc71; font-weight: bold;">(Completado en Sprint ${t.sprint_completado})</span>` : `<span style="color: #e67e22; font-weight: bold;">(Comprometido - Pendiente)</span>`;
        let etiquetaResponsable = '';
        if (miembroFiltrado === 'todos') {
          let nombreFormateado = t.responsable ? t.responsable.charAt(0).toUpperCase() + t.responsable.slice(1) : 'A designar';
          etiquetaResponsable = ` | Responsable: <strong>${nombreFormateado}</strong>`;
        }
        html += `<li style="margin-bottom: 10px;"><strong>${icono} ${t.titulo}</strong> <br><span style="font-size: 0.9em; color: #666;">ID: <code>${t.id}</code> | Puntos: <strong>${t.puntos} pts</strong>${etiquetaResponsable} | Estado: ${stringEstado}</span></li>`;
      });
      html += '</ul>';
      contenedor.innerHTML = html;
    }
    document.getElementById('selectorMiembroBacklog').addEventListener('change', actualizarVistaBacklog);
    actualizarVistaBacklog();
  })();
</script>
