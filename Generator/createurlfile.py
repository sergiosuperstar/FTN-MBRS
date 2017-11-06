import os
from jinja2 import Environment, FileSystemLoader
import globals

constants = globals.Constants()

def render_template(template_filename, context):
    path = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(path, constants.goBack, constants.targetDestination + "app\\"))

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, constants.goBack, constants.targetDestination + "app\\")),
        trim_blocks=False)
    return template_environment.get_template(template_filename).render(context)

def create_urls_py_file(parsed_model):
    filename = constants.goBack + constants.targetDestination + "app\\" + "urls.py"
    model_entities = []

    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        model_entities.append(model_name)

    context = {
        'm_models': model_entities
    }

    with open(filename, 'w') as f:
        urls_py = render_template('urls.py.jinja2', context)
        f.write(urls_py)