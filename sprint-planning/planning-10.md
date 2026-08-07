---
layout: default
title: Sprint planning N°10
parent: Sprint planning
nav_order: 10
---

# Sprint planning N°10

**Fecha:** Miércoles 05/08/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Cerrar por completo el MVP diseñado para SocioUnido. Para lograrlo, el enfoque principal será ejecutar un testing intensivo de toda la arquitectura (microservicios, gateway, aplicaciones y plataforma web) y pulir la seguridad, confiabilidad y claridad del código utilizando OpenClaw y SonarCloud. Además, se incluye el despliegue final del bot conversacional en Telegram, la creación de la página de monitoreo, y la implementación de funcionalidades pequeñas de alto valor.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana de **1 semana**, sosteniendo el inicio de ciclo los días miércoles.
* **Foco técnico (Testing y Calidad):** La prioridad absoluta es la estabilidad del producto. Se auditará el código con herramientas automatizadas (SonarCloud y OpenClaw) y se redactará un anexo formal basado en los reportes obtenidos.
* **Funcionalidades "Quick Wins":** Se acordó incorporar únicamente aquellas pequeñas funcionalidades que representen un bajo costo de desarrollo/implementación pero que aporten un alto valor percibido al MVP.
* **Pivote de canal conversacional:** Se finalizará la migración y el despliegue del bot hacia la nueva plataforma elegida (Telegram), adaptando las integraciones necesarias.
* **Monitoreo de producto:** Se destinará capacidad del equipo a la creación de un panel de monitoreo multi-club para tener control integral del sistema.

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

* **Sobrecarga por hallazgos de seguridad:** Los análisis de SonarCloud y OpenClaw pueden revelar una gran cantidad de deudas técnicas o vulnerabilidades que excedan el tiempo del sprint.
* **Mitigación:** Se priorizará la resolución exclusiva de vulnerabilidades críticas o bloqueantes para el MVP.
* **Curva de integración con Telegram:** El despliegue en la nueva plataforma puede presentar trabas en la configuración de webhooks o permisos. Se atacará esta tarea en los primeros días del sprint para tener margen de maniobra.

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
    const SPRINT_ACTUAL = 10;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°10.</p>';
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
