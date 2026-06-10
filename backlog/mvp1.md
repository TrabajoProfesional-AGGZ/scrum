---
layout: default
title: Backlog del primer MVP
parent: Backlog
nav_order: 1
---

# Backlog del Primer MVP (Sprint 1 a 10)

A continuación se detalla el árbol de tareas planificadas para el ciclo inicial, clasificadas por el Sprint asignado y agrupadas internamente según su Épica o naturaleza técnica.

<div id="arbolBacklogContenedor"></div>

<script type="application/json" id="backlog-data">
{% if site.data.backlog %}{{ site.data.backlog | jsonify }}{% else %}[]{% endif %}
</script>

<script markdown="0">
  (function() {
    let tareasData = [];
    try {
      tareasData = JSON.parse(document.getElementById('backlog-data').textContent) || [];
    } catch(e) {
      console.error("Error al mapear el backlog:", e);
    }
    const NUM_SPRINTS = 10;
    const contenedor = document.getElementById('arbolBacklogContenedor');
    let htmlTotal = '';
    for (let s = 1; s <= NUM_SPRINTS; s++) {
      const tareasDelSprint = tareasData.filter(function(t) {
        return t.sprint_planificado === s;
      });
      if (tareasDelSprint.length > 0) {
        let mapaCategorias = {};
        tareasDelSprint.forEach(function(t) {
          let cat = t.categoria || "Otras Tareas";
          if (!mapaCategorias[cat]) {
            mapaCategorias[cat] = [];
          }
          mapaCategorias[cat].push(t);
        });
        htmlTotal += `<details style="margin-bottom:15px; border:1px solid #ddd; padding:10px; border-radius:5px; background:#fdfdfd;">`;
        htmlTotal += `<summary style="font-size:1.2em; font-weight:bold; cursor:pointer; color:#7253ed;">📅 Sprint N° ${s}</summary>`;
        htmlTotal += `<div style="margin-top:10px; padding-left:15px;">`;
        for (let catName in mapaCategorias) {
          htmlTotal += `<h4 style="margin-top:15px; margin-bottom:5px; color:#2c3e50; border-bottom:1px solid #eee; padding-bottom:3px;">📂 ${catName}</h4>`;
          htmlTotal += `<ul style="margin:0; padding-left:20px;">`;
          mapaCategorias[catName].forEach(function(tarea) {
            const completada = tarea.sprint_completado !== null;
            const icono = completada ? '✅' : '⏳';
            const badge = completada ? `<span style="color:#2ecc71; font-weight:bold;">[Hecho]</span>` : `<span style="color:#e67e22; font-weight:bold;">[Pendiente]</span>`;
            let resp = tarea.responsable ? tarea.responsable.charAt(0).toUpperCase() + tarea.responsable.slice(1) : 'A definir';
            htmlTotal += `<li style="margin-bottom:6px;">${icono} <strong>${tarea.titulo}</strong> ${badge}<br><span style="font-size:0.85em; color:#666;">ID: <code>${tarea.id}</code> | Puntos: <strong>${tarea.puntos} pts</strong> | Asignado: <em>${resp}</em></span></li>`;
          });
          htmlTotal += `</ul>`;
        }
        htmlTotal += `</div></details>`;
      }
    }
    if (htmlTotal === '') {
      contenedor.innerHTML = '<p>No se registran tareas cargadas en los Sprints del MVP actual.</p>';
    } else {
      contenedor.innerHTML = htmlTotal;
    }
  })();
</script>
