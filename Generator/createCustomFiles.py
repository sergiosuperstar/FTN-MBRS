import os
from jinja2 import Environment, FileSystemLoader
import globals

constants = globals.Constants()


def create_custom_functions(parsed_model):
    path = os.path.dirname(os.path.abspath(__file__))
    template_filename = "model_extensions.py.jinja2"
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        if(not os.path.exists(constants.goBack + constants.targetDestination + "app\\model_extensions\\" + model_name + "_extensions.py")):
            context = {
                'that_modelName': model_name
            }
            template_environment = Environment(
                autoescape=False,
                loader=FileSystemLoader(os.path.join(path, constants.goBack, constants.djangoCoreSource + "app\\model_extensions\\")),
                trim_blocks=False)
            filename = constants.goBack + constants.targetDestination + "app\\model_extensions\\" + model_name + "_extensions.py"
            with open(filename, 'w') as f:
                urls_py = template_environment.get_template(template_filename).render(context)
                f.write(urls_py)