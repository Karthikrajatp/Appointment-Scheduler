# Appointment Scheduler
### Using this application, Employees have the ability to monitor the availability of their fellow colleagues, which empowers them to efficiently schedule appointments and coordinate their work effectively.
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
