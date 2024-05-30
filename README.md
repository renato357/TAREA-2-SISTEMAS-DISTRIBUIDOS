# TAREA 2: Sistema de Gestión de Pedidos con Apache Kafka

Este repositorio contiene el código y los recursos relacionados con el proyecto de implementación y evaluación de un sistema de gestión de pedidos para un servicio de delivery, utilizando Apache Kafka.

## Descripción

El proyecto tiene como objetivo principal diseñar e implementar un sistema escalable y de alta disponibilidad para la gestión de pedidos, aprovechando las funcionalidades de Apache Kafka. El sistema se compone de tres servicios principales: Solicitud, Procesamiento y Notificación. Se utiliza Kafka para la transmisión de datos entre estos servicios, aprovechando su arquitectura distribuida y modelo pub-sub.

## Estructura del Repositorio

- `src/`: Directorio que contiene el código fuente de los servicios implementados.
  - `solicitud/`: Código del servicio de solicitud que recibe y publica pedidos en Kafka.
  - `procesamiento/`: Código del servicio de procesamiento que consume y procesa los pedidos.
  - `notificación/`: Código del servicio de notificación que informa el estado de los pedidos.
- `report/`: Directorio que contiene el informe final del proyecto.
- `tests/`: Directorio que contiene los scripts de prueba y los conjuntos de datos utilizados para las pruebas.

## Video

El enlace para ver el vídeo que muestra el funcionamiento del código con explicaciones es: [Video del proyecto](https://drive.google.com/file/d/1ZGgol_dI9wat6oivdzzq3Bci1xQscC4z/view?ts=6625dcd6)

## Informe Final

El informe final del proyecto se encuentra en el directorio `report/`. Incluye un análisis detallado de los resultados obtenidos, comparaciones entre los diferentes escenarios de carga y respuestas a las preguntas planteadas en el enunciado del proyecto.

## Contacto

Si tienes preguntas o comentarios sobre este proyecto, no dudes en ponerte en contacto con nosotros:

- **José Martín Berríos Piña**
  - Correo electrónico: jose.berrios1@mail.udp.cl

- **Renato Óscar Benjamín Contreras Carvajal**
  - Correo electrónico: renato.contreras@mail.udp.cl
