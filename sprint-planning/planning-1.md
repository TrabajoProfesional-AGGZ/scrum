---
layout: default
title: Sprint Planning N°1
parent: Sprint Planning
nav_order: 1
---

# Sprint Planning N°1

**Fecha:** Domingo 07/06/2026  
**Duración del Sprint:** 4 días

## 🎯 Objetivo del Sprint

Crear la estructura base de los microservicios y la plataforma web, establecer el funcionamiento empírico del sistema de estimaciones por puntos, y afianzar la dinámica de trabajo en equipo durante esta primera iteración.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Sistema de puntuación de historias de usuario (GitHub Projects):** Se definieron los siguientes valores:
  * Verde/Bajo (Low) = 1 punto.
  * Amarillo/Medio (Medium) = 3 puntos.
  * Rojo/Alto (High) = 5 puntos.
* **Organización del equipo:** 3 integrantes desarrollarán las Historias de Usuario (Axel, Lautaro y Martín) y 1 integrante se encargará de la documentación técnica y presentaciones (Felipe).
* **Gestión de ceremonias:** Se estableció que todas las ceremonias de Scrum se realizarán los días **Jueves** (esta primera sesión fue el domingo 07/06 de forma excepcional).
* **Duración:** Este es un **Sprint corto (4 días)**, lo cual fue considerado como un factor principal para dimensionar el alcance de las tareas.
* **Lineamientos técnicos:** * Se creará toda la estructura base de la plataforma web. Queda estrictamente definido que no se pasará a la fase de desarrollo de la app móvil hasta no finalizar esta etapa del desarrollo.
  * Se utilizarán *Sub-issues* en cada ticket para identificar claramente todos los repositorios involucrados en el funcionamiento de una tarea particular (ej. Vista, gateway, microservicios, etc).

## 📦 Sprint Backlog (Tareas Comprometidas)

Se definió trabajar sobre todas las historias de usuario correspondientes a las **Épicas 1 y 2** planificadas para este ciclo.

Filtrar el backlog comprometido por integrante del equipo:

*Nota: La opción **"Vista General"** consolidará el listado absoluto de tareas del sprint.*

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

* **Arquitectura de microservicios:** Posibles inconvenientes a la hora de crear e interconectar todos los microservicios, bases de datos e interfaces de usuario entre sí. Se prestará principal atención a esto durante el transcurso del ciclo.
* **Dinámica de trabajo:** Al ser el primer Sprint, existe el desafío natural del funcionamiento del equipo en su conjunto, la adaptación a los repositorios separados y el ciclo de revisión de código.
* **Limitación de tiempo:** El tiempo reducido de este primer Sprint (4 días en lugar del ciclo habitual) podría afectar el volumen total de cierre de tareas.

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
    const SPRINT_ACTUAL = 1;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint Planning N°1.</p>';
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
