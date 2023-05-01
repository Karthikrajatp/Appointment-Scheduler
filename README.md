# nbyula-assignment1
### Using this application, terraformers can track the availability of other terraformers and use that information to schedule appointments.


This project was created using
 <p align="center">
  <a href="#">
    <img src="https://skillicons.dev/icons?i=html,css,js,flask,sqlite,github" />
  </a>
</p>

## Running the Server

In the project directory, you can run:
```
gunicorn -w 4 --bind 0.0.0.0:6100 main:gunicorn_app
```

Runs the app in the development mode.\
Open <http://localhost:6100/> to view it in your browser.

## Missing Modules

Recommended to create virtual environment and install modules from requirements.txt using:
```
pip install -r requirements.txt
```
