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











