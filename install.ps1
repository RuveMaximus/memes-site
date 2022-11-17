py -m venv venv

.\venv\Scripts\activate
pip install -r requirements.txt

py .\shmemes\manage.py migrate
deactivate