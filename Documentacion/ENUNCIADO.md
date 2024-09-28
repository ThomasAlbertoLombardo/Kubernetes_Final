# Práctica: Despliegue de una aplicación en Kubernetes

<p align="center">
    <img src="img/diagram.png" alt="application with database" width="500"/>
</p>

## Objetivo General
Desplegar una aplicación con una base de datos en Kubernetes utilizando Helm, asegurando que la aplicación sea accesible, escalable y que los datos se almacenen de forma persistente. La aplicación puede ser pública (e.g. Wordpress) o cualquier otra aplicación que se conecte a una base de datos (e.g. otra aplicación que hayáis desarrollado en otro curso de KeepCoding).

## Objetivos Específicos
- **Crear un chart de Helm**: Desarrollar un chart de Helm que incluya todos los recursos necesarios para desplegar la aplicación en Kubernetes.
- **Configurar la Persistencia de Datos**: Implementar un mecanismo que asegure que los datos de la base de datos sean almacenados de manera duradera.
- **Gestionar Configuración Sensible**: Asegurar que las credenciales y configuraciones sensibles se manejen de forma segura, utilizando los recursos adecuados de Kubernetes y evitando cualquier tipo de información sensible en el repositorio.
- **Asegurar Alta Disponibilidad (HA)**: La aplicación deberá estar siempre disponible configurando un mínimo número de réplicas que asegure una alta disponibilidad.
- **Escalar la Aplicación de manera automática**: El despliegue de la aplicación debe ser escalable, permitiendo ajustar el número de réplicas en base al uso de CPU. Esta configuración debe estar expuesta en el chart para poder ajustarse mediante el fichero values.yaml. Por defecto la aplicación debe escalar cuando supere el 70% de uso de CPU.
- **Exponer la Aplicación al exterior**: Configurar los recursos necesarios para que la aplicación sea accesible desde fuera del clúster de Kubernetes.
- **Garantizar la resiliencia de la Aplicación**: La aplicación deberá poder recuperarse ante errores. Aplicar el mecanismo que nos permite reiniciar la aplicación cuando no está funcionando y evitar que llegue tráfico a los PODs que no responden correctamente.
- **Documentación**: Elaborar una documentación clara que explique cómo desplegar y gestionar la aplicación utilizando el chart de Helm creado.

## Entrega
- **Chart de Helm Completo**: Entrega un chart de Helm que cumpla con todos los objetivos planteados.
- **Documentación**: Incluye un archivo README que explique cómo instalar y desplegar la aplicación, cómo ajustar configuraciones y cómo escalar la aplicación.
- **Evidencia Visual**: Adjunta capturas de pantalla o un vídeo corto que demuestre el funcionamiento de la aplicación desplegada.
- **Repositorio GitHub**: La práctica ha de entregarse como repositorio GitHub dentro de la organización KeepCoding, no se aceptarán entregas en cuentas de GitHub personales, ya sean los repositorios públicos o privados.
- **Formulario Oficial**: La entrega ha de comunicarse mediante el formulario oficial de entrega, no se aceptan o revisan entregas comunicadas por ningún otro medio.

## Criterios de Evaluación
- **Funcionamiento Completo**: El chart de Helm debe permitir el despliegue correcto de la aplicación junto a la base de datos, y la aplicación debe ser accesible cumpliendo con los objetivos planteados.
- **Buenas prácticas**: Se valorará el uso correcto de los objetos (Deployments, Statefulsets, Services…) y el uso de buenas prácticas.
- **Gestión Segura de Configuraciones**: La implementación debe garantizar que las credenciales y configuraciones sensibles estén protegidas. 
- **Escalabilidad**: Se evaluará la capacidad de escalar la aplicación a través de la configuración en el chart de Helm.
- **Calidad de la documentación**: El README debe ser claro, completo y debe guiar correctamente en la instalación y uso del chart de Helm.