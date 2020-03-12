./appenv/Scripts/activate
flask db init
flask db migrate -m "components table"
flask db migrate -m "maintenances table"
flask db upgrade
python generate_data.py
deactivate
