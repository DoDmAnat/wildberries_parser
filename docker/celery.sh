#!/bin/sh
cd src

celery --app=tasks:celery worker -l INFO
 fi