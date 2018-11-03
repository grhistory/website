# GR Historical Site 

This project is for grhistory.org using cartidge and mezzanine django cms.

To set up project: 

create a virtual environment 

```
python3 -m venv myvenv
source myvenv/bin/activate
cd grhistoricalsite
pip install -r requirements.txt
```

create `grhistoricalsite/grhistoricalsite/local_settings.py` file

`python manage.py createdb --noinput --nodata`

run the server:

`python manage.py runserver`
