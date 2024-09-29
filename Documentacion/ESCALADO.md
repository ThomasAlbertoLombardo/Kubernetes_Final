# Guía de Escalado

Esta guía explica cómo escalar la aplicación de contador en Kubernetes.

## Escalado Horizontal

Ajusta el número de réplicas para manejar más tráfico:

1. Edita el archivo `values.yaml`:
   - Cambia `replicaCount` al número deseado.

2. Aplica los cambios con Helm:

```bash
helm upgrade counter-app ./helm-chart/counter-app
```

### Escalado Automático

Configura el escalado automático basado en métricas como CPU:

1. **Crea un Horizontal Pod Autoscaler**:

```bash
kubectl autoscale deployment counter-app-counter-app --cpu-percent=50 --min=2 --max=10
```

2. **Verifica el estado del HPA:**:
```bash
kubectl get hpa
```
### Consideraciones para el Escalado

- **Rendimiento**: Asegúrate de que tu clúster tenga suficientes recursos para soportar el escalado.
- **Pruebas**: Realiza pruebas de carga para determinar los límites óptimos antes del escalado.
