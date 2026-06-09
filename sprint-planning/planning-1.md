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

Se definió trabajar sobre todas las historias de usuario correspondientes a las **Épicas 1 y 2**.

### Historias de usuario

<details markdown="1">
<summary><strong>Épica 1: Accesos y Seguridad</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

<details markdown="1">
<summary><strong>HU-1.1 Login de Usuario Administrativo (documentacion#6)</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

**Criterios de aceptación:**

* **Dado que** el usuario ingresa credenciales válidas, **cuando** presiona "Ingresar", **entonces** el sistema lo redirige al Dashboard principal.
* **Dado que** el usuario ingresa credenciales no válidas, **entonces** el sistema no le permite el ingreso y le aparece un mensaje explicando el motivo.

**Sub-issues:**

* Inicio de sesión de usuario administrativo (vista) `plataforma-web#1` - *Responsable/s: Axel*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).
* Inicio de sesión de usuario administrativo (gateway) `gateway#1` - *Responsable/s: Lautaro*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Medio (3 puntos).
* Inicio de sesión de usuario administrativo (autenticación) `microservicio-autenticacion#1` - *Responsable/s: Martín*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Medio (3 puntos).

</details>

<details markdown="1">
<summary><strong>HU-1.2 Gestión de Roles y Permisos (documentacion#7)</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

**Criterios de aceptación:**

* **Dado que** el Super Administrador accede a la sección de configuración de seguridad, **cuando** guarda un nuevo rol o edita uno existente con permisos específicos, **entonces** el sistema actualiza la base de datos de accesos correctamente.
* **Dado que** un usuario administrativo inicia sesión, **cuando** el sistema carga el menú de navegación, **entonces** solo debe renderizar las opciones y módulos para los cuales el usuario tiene permisos explícitos.

**Sub-issues:**

* Gestión de roles y permisos (vista) `plataforma-web#4` - *Responsable/s: Axel*
    * **Prioridad:** Media.
    * **Esfuerzo:** Bajo (1 punto).
* Gestión de roles y permisos (gateway) `gateway#4` - *Responsable/s: Lautaro*
    * **Prioridad:** Media.
    * **Esfuerzo:** Medio (3 puntos).
* Gestión de roles y permisos (autenticacion) `microservicio-autenticacion#4` - *Responsable/s: Martín*
    * **Prioridad:** Media.
    * **Esfuerzo:** Bajo (1 punto).
* Gestión de roles y permisos (core) `microservicio-club#2` - *Responsable/s: Axel*
    * **Prioridad:** Media.
    * **Esfuerzo:** Medio (3 puntos).

</details>

<details markdown="1">
<summary><strong>HU-1.3 ABM de Usuarios Administrativos (documentacion#8)</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

**Criterios de aceptación:**

* **Dado que** el Super Administrador completa el formulario de alta de personal, **cuando** ingresa un correo electrónico válido y confirma la acción, **entonces** el sistema crea la cuenta y envía un enlace automático a ese correo para la generación de la contraseña.
* **Dado que** un empleado ya no pertenece al club, **cuando** el Super Administrador ejecuta la acción de baja sobre su usuario, **entonces** el sistema cambia su estado lógico a "Inactivo" (Soft Delete) manteniendo intactos los registros históricos de sus operaciones.

**Sub-issues:**

* ABM usuarios administrativos (vista) `plataforma-web#2` - *Responsable/s: Axel*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).
* ABM usuarios administrativos (gateway) `gateway#2` - *Responsable/s: Lautaro*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Medio (3 puntos).
* ABM usuarios administrativos (autenticación) `microservicio-autenticacion#2` - *Responsable/s: Martín*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).
* ABM usuarios administrativos (core) `microservicio-club#1` - *Responsable/s: Axel*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Medio (3 puntos).

</details>

</details>

<details markdown="1">
<summary><strong>Épica 2: Gestión Societaria</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

