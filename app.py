from subprocess import call

app_name = input("Your app name: ")

call(["python", "manage.py", "startapp", app_name])
