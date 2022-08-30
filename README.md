# InsuranceMGT
=======
Insurance Management System


# Installation & Run Guide

## Install Steps

### Create conda env
conda create -n insurancemgt django

### install other packages
pip install -r requirements.txt

### Migrate models
python manage.py migrate

## Running the Web Application
python manage.py runserver