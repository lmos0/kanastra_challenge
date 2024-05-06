#!/bin/bash
echo "Fazer migration"
python3 manage.py makemigrations teste_kanastra
echo "============================="

echo "Migrar"
python3 manage.py migrate
echo "============================="

echo "Iniciar servidor"
python3 manage.py runserver 0.0.0.0:8000
