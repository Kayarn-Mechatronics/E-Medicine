# InsuranceMGT
=======
Insurance Management System


# Installation & Run Guide

## Install Steps

### clone repository
git clone https://github.com/agent87/InsuranceMGT.git

### Create conda env
conda create -n insurancemgt django

### activate conda env
activate insurancemgt

### install other packages
pip install -r requirements.txt

### Migrate models
python manage.py migrate

## Running the Web Application
python manage.py runserver