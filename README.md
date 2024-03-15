# Django Project Template

## Setup
* Clone this repo
* copy local.env as .env
* run docker compose build and docker compose up
* visit `localhost:8080/admin`, and login with admin : admin

## Advanced Setup
* create a new app
  *  docker compose run backend python manage.py startapp <app_name>
  *  (optional) move app to apps folder
  *  edit <app_name>/appss.py so that `name=apps.<app_name>` instead of `name=<app_name>`
  *  add app to `settings.base.py` in LOCAL_APPS as `apps.<app_name>`

* run in local mode
  * make sure your .env file has `DJANGO_SETTINGS_MODULE=settings.dev`
  * run `docker compose up`
  * app will run without cache and with sqlite

* run in dev mode
  * make sure your .env file has `DJANGO_SETTINGS_MODULE=settings.dev`
  * run `docker compose up`
  * app will run with cache and with postgres

* run in prod
  * make sure your .env file has `DJANGO_SETTINGS_MODULE=settings.prod`
  * make sure your .env file's `DJANGO_SECRET_KEY` is unique
  * make sure default values are unique, or setup as secrets in your deployment target
  * make sure .env hosts and ports are valid for your deployment network setup (redis, postgres)
  * do not use compose, instead use the image and gunicorn (see `docker/Dockerfile`)
