---
layout: default
title: Sprint planning N°9
parent: Sprint planning
nav_order: 9
---

# Sprint planning N°9

**Fecha:** Miércoles 29/07/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Finalizar el desarrollo de las últimas épicas del primer MVP: Épica 10 (Rol empleado / Accesos) y Épica 11 (Canal conversacional), con el propósito de finalizar la primera versión del producto y garantizar una semana entera de colchón dedicada exclusivamente a testing integral.

Asimismo, concretar la entrevista de validación con Martín Fernando Rubino (Club Atlético Talleres de Remedios de Escalada).

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración y nuevo ciclo:** El sprint tendrá una duración de **1 semana**, oficializando el nuevo esquema de inicio los días miércoles.
* **Foco técnico (Cierre de MVP):** La máxima prioridad técnica es liquidar las historias de usuario de la Épica 10 y la Épica 11. No se tomarán tareas de nuevas épicas para evitar el *scope creep* y asegurar el cierre limpio del primer MVP.
* **Semana de colchón:** Todo el trabajo de desarrollo comprometido en este ciclo debe finalizar en tiempo y forma para habilitar que el siguiente sprint funcione íntegramente como una semana de *testing*, *bugfixing* y estabilización general antes de las presentaciones.
* **Foco de validación y negocio:** Se llevará a cabo la reunión con Martín Fernando Rubino, aprovechando su experiencia y visión dentro del Club Atlético Talleres (Remedios de Escalada) para validar el enfoque del producto con un actor real del sector.

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

* **Ajustes derivados de la entrevista:** La charla de validación con Talleres de Remedios de Escalada puede arrojar comentarios o sugerencias de cambios sobre funcionalidades existentes.
* **Mitigación:** Se acordó que cualquier nuevo requerimiento o mejora surgida de la entrevista se registrará como un ítem de mejora para etapas posteriores al MVP, preservando intacta la semana de colchón para pruebas.
* **Complejidad en integraciones:** El cierre del canal conversacional (Épica 11) y el control de accesos (Épica 10) pueden generar cuellos de botella al integrarse con el resto de los módulos ya terminados. Se priorizarán las revisiones conjuntas para desbloquear PRs rápidamente.

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
    const SPRINT_ACTUAL = 9;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°9.</p>';
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
