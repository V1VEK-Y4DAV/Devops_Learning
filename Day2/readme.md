# (a) Create a repository {chat-app}

# (b) Create few branches
- dev → code  write MVP ( Minimum viable product )
- test → test the existing code for edge cases
- prod → production team ensures the code that it is production ready  

# (c) Containerise the working app
[ code → Image ]

image  
- .iso → OS image  
- .exe → executable  
- .dmg → mac  
- .apk → android  

Docker → Containerization tool

Production team ka kaam hota hai code ko image me containerise karna → matlab multiple file ko ek package me banana ki containerization.

ek application me:

- main.py → actual origin  
- requirements.txt → requirement  

ye run se hum padenge


program sirf ek hi image me hi sab pack hoga  
Sab kuch hoga  
ek doosre se dependency hogi  
version change hoga  
ek same command lage

---

# (2)

image (file) → extract files  
- .bin  
- .iso  
- .exe  
- .env  
- .etc  

hum is image ko extract karte hai

---

## (d) Store these container images into Registry

ek bar humne pass image hai  
store these container images in registry

container image ek registry me store hogi

image → service bana ke deployment karna  
scale karna multiple

---

## Docker

Docker image = store nahi  
store hoga → Docker Hub Registry

---

## Source Code

repository me store hota hai

container image ek registry me store hoti hai

---

# (e) Container orchestration tool

[Kubernetes]

- Pods  
- Replica sets  
- Deployments  
- services  
- nodes  
- cluster  

pod ke andar ek container hota hai  
pod ke andar multiple container bhi ho sakte hai

pod ke andar container image ko pull karega

---

# (3)

## Containerization {app}

### (a) app

Dockerfile → app ke root directory me


---

## (b) docker build -t point:v1

image → blueprint / template

application code + dependencies + runtime

docker container = running instance of image

---

## containerization → application ko image bana kar container me run karna