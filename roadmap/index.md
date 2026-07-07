---
layout: default
title: Hoja de ruta
nav_order: 2
has_children: true
---

# Hoja de ruta estratégica

En esta sección detallamos la hoja de ruta del proyecto, estructurando el desarrollo en fases claras e iterativas.

## Planificación del primer MVP (Sprints 1 al 10)

El desarrollo de este MVP está segmentado en cuatro grandes fases, garantizando entregas de valor continuo, testeo temprano y un margen de tiempo seguro para imprevistos.

### Fase 1: Estructura base y plataforma Web de gestión

El objetivo inicial es establecer los cimientos de la arquitectura (microservicios) y habilitar el panel administrativo para la gestión integral del club.

* **Sprint 1: Iniciación y seguridad**
  * Creación de la estructura web e interconexiones iniciales entre microservicios.
  * **Épica 1 (Accesos y Seguridad):** Login, registro, baja de usuarios administrativos y gestión de roles.
  * **Épica 2 (Gestión Societaria):** Consulta integral del socio (cuotas, reservas, último login).

* **Sprints 2, 3 y 4: Operaciones y dashboard**
  * **Épica 3 (Gestión Operativa):** ABM de reservas; administración de disciplinas y consulta de socios inscriptos.
  * **Épica 4 (Comunicación y Retención):** Configuración y envío de alertas a socios; publicación de noticias.
  * **Épica 5 (Dashboard Analítico):** Métricas (recaudación, morosidad, accesos, uso de espacios, etc.); ABM de socios y métricas predictivas de fidelización.
  * Retrospectiva de la plataforma web, refinamiento de la UI y ajuste de microservicios.

* **Sprints 5: Testeo y refinamiento**
  * Testeo integral (End-to-End) de toda la plataforma web.
  * Corrección de bugs y refinamiento general de la interfaz y la experiencia de usuario (UX/UI).
  * Retrospectiva final del panel web, análisis de resultados y planificación de mejoras para futuras iteraciones.

### Fase 2: Aplicación móvil (Socios y empleados)

Una vez estabilizado el panel web, el enfoque se traslada a la interfaz de usuario final, permitiendo la autogestión de los socios y herramientas de control para los empleados en campo.

* **Sprint 6, 7 y 8: Iniciación móvil y autogestión**
  * Creación de la aplicación móvil y sus primeras interconexiones.
  * **Épica 6 (Perfil y Autogestión):** Login de socios, cambio de contraseña, manejo de perfil, ABM de reservas propias y consulta de estado de deuda.
  * **Épica 7 (Reservas y Deportes):** Consulta e inscripción a disciplinas; vista de espacios compartidos y formularios del club.
  * **Épica 8 (Pagos):** Pasarela para abono de cuotas, reservas, disciplinas y entradas.
  * **Épica 9 (Novedades):** Feed de noticias del club e interacción con la tienda de productos.
  * **Épica 10 (Rol Empleado):** Login específico para personal, manejo de perfil y escaneo de códigos QR para control de accesos.
  * Testeo integral (End-to-End) de toda la aplicación móvil.
  * Retrospectiva de la app móvil y refinamiento del ecosistema.

### Fase 3: Inteligencia artificial, automatización y testeo integral

Integración de herramientas avanzadas para optimizar la carga de soporte del club y mejorar la experiencia del usuario.

* **Sprints 9 y 10: Canal conversacional**
  * Desarrollo, entrenamiento del modelo e integración final con el resto de los microservicios.
  * **Épica 11 (Canal Conversacional):** Bot para responder consultas frecuentes de los usuarios de forma automática y envío de alertas/noticias proactivas.
  * Testeo integral (End-to-End) de toda la plataforma web y la aplicación móvil.
  * Corrección de bugs y refinamiento general de la interfaz y la experiencia de usuario (UX/UI).
  * Retrospectiva final del MVP, análisis de resultados y planificación de mejoras para futuras iteraciones.

### Ideas futuras para el segundo MVP

Durante el desarrollo de este primer MVP, se fueron identificando nuevas oportunidades de mejora y funcionalidades adicionales que podrían ser incorporadas en un segundo MVP, como:

- Rol de profesor/entrenador dentro de la plataforma web, quien puede gestionar sus propias clases, horarios y alumnos.
- Integración de un sistema de reservas para eventos especiales o torneos organizados por el club
- Sistema de notificaciones push.
