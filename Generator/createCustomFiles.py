import os
from jinja2 import Environment, FileSystemLoader
import globals

constants = globals.Constants()


def create_custom_functions(parsed_model):
    path = os.path.dirname(os.path.abspath(__file__))
    model_entities = []
    template_filename = "customs.py.jinja2"
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        model_entities.append(model_name)
    context = {
        'm_models': model_entities
    }
    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, constants.goBack, constants.djangoCoreSource + "app\\")),
        trim_blocks=False)
    filename = constants.goBack + constants.targetDestination + "app\\" + "customs.py"
    with open(filename, 'w') as f:
        urls_py = template_environment.get_template(template_filename).render(context)
        f.write(urls_py)