---
layout: default
title: Sprint planning N°7
parent: Sprint planning
nav_order: 7
---

# Sprint planning N°7

**Fecha:** Jueves 16/07/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

El objetivo principal de esta iteración es finalizar completamente el desarrollo de la Épica 8, consolidando el microservicio de pagos iniciado la semana pasada, y abordar en su totalidad el desarrollo y las funcionalidades correspondientes a la Épica 7.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana del sprint en **1 semana**.
* **Foco técnico:** La prioridad al inicio de la semana será destrabar y finalizar cualquier pendiente crítico del microservicio de pagos (Épica 8) para asegurar su correcto funcionamiento. Posteriormente, el equipo se enfocará de lleno en las nuevas historias de la Épica 7.
* **Organización:** Se buscará un trabajo en paralelo donde los responsables de la Épica 8 puedan realizar el cierre de la misma mientras el resto del equipo va sentando las bases de la Épica 7, optimizando los tiempos del ciclo.

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

* **Cuellos de botella técnicos:** Finalizar una épica compleja (microservicio de pagos) mientras se inicia una nueva (Épica 7) puede generar sobrecarga en la revisión de código o en la integración continua.

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
    const SPRINT_ACTUAL = 7;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°7.</p>';
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
