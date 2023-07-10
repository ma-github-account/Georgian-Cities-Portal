This application is a portal about Georgian cities. It displays a map of Georgia with markers for major cities. Clicking on a marker results in city details and photo display. Cities are added via Admin panel.

Prerequisites:

- Python 3.9.7,
- Django 4.1.2,
- Django Rest Framework 3.14.0
- Pillow 7.0.0 (pip install Pillow==7.0.0)
- GeoDjango (PostGIS, PostgreSQL, Psycopg2, OSGeo4W, Gdal)

After installing PostreSQL and creating geospatial database, it needs to be referenced in settings.py file (line 109).

Application is based on Australian Cultural Heritage Places application presented by Ikrom Nishanbaev in his Udemy Course "Leaflet From Scratch With A GeoDjango Project".

How to run: 1.python manage.py makemigrations 2.python manage.py migrate 3.Adding desired cities to the geospatial database 4.python manage.py runserver



![1](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/ba4916c9-3aae-4c9c-b14d-f83f32a064e3)


![2](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/2c7975a8-625d-4436-90bb-173587d6b19a)


![3](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/be103157-a211-4d88-98d2-e9c2cbf8525c)


![4](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/b8f7aa08-37ab-4f49-8091-be9a5b9a855c)


![5](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/0148879d-e8aa-4201-81c3-8e87f8234f0a)



