<details markdown="1">
<summary><strong>HU-2.1 ABM de Socios (documentacion#9)</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

**Criterios de aceptación:**

* **Dado que** un administrativo está registrando un nuevo socio, **cuando** ingresa un número de DNI que ya se encuentra activo en el padrón, **entonces** el sistema debe mostrar un mensaje de error y bloquear la creación del registro.
* **Dado que** el administrativo completa el formulario de alta de socio, **cuando** ingresa la fecha de nacimiento, **entonces** el sistema debe calcular la edad y asignar automáticamente la categoría societaria correspondiente (ej. Cadete, Activo).

**Sub-issues:**

* ABM socios (vista) `plataforma-web#3` - *Responsable/s: Axel*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).
* ABM socios (gateway) `gateway#3` - *Responsable/s: Lautaro*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Medio (3 puntos).
* ABM socios (autenticación) `microservicio-autenticacion#3` - *Responsable/s: Martín*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).
* ABM socios (core) `microservicio-club#4` - *Responsable/s: Axel*
    * **Prioridad:** Alta.
    * **Esfuerzo:** Bajo (1 punto).

</details>

<details markdown="1">
<summary><strong>HU-2.2 Consulta 360 del Socio (documentacion#10)</strong> - <em>Responsable/s: Axel, Lautaro y Martín</em></summary>

**Criterios de aceptación:**

* **Dado que** el administrativo necesita localizar a un miembro, **cuando** ingresa un número de DNI, apellido o número de socio en la barra de búsqueda global, **entonces** el sistema debe listar los perfiles coincidentes.
* **Dado que** el administrativo selecciona a un socio de los resultados de búsqueda, **cuando** se carga la "Vista 360", **entonces** el sistema debe mostrar consolidados los datos personales, el estado de pagos y el último ingreso detectado.

**Sub-issues:**

* Consulta del Socio (vista) `plataforma-web#5` - *Responsable/s: Axel*
    * **Prioridad:** Media.
    * **Esfuerzo:** Bajo (1 punto).
* Consulta del Socio (gateway) `gateway#5` - *Responsable/s: Lautaro*
    * **Prioridad:** Media.
    * **Esfuerzo:** Medio (3 puntos).
* Consulta del Socio (autenticación) `microservicio-autenticacion#5` - *Responsable/s: Martín*
    * **Prioridad:** Media.
    * **Esfuerzo:** Medio (3 puntos).
* Consulta del socio (core) `microservicio-club#3` - *Responsable/s: Axel*
    * **Prioridad:** Media.
    * **Esfuerzo:** Medio (3 puntos).

</details>

</details>

### Tareas de documentación

<details markdown="1">
<summary><strong>documentacion #36</strong>: Redactar múltiples variantes de la presentación breve de "SocioUnido" - <em>Responsable: Felipe</em></summary>

* Prioridad: Alta.
* Esfuerzo: Medio (3 puntos).

</details>

<details markdown="1">
<summary><strong>documentacion #37</strong>: Crear primera versión de la presentación para la entrega intermedia - <em>Responsable: Felipe</em></summary>

* Prioridad: Alta.
* Esfuerzo: Alto (5 puntos).

</details>

<details markdown="1">
<summary><strong>scrum #1</strong>: Documentar ceremonias de Scrum y métricas de la iteración N°1 - <em>Responsable: Felipe</em></summary>

* Prioridad: Alta.
* Esfuerzo: Medio (3 puntos).

</details>

<details markdown="1">
<summary><strong>scrum #2</strong>: Definir la primer hoja de ruta para el MVP inicial - <em>Responsable: Axel, Felipe, Lautaro y Martín</em></summary>

* Prioridad: Urgente.
* Esfuerzo: Medio (3 puntos).

</details>

<details markdown="1">
<summary><strong>scrum #3</strong>: Crear la página web documental de 'Scrum' y 'Hoja de ruta' - <em>Responsable: Felipe</em></summary>

* Prioridad: Alta.
* Esfuerzo: Alto (5 puntos).

</details>

<details markdown="1">
<summary><strong>bitacora #2</strong>: Hacer la bitácora de la semana 13 - <em>Responsable: Felipe</em></summary>

* Prioridad: Media.
* Esfuerzo: Bajo (1 punto).

</details>

## ⚠️ Riesgos y dependencias

* **Arquitectura de microservicios:** Posibles inconvenientes a la hora de crear e interconectar todos los microservicios, bases de datos e interfaces de usuario entre sí. Se prestará principal atención a esto durante el transcurso del ciclo.
* **Dinámica de trabajo:** Al ser el primer Sprint, existe el desafío natural del funcionamiento del equipo en su conjunto, la adaptación a los repositorios separados y el ciclo de revisión de código.
* **Limitación de tiempo:** El tiempo reducido de este primer Sprint (4 días en lugar del ciclo habitual) podría afectar el volumen total de cierre de tareas.
