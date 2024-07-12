import os
from pathlib import Path


FILE_PATH = Path(__file__).resolve().parent
PROJECTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_apps():
    count = input("Nechta app yaratilsin: ")
    if not count.isdigit():
        print("Sonda kiriting")
        create_apps()
    for i in range(int(count)):
        name = input('appni nomini kiriting: ')
        os.system(f"{FILE_PATH}/venv/bin/python {FILE_PATH}/manage.py startapp {name}")
        os.system(f"mv {FILE_PATH.parent}/{name} {FILE_PATH}/apps")
        os.system(f"cp {PROJECTS}/new_django_project/urls.py -r  {FILE_PATH}/apps/{name}")
        os.system(f"cp {PROJECTS}/new_django_project/forms.py -r  {FILE_PATH}/apps/{name}")
        print(f"{name} app yaratildi")

create_apps()