## Guía de Instalación

Esta guía te llevará a través de los pasos necesarios para instalar y desplegar la aplicación de contador con Redis en un clúster de Kubernetes usando Minikube y Helm.

## Requisitos Previos

- **Docker**: Asegúrate de tener Docker instalado y funcionando.
- **Minikube**: Necesitarás Minikube para crear un clúster local de Kubernetes.
- **Kubectl**: La herramienta de línea de comandos para interactuar con Kubernetes.
- **Helm**: El gestor de paquetes para Kubernetes.

## Pasos de Instalación

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto:

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
```

### 2. Iniciar Minikube

Inicia Minikube para crear tu clúster local:

```bash
minikube start
```

### 3. Construir la imagen Docker

Construye la imagen Docker de la aplicación:

```bash
docker build -t thomasalberto/counter-app:v2 .
```

### 4. Cargar la imagen en Minikube

Carga la imagen Docker en el entorno de Minikube:

```bash
minikube image load thomasalberto/counter-app:v2
```

### 5. Desplegar la Aplicación con Helm

Usa Helm para desplegar la aplicación en el clúster:

```bash
helm install counter-app ./helm-chart/counter-app
```

### 6. Verificar los Pods

Asegúrate de que todos los pods estén en ejecución:

```bash
kubectl get pods
```

### 7. Configurar el Acceso Local

Si estás usando Minikube, añade una entrada en tu archivo hosts para acceder a la aplicación:

```bash
echo "$(minikube ip) counter.local" | sudo tee -a /etc/hosts
```

En Windows, edita C:\Windows\System32\drivers\etc\hosts manualmente con permisos de administrador.

### 8. Acceder a la Aplicación

Abre tu navegador y accede a la aplicación en:

```bash
http://counter.local
```

### Solución de Problemas Comunes
#### - Problemas de Conexión: Asegúrate de que Minikube esté corriendo y que la IP sea correcta.
#### - Errores al Construir la Imagen: Verifica que Docker esté funcionando correctamente y que estés en el directorio correcto.
Para más detalles, consulta las otras guías incluidas en este proyecto