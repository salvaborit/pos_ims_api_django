# POS IMS (Point-of-Sale Inventory Management System) Backend

POS IMS is a Django-based web application that allows users to manage their point-of-sale (POS) terminal inventory, along with their respective details. This is the backend codebase for the application, built with Django REST Framework.

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it (pipenv was used).
3. Install the dependencies using the command `pipenv install`.
4. Create a database (MySQL was used) and configure it in the settings.py file.
5. Make and run the database migrations using the commands `python manage.py makemigrations` and `python manage.py migrate`.
6. Start the development server using the command `python manage.py runserver`.

## API Endpoints

The following API endpoints are available:

`/status/` - GET the API status <br>
`/terminals/` - GET a list of all terminals or CREATE a new terminal <br>
`/terminals/<int:pk>/` - GET, PUT, or DELETE a single terminal <br>
`/acquirers/` - GET a list of all acquirers or CREATE a new acquirer <br>
`/acquirers/<int:pk>/` - GET, PUT, or DELETE a single acquirer <br>
`/models/` - GET a list of all models or CREATE a new model <br>
`/models/<int:pk>/` - GET, PUT, or DELETE a single model <br>
`/locations/` - GET a list of all locations or CREATE a new location <br>
`/locations/<int:pk>/` - GET, PUT, or DELETE a single location <br>
`/statuses/` - GET a list of all statuses or CREATE a new status <br>
`/statuses/<int:pk>/` - GET, PUT, or DELETE a single status <br>
`/connectivities/` - GET a list of all connectivities or CREATE a new connectivity <br>
`/connectivities/<int:pk>/` - GET, PUT, or DELETE a single connectivity <br>
