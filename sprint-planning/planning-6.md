---
layout: default
title: Sprint planning N°6
parent: Sprint planning
nav_order: 6
---

# Sprint planning N°6

**Fecha:** Jueves 09/07/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Iniciar el desarrollo de la plataforma bajo el enfoque PWA (Progressive Web App) y establecer los primeros canales de comunicación y transacciones.

El foco estará en abordar las historias de usuario de la Épica 6, sentar las bases del microservicio de pagos (Épica 8), configurar de forma inicial el canal conversacional vía WhatsApp y analizar Trabajos Profesionales anteriores para incorporar ideas y valor agregado al proyecto.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana del sprint en **1 semana**.
* **Foco técnico:** La prioridad se divide entre la configuración inicial de la arquitectura PWA y la creación de pruebas de concepto para integraciones clave (WhatsApp y pasarela de pagos). 
* **Investigación y análisis:** Se asignará parte de la capacidad del equipo a la lectura y análisis de Trabajos Profesionales anteriores. Esto funcionará como una etapa de descubrimiento para inspirar nuevas funcionalidades o mejorar el enfoque actual.
* **Transición de entorno:** Tras haber cerrado la fase estrictamente web, el equipo se adaptará a las nuevas herramientas requeridas para la PWA y las integraciones de microservicios.

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

* **Curva de aprendizaje en integraciones:** El inicio de las bases para WhatsApp y el microservicio de pagos puede presentar bloqueos técnicos al depender de APIs o servicios externos.
* **Mitigación:** Se buscará hacer implementaciones "base" o pruebas de concepto antes de comprometer un desarrollo profundo. Además, la revisión de trabajos anteriores servirá para anticipar problemas comunes y adoptar buenas prácticas comprobadas.

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
    const SPRINT_ACTUAL = 6;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°6.</p>';
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
