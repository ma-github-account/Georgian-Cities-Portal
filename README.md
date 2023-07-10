![1](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/d919e3a2-94fe-493d-9927-6eb48ff3b69b)This application is a portal about Georgian cities. It displays a map of Georgia with markers for major cities. Clicking on a marker results in city details and photo display. Cities are added via Admin panel.

Prerequisites:

- Python 3.9.7,
- Django 4.1.2,
- Django Rest Framework 3.14.0
- Pillow 7.0.0 (pip install Pillow==7.0.0)
- GeoDjango (PostGIS, PostgreSQL, Psycopg2, OSGeo4W, Gdal)

After installing PostreSQL and creating geospatial database, it needs to be referenced in settings.py file (line 109).

Application is based on Australian Cultural Heritage Places application presented by Ikrom Nishanbaev in his Udemy Course "Leaflet From Scratch With A GeoDjango Project".

How to run: 1.python manage.py makemigrations 2.python manage.py migrate 3.Adding desired cities to the geospatial database 4.python manage.py runserver



![1](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/650df092-9868-429b-afa9-d207643c75a3)



![2](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/9fb8eeff-b8d5-4807-8488-127ec5b2779f)




![3](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/d961c6a7-c9c1-4a84-8eb6-f44d7506368a)




![4](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/27223c68-38e0-4679-baca-0585fc75c996)




![5](https://github.com/ma-github-account/Georgian-Cities-Portal/assets/89083426/7dfcdc47-b1d7-4919-8620-34043333cf8a)
































