###### https://github.com/GoogleCloudPlatform/microservices-demo
###### http://cs.brown.edu/courses/csci2952-f/HWs.pdf

#### HW 1: Microservices Hello World (2/4 - 2/11)

#### HW 2: Enhanced Microservices (2/13 - 2/27)
* Hand-In: Codebase + project report.
* API Gateway: In particular, you will add an API-gateway (i.e., Ambassador) to
expose several of your internal services to the outside world. We will expose the
following services: RecommendationService, AdService, and CartService. There are
several API-gateway platforms in addition to Ambassador, and you are free to choose
one.
* Authentication: Next, you will setup OPA (Open Policy Agent) as an external entity
to perform authorization.

#### HW 3: Observability (3/3 - 3/12)
* Hand-In: Screenshots.
* In the second assignment, you will setup Zipkin (Or Jaeggar) to collect network telemetry
information from the microservice that you set up in assignment #1. A key benefit of using
Google’s microservice demo is that existing distributed tracing tools work with the demo.
Moreover, you will not need to add any specific tracing information to enable tracing.

#### HW 4: Bugs and Chaos (3/17 - 3/28)
* Hand-In: Codebase + project report.
* In the fourth assignment, you will explore the use of ChaoEngineering for testing and analysis. Istio and Kubernetes both include primitives to help with ChaosEngineering. Furthermore, orchestration platforms, e.g., Chaos Toolkit, exist to simplify chaos engineering. In particular, you will add two types of Chaos: adding latency and dropping connections.
There are several chaos orchestration platforms in addition to ChaosToolKit, and you are
free to choose one.

#### HW 5: Migration (4/2 - 4/16)
* Optional 
* In this last experiment, you will work to migrate one of several large scale microservices onto
a ServiceMesh. These services already come with tracing enabled. You will need to add and
setup Envoy and Istio for orchestration. You will also need to add an API-gateway to expose
a subset of the infrastructure.
