---
layout: default
title: Sprint planning N°11
parent: Sprint planning
nav_order: 11
---

# Sprint planning N°11

**Fecha:** Miércoles 12/08/2026  
**Duración del Sprint:** 1 semana

## 🎯 Objetivo del sprint

Iniciar al 100% el desarrollo de la documentación final del Trabajo Profesional. A nivel técnico, el objetivo es construir un "club maqueta" completamente funcional con un padrón societario extenso para simulaciones, finalizar la preparación del bot conversacional ("Botín") para la Demo oficial, e incorporar las últimas métricas (eventos y tienda) a la plataforma web.

## ⏱️ Capacidad del equipo y acuerdos de trabajo

* **Duración:** Se mantiene la ventana de **1 semana**, iniciando el día miércoles.
* **Foco documental absoluto:** Se invertirá la mayor parte de la capacidad del equipo en redactar las páginas documentales de todos los microservicios, aplicaciones y gateways. Además, se confeccionarán todos los diagramas finales (C4 Model y DER) y la serie completa de Anexos (Vistas, Atributos de calidad, APIs, Lecciones aprendidas, Bugs, etc.).
* **Preparación para la Demo:** El desarrollo activo se enfocará en pulir la interacción e imagen de "Botín", realizando un testeo integral de su funcionalidad para asegurar una presentación impecable.
* **Infraestructura y datos:** Se configurará un club de prueba robusto (con disciplinas, cuotas, eventos y productos) y se procederá a separar las aplicaciones de socios y empleados a nivel de Firebase para mayor seguridad y orden.

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

* **Sobrecarga por volumen de redacción:** La cantidad de documentación requerida (manuales, múltiples diagramas arquitectónicos y anexos) es masiva y podría desfasar los tiempos del sprint.
* **Mitigación:** Se ha categorizado y distribuido fuertemente la carga documental desde el primer día del sprint. No se tomarán nuevas tareas de código complejas más allá de las necesarias para la Demo.
* **Inestabilidad en la presentación:** Que el bot o la maqueta fallen durante las pruebas de la Demo. Se destinarán tareas exclusivas de testeo funcional para blindar la experiencia antes del cierre.

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
    const SPRINT_ACTUAL = 11;
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
        contenedor.innerHTML = '<p style="margin:0; color:#555;">No se registran tareas asignadas a este criterio dentro del Sprint planning N°11.</p>';
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
