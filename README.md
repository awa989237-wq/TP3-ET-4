# School Manager — TP guidé 3

Projet Django de démonstration conforme au TP : applications `pages`, `students`, `teachers`, modèles, administration, ORM, recherche et filtres.

## Installation (Windows / PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir `http://127.0.0.1:8000/` pour le site et `http://127.0.0.1:8000/admin/` pour l'administration.

## Données à saisir dans /admin/

### Étudiants
- Awa Diop — awa.diop@ecole.sn — L1 — actif
- Moussa Fall — moussa.fall@ecole.sn — L2 — actif
- Fatou Ndiaye — fatou.ndiaye@ecole.sn — L1 — inactif
- Ibrahima Sow — ibrahima.sow@ecole.sn — L3 — actif
- Mariama Ba — mariama.ba@ecole.sn — L2 — actif
- Ousmane Cissé — ousmane.cisse@ecole.sn — L3 — actif

### Enseignants
- Mamadou Ba — mamadou.ba@ecole.sn — Mathématiques
- Aïssatou Sy — aissatou.sy@ecole.sn — Informatique
- Cheikh Diallo — cheikh.diallo@ecole.sn — Anglais

Le téléphone et la date de naissance sont facultatifs.

## Adresses à tester
- `/`
- `/about/`
- `/students/`
- `/students/1/`
- `/students/classe/L1/`
- `/teachers/`
- `/admin/`

## Git
La base locale `db.sqlite3` est ignorée par Git. Les fichiers de migrations doivent être conservés et versionnés.
