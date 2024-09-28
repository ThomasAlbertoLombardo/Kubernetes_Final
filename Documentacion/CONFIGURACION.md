# Guía de Configuración

Esta guía detalla cómo ajustar las configuraciones de la aplicación de contador desplegada en Kubernetes.

## Archivos de Configuración

### 1. `values.yaml`
Este archivo contiene las configuraciones principales para Helm. Aquí puedes ajustar:

- **Imagen Docker**: Cambia la etiqueta de la imagen si necesitas actualizarla.
  - `image.repository`: `thomasalberto/counter-app`
  - `image.tag`: `v2`
  
- **Recursos**: Define los límites de CPU y memoria.
  - `resources.requests.cpu`: `"100m"`
  - `resources.requests.memory`: `"128Mi"`
  - `resources.limits.cpu`: `"200m"`
  - `resources.limits.memory`: `"256Mi"`
  
- **Réplicas**: Ajusta el número de réplicas para escalar la aplicación.
  - `replicaCount`: `3`

### 2. ConfigMap
El `ConfigMap` almacena configuraciones específicas de la aplicación:

- **REDIS_HOST**: Dirección del servicio Redis.
  - Asegúrate de que coincida con el nombre del servicio Redis en Kubernetes.

Para editar el `ConfigMap`, usa:
```bash
kubectl edit configmap counter-app-counter-config
