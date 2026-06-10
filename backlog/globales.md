---
layout: default
title: Backlog global
parent: Backlog
nav_order: 1
---

# Backlog global del proyecto

A continuación se detalla el árbol de todas las tareas e historias de usuario planificadas para el ciclo de vida completo del proyecto, agrupadas dinámicamente según su Épica o naturaleza técnica.

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
    const contenedor = document.getElementById('arbolBacklogContenedor');
    let htmlTotal = '';
    if (tareasData.length > 0) {
      let mapaCategorias = {};
      tareasData.forEach(function(t) {
        let cat = t.categoria || "Otras Tareas";
        if (!mapaCategorias[cat]) {
          mapaCategorias[cat] = [];
        }
        mapaCategorias[cat].push(t);
      });
      const listaCategorias = Object.keys(mapaCategorias).sort(function(a, b) {
        let catA = a.toLowerCase();
        let catB = b.toLowerCase();
        if (catA.startsWith("épica") && catB.startsWith("épica")) {
          return catA.localeCompare(catB);
        }
        if (catA.startsWith("épica")) return -1;
        if (catB.startsWith("épica")) return 1;
        return catA.localeCompare(catB);
      });
      listaCategorias.forEach(function(catName) {
        htmlTotal += `<details style="margin-bottom:15px; border:1px solid #ddd; padding:10px; border-radius:5px; background:#fdfdfd;">`;
        htmlTotal += `<summary style="font-size:1.2em; font-weight:bold; cursor:pointer; color:#7253ed;">📂 ${catName}</summary>`;
        htmlTotal += `<div style="margin-top:10px; padding-left:15px;">`;
        htmlTotal += `<ul style="margin:0; padding-left:20px;">`;
        mapaCategorias[catName].forEach(function(tarea) {
          const completada = tarea.sprint_completado !== null;
          const icono = completada ? '✅' : '⏳';
          const badge = completada ? `<span style="color:#2ecc71; font-weight:bold;">[Hecho]</span>` : `<span style="color:#e67e22; font-weight:bold;">[Pendiente]</span>`;
          let resp = tarea.responsable ? tarea.responsable.charAt(0).toUpperCase() + tarea.responsable.slice(1) : 'A definir';
          let planificadoStr = tarea.sprint_planificado ? "Sprint " + tarea.sprint_planificado : "Sin planificar";
          htmlTotal += `<li style="margin-bottom:8px;">${icono} <strong>${tarea.titulo}</strong> ${badge}<br><span style="font-size:0.85em; color:#666;">ID: <code>${tarea.id}</code> | Puntos: <strong>${tarea.puntos} pts</strong> | Planificado: <strong>${planificadoStr}</strong> | Asignado: <em>${resp}</em></span></li>`;
        });
        htmlTotal += `</ul></div></details>`;
      });
    }
    if (htmlTotal === '') {
      contenedor.innerHTML = '<p>No se registran tareas cargadas en el backlog general.</p>';
    } else {
      contenedor.innerHTML = htmlTotal;
    }
  })();
</script>
