import os
from jinja2 import Environment, FileSystemLoader
import globals

def render_template(template_filename, context):
    constants = globals.Constants()
    path = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(path, '..', constants.targetDestination + "app\\templates\\"))

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, '..', constants.targetDestination + "app\\templates\\")),
        trim_blocks=False)
    return template_environment.get_template(template_filename).render(context)

class EntityDetails(object):
    def __init__(self, name):
        self.Name = name
        #implement logic for creating urls from entity name
        self.Url = name

def create_base_html_file(parsed_model):
    filename = "base.generated.html"
    entitiesDetails = []
    for model in parsed_model["modelItems"]:
        entitiesDetails.append(EntityDetails(model["modelName"]))

    context = {
        'm_modelDetails': entitiesDetails
    }

    with open(filename, 'w') as f:
        base_html = render_template('base.html.jinja2', context)
        f.write(base_html)
