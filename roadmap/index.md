---
layout: default
title: Hoja de ruta
nav_order: 2
has_children: true
---

# Hoja de ruta estratégica

En esta sección detallamos la hoja de ruta del proyecto, estructurando el desarrollo del MVP en sus primeras 10 semanas (Sprints 1 al 10), luego la redacción de la documentación entregable y la preparación para la defensa final.

## Desarrollo del MVP (Sprints 1 al 10)

El desarrollo de este "MVP" está segmentado en grandes fases, garantizando entregas de valor continuo, testeo temprano y un margen de tiempo seguro para imprevistos.

### Fase 1: Estructura base y plataforma web de gestión

El objetivo inicial es establecer los cimientos de la arquitectura (microservicios) y habilitar el panel administrativo para la gestión integral del club.

* **Sprint 1: Iniciación y seguridad**
  * Creación de la estructura web e interconexiones iniciales entre microservicios.
  * **Épica 1 (Accesos y seguridad):** Login, registro, baja de usuarios administrativos y gestión de roles.
  * **Épica 2 (Gestión societaria):** Consulta integral del socio (cuotas, reservas, último login).

* **Sprints 2, 3 y 4: Operaciones y dashboard**
  * **Épica 3 (Gestión operativa):** ABM de reservas, administración de disciplinas y consulta de socios inscriptos.
  * **Épica 4 (Comunicación y retención):** Configuración/Envío de alertas a socios y publicación de noticias.
  * **Épica 5 (Dashboard analítico):** Métricas (Recaudación, morosidad, accesos, uso de espacios, etc.). ABM de socios y métricas predictivas de fidelización.
  * Retrospectiva de la plataforma web, refinamiento de la UX/UI y ajuste de microservicios.

* **Sprint 5: Testeo y refinamiento**
  * Testeo integral (End-to-End) de toda la plataforma web.
  * Corrección de bugs y refinamiento general de la interfaz y la experiencia de usuario.
  * Retrospectiva final del panel web, análisis de resultados y planificación de mejoras para futuras iteraciones.

### Fase 2: Aplicación móvil (Socios y empleados) e Inteligencia Artificial

Una vez estabilizado el panel web, el enfoque se traslada a la interfaz de usuario final, permitiendo la autogestión de los socios y herramientas de control para los empleados en campo.

* **Sprints 6, 7 y 8: Iniciación móvil y autogestión**
  * Creación de la aplicación móvil y sus primeras interconexiones.
  * **Épica 6 (Perfil y autogestión):** Login de socios, cambio de contraseña, manejo de perfil, ABM de reservas propias y consulta de estado de deuda.
  * **Épica 7 (Reservas y deportes):** Consulta e inscripción a disciplinas, vista de espacios compartidos y formularios del club.
  * **Épica 8 (Pagos):** Pasarela para abono de cuotas, reservas, disciplinas y entradas.
  * **Épica 9 (Novedades):** Feed de noticias del club e interacción con la tienda de productos.
  * **Épica 10 (Rol empleado):** Login específico para personal, manejo de perfil y escaneo de códigos QR para control de accesos.

* **Sprints 9 y 10: Canal conversacional y testeo integral**
  * Desarrollo, entrenamiento del modelo e integración final con el resto de los microservicios.
  * **Épica 11 (Canal conversacional):** Bot para responder consultas frecuentes de los usuarios de forma automática y envío de alertas/noticias proactivas.
  * Testeo integral (End-to-End) de toda la plataforma web y la aplicación móvil.
  * Corrección de bugs y refinamiento general de la interfaz y la experiencia de usuario (UX/UI).
  * Retrospectiva final del MVP, análisis de resultados y planificación de mejoras para futuras iteraciones.

## Consolidación y documentación final (Semanas 11 a 13)

Tras concluir el desarrollo central del código, el enfoque principal del equipo se traslada a la formalización del proyecto.

* **Sprints 11, 12 y 13:** 
  * Redacción, revisión y finalización de toda la documentación entregable (Técnica, funcional y de gestión).
  * Consolidación de manuales de usuario y métricas finales del ciclo de vida del producto.

## Pulido final y preparación de la defensa (Semana 14 en adelante)

El tiempo restante del calendario se destinará exclusivamente a asegurar la máxima calidad del entregable y garantizar una presentación exitosa.

* **Refinamiento continuo:** Pulir detalles de UX/UI para asegurar que tanto la plataforma web como la app móvil ofrezcan una experiencia impecable.
* **Resolución de errores (Bug fixing):** Detección y corrección de pequeños *bugs* o fallos que puedan ser encontrados durante las pruebas de uso, asegurando la estabilidad total del ecosistema.
* **Validación de producto:** Realización de múltiples validaciones del sistema con posibles usuarios finales para seguir mejorando la aplicación y obtener el *feedback* necesario que fortalezca los argumentos de cara a la defensa final y la evolución de la solución.
* **Agregado de valor rápido:** Incorporar pequeñas funcionalidades o ajustes detectados durante el uso que aporten valor sin poner en riesgo la estabilidad del sistema.
* **Defensa final:** Preparación del discurso, armado de material visual, ensayos de la presentación y puesta a punto de los entornos de demostración para el jurado.

## Futuras líneas de desarrollo e iteraciones del producto

Durante el ciclo de desarrollo de esta primera versión funcional, se identificaron diversas oportunidades de mejora y características de alto valor añadido. A continuación, se documentan las principales funcionalidades proyectadas para las futuras expansiones del ecosistema:

* **Módulo de gestión de grupo familiar:** Vinculación de múltiples perfiles bajo la administración de un único socio titular, permitiendo la centralización de pagos, seguimiento de credenciales e inscripciones a disciplinas de todo el núcleo familiar desde una sola cuenta.
* **Rol de profesor y entrenador:** Incorporación de un nivel de acceso específico en la plataforma web para que el personal deportivo pueda gestionar sus propias clases, realizar el seguimiento de sus alumnos y administrar sus grillas horarias.
* **Gestión de fondos multi-cuenta:** Capacidad de configurar múltiples cuentas bancarias de destino, permitiendo a las instituciones derivar y organizar su recaudación en distintos fondos (por ejemplo, separar los ingresos de la cuota social de los de la tienda o disciplinas).
* **Ampliación de pasarelas de pago:** Integración con proveedores y pasarelas de pago externas adicionales, brindando a los clubes la capacidad de ofrecer una mayor flexibilidad y variedad de métodos de cobro a sus asociados.
* **Sincronización con hardware de acceso:** Integración directa de la plataforma y el carnet digital (código QR) con molinetes físicos y sistemas de control de acceso automatizado en las instalaciones de los clubes.
