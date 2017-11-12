import subprocess
import globals


def run():
    constants = globals.Constants()

    print('make migrations:')
    process_make_migrations = subprocess.Popen(r'python manage.py makemigrations', cwd=constants.goBack + constants.targetDestination)
    make_migrations_output = process_make_migrations.communicate()[0]
    print(make_migrations_output)

    print('migrate:')
    process_migrate = subprocess.Popen(r'python manage.py migrate', cwd=constants.goBack + constants.targetDestination)
    process_migrate_output = process_migrate.communicate()[0]
    print(process_migrate_output)
