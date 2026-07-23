---
layout: default
title: Sprint planning N°8
parent: Sprint planning
nav_order: 8
---

# Sprint planning N°8

**Fecha:** Jueves 23/07/2026  
**Duración del Sprint:** 6 días

## 🎯 Objetivo del sprint

Cerrar definitivamente las historias de usuario que quedaron pendientes de la Épica 7 y la Épica 8. En paralelo, iniciar el acercamiento comercial definiendo estratégicamente el club para las demos y consiguiendo contactos clave en diferentes instituciones para validar la utilidad del producto y refinar nuestro foco.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración atípica:** Excepcionalmente, este sprint durará **6 días**, ya que el equipo acordó cambiar la fecha de las reuniones semanales de los jueves a los días miércoles.
* **Foco técnico:** La prioridad a nivel de código es liquidar la deuda técnica y las tareas pendientes de las Épicas 7 y 8 para dejar el producto estable y no arrastrar funcionalidades incompletas.
* **Foco comercial y de negocio:** Se destinará una parte importante del esfuerzo en buscar y concretar contactos en distintos clubes. Esto nos permitirá validar de primera mano la utilidad de la plataforma y entender exactamente en qué puntos de dolor debemos focalizarnos.
* **Elección estratégica:** La definición del club con el que se harán las demos se tomará con especial cuidado. El objetivo es elegir una institución que nos permita simpatizar con el resto del mercado y generar una excelente recepción por parte de futuros clientes.

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

* **Dependencia de terceros:** Conseguir contactos y respuestas de los clubes para la validación puede demorarse más de la cuenta al depender de personas externas al proyecto.
* **Mitigación:** Se buscará contactar a varias instituciones en paralelo para no depender de una sola respuesta. A su vez, mientras se espera el feedback, el equipo de desarrollo seguirá avanzando ininterrumpidamente con el cierre de las tareas técnicas.

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
    const SPRINT_ACTUAL = 8;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°8.</p>';
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
