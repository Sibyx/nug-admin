# nug-admin

**Work in progress**

Simple web administration for the Project Nug.

This project is a part of my master thesis on the
[Faculty of Informatics and Information Technologies STU in Bratislava](https://www.fiit.stuba.sk/en.html) on the
subject of KVM switch implementation.

## Installation

Please keep in mind, that application need to have `root` privileges (or any alternative to control `supervisord`
service) to work correctly.

1. Create python virtual environment (`python -m venv venv`)
2. Enter environment (`source venv/bin/activate`)
3. Install dependencies `pip install -r requirements.txt`
4. Create `.env` file according `.env.example`
5. Execute migrations `python manage.py migrate`
6. Create superuser using `python manage.py createsuperuser`

---
With ❤️☕️🥃🍀 Jakub Dubec 2022
