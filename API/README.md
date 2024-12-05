<<<<<<< HEAD
# PRO_UF1/API

Exercici Pràctic: API d'Alumnes amb FastAPI
Aquest projecte implementa una API per gestionar alumnes utilitzant FastAPI i una base de dades MariaDB. L'API permet realitzar operacions CRUD (Crear, Llegir, Actualitzar, Eliminar) sobre una base de dades d'alumnes i les seves relacions amb la aula a la que estudian.

1. GET /alumne/list
Descripció: Retorna una llista de tots els alumnes.
Resposta: JSON amb la informació de tots els alumnes.
2. GET /alumne/show/{id}
Descripció: Retorna la informació d'un alumne específic, donant la seva id.
Resposta: JSON amb les dades de l'alumne.
3. POST /alumne/add
Descripció: Afegeix un nou alumne a la base de dades.
Cos: JSON amb la informació del nou alumne.
Resposta: Missatge JSON confirmant que s'ha afegit correctament.
4. PUT /alumne/update/{id}
Descripció: Actualitza la informació d'un alumne existent.
Cos: JSON amb els camps a modificar.
Resposta: Missatge JSON confirmant que s'ha modificat correctament.
5. DELETE /alumne/delete/{id}
Descripció: Elimina un alumne de la base de dades per la seva id.
Resposta: Missatge JSON confirmant que s'ha eliminat correctament.
6. GET /alumne/listAll
Descripció: Retorna la informació de tots els alumnes juntament amb les dades de la seva aula, edifici i pis.
Resposta: JSON amb la informació detallada de l'alumne i l'aula.
=======
# PRO_UF1
>>>>>>> 4c0129e03436393457fdb9744c25a1f3e49d48e9
