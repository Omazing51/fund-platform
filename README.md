# fund-platform
# README - Despliegue de Frontend y Backend con AWS CloudFormation

Este documento describe el paso a paso para desplegar el proyecto **Funds** (frontend + backend FastAPI) usando una única plantilla de **AWS CloudFormation**.

---

## 1. Prerrequisitos
Antes de iniciar, se debe tener en cuenta lo siguiente:
- Una cuenta AWS activa.
- AWS CLI instalado y configurado ("aws configure").
- Docker instalado y en funcionamiento.
- Permisos de administrador para crear recursos (S3, CloudFront, ECS, ECR, IAM).

---

## 2. Empaquetar y subir la imagen del backend a ECR
1. Crear un repositorio en **ECR**:
   bash
   aws ecr create-repository --repository-name funds-backend --region us-east-1
   
2. Obtener el URI del repositorio creado.
3. Loguearse en ECR:
   bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ECR_URI>
   
4. Construir la imagen del backend (FastAPI):
   bash
   docker build -t funds-backend ./fund-platform
   
5. Etiquetar y subir:
   bash
   docker tag funds-backend:latest <ECR_URI>:latest
   docker push <ECR_URI>:latest
   

---

## 3. Desplegar la plantilla CloudFormation
1. Subir el archivo "cloudformation.yml" a tu máquina o entorno.
2. Ejecutar:
   bash
   aws cloudformation create-stack \
     --stack-name funds-stack \
     --template-body file://cloudformation.yml \
     --capabilities CAPABILITY_IAM
   
3. Esperar a que el stack finalice ("CREATE_COMPLETE").

## 4. Cargar el frontend en S3
1. Se tiene el frontend listo:
   bash
   cd frontend/funds_frontend
   npm install
   npm run build
   
2. Subir el contenido de "dist/" al bucket S3 creado por el stack:
   bash
   aws s3 sync dist/ s3://<BUCKET_NAME> --delete
   
## 5. Probar el despliegue
- **Frontend**: acceder a la URL de **CloudFront** provista por CloudFormation.
- **Backend**: acceder a la URL del **ALB** o endpoint API.

## 6. Limpieza de recursos
Para evitar costos, eliminar el stack:
bash
aws cloudformation delete-stack --stack-name funds-stack
