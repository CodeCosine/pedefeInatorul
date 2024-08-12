# IMPORTANT
! Acest API este pus pe contul beneficiarului si nu v-a fi actualizat decat și DOAR la dorinta sa de alte modificari.
Link-ul original este https://github.com/AndreiOp235/pedefeInatorul

© Copyright 2023

---
# Intro
Refuz sa cred necesitatea unui API separat pentru a transforma un PDF la PNG.
Acest API este hostat prin platforma RENDER

' bonus se selecteaza doar partea utila din document
# Utilizare
1. Accesand https://flask-hello-world-xi0b.onrender.com/ si incarcand un document in format PDF. Outputul va fi o captura a primei pagini in format PNG
2. Trimitand un request de tip POST catre https://flask-hello-world-xi0b.onrender.com/convert avand ca payload raw-text sub forma
   { "pdf_base64": "<fisier PDF encoded as base64>" }
Raspunsul primit va fi un raw-text sub forma
  {"png_base64":"<fisier PNG encoded as base64>"}

   Ce urmeaza este readME-ul de la proiectul folosit ca si template

# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.


