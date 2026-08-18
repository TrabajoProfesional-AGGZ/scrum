---
layout: default
title: Sprint planning N°13
parent: Sprint planning
nav_order: 13
---

# Sprint planning N°13

**Fecha:** Miércoles 26/08/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Enfocar el 100% del esfuerzo en la preparación académica para el cierre del "Trabajo Profesional". Se finalizará la redacción de los manuales y la grabación de los tutoriales de uso. Además, se construirá la primera versión del informe final a entregar y la presentación (diapositivas y guion) que se utilizará en la defensa final del proyecto.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana de **1 semana**, iniciando el día miércoles.
* **Cierre de desarrollo técnico:** No se planifican nuevas tareas de código o infraestructura; el producto se encuentra congelado y estable.
* **Foco en la Defensa Final:** La prioridad absoluta del equipo es el armado de la documentación académica requerida por la facultad. Esto incluye la estructuración del informe final y la preparación del material de soporte para la defensa oral.
* **Finalización de material de apoyo:** Se completarán las tareas de los tutoriales y manuales arrastradas desde el sprint 12 para tener el paquete de entrega completo.

## 📦 Sprint Backlog (Tareas comprometidas)

*(Las tareas específicas se listan a continuación, filtradas por miembro del equipo).*

<div style="display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap;">
  <select id="selectorMiembroBacklog" style="padding: 8px; font-size: 16px; border-radius: 5px; cursor: pointer;">
    <option value="todos">Vista general</option>
    <option value="axel">Axel</option>
    <option value="lautaro">Lautaro</option>
    <option value="martin">Martín</option>
    <option value="felipe">Felipe</option>
    <option value="equipo">Equipo conjunto</option>
  </select>
</div>

<div id="backlogTareasContenedor" style="background-color: #f8f9fa; border-left: 4px solid #7253ed; padding: 15px; border-radius: 4px; margin-bottom: 25px;"></div>

## ⚠️ Riesgos y dependencias

* **Sobrecarga de revisión académica:** La elaboración de la primera versión del informe final y la presentación puede requerir iteraciones rápidas para ajustar formatos o contenidos.
* **Mitigación:** Se priorizará tener borradores (primeras versiones) lo antes posible para poder realizar revisiones cruzadas entre todos los miembros del equipo y corregir detalles antes de la fecha límite.

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
    const SPRINT_ACTUAL = 13;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°13.</p>';
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
