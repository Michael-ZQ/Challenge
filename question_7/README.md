# Question 7

## Preguntas adicionales sobre AWS

**1. ¿Cuál de los siguientes servicios AWS NO está relacionado con el almacenamiento?**
 - S3
 - EBS
 - EC2
 - Glacier


    Amazon Elastic Compute Cloud (EC2) es un servicio de computación en la nube.

**2. ¿Cuál de las siguientes afirmaciones acerca de la Elasticidad de AWS es correcta?**
  - La Elasticidad se refiere a la capacidad de AWS para manejar aumentos rápidos en la demanda
  - AWS no puede escalar automáticamente para satisfacer la demanda 
  - AWS requiere que los usuarios prevean la demanda con antelación 
  - Todas las anteriores


    La Elasticidad se refiere a la capacidad de AWS para manejar aumentos rápidos en la demanda. 

**3. ¿Qué servicio AWS se utiliza para la transmisión de datos en tiempo real?**
  - Amazon Athena 
  - Amazon Kinesis 
  - AWS Batch 
  - Amazon EMR


    Amazon Kinesis permite capturar, procesar y analizar grandes volúmenes de datos en tiempo real. 

**4. ¿Cómo se conoce a la región geográfica en la que se encuentran los servidores de AWS?**
  - Zona de Disponibilidad 
  - Zona de Seguridad 
  - Área de Almacenamiento 
  - Region

    
    Regiones, una región es una ubicación geográfica física en la que se encuentran los centros de datos de AWS.

## Preguntas sobre microservicios en AWS

**1. ¿Cuál de los siguientes es un servicio de AWS que ayuda a administrar microservicios?** 
- AWS Amazon Elastic Container Service (ECS) 
- Amazon S3
- Amazon DynamoDB
- Amazon EMR

    
    AWS Amazon Elastic Container Service permite ejecutar, detener y 
    administrar contenedores Docker en un clúster de instancias de EC2.


**2. ¿Si estás implementando un microservicio en AWS y quieres monitorizar su rendimiento, ¿qué servicio usarías?**
- AWS XRay
- AWS Rekognition
- AWS Snowball 
- AWS Redshift

    
    AWS X-Ray es un servicio de monitoreo y análisis de aplicaciones, incluidos los microservicios.

**3. ¿Qué servicio de AWS sería más apropiado para implementar una 
    arquitectura basada en eventos para tus microservicios?**
- Amazon S3
- Amazon SQS
- Amazon Lambda
- Amazon Route 53


    Amazon SQS, podemos implementar una arquitectura basada en eventos, 
    donde los microservicios se comunican mediante el envío y recepción de mensajes en colas.


**4. ¿Cuál de las siguientes afirmaciones es correcta respecto a la seguridad de los microservicios en AWS?**
- Cada microservicio debería tener su propia política de seguridad
- Todos los microservicios deben compartir la misma política de seguridad
- Los microservicios no necesitan políticas de seguridad
- Las políticas de seguridad son gestionadas por AWS, por lo que los usuarios no necesitan preocuparse por ellas

    
    Cada microservicio debería tener su propia política de seguridad.