import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_filename, context):
    path = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(path, '..', "Target\Django.Core\\app\\"))

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, '..', "Target\Django.Core\\app\\")),
        trim_blocks=False)
    return template_environment.get_template(template_filename).render(context)

def create_urls_py_file(parsed_model):
    filename = "urls.generated.py"
    model_entities = []

    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        model_entities.append(model_name)

    context = {
        'm_models': model_entities
    }

    with open(filename, 'w') as f:
        base_html = render_template('urls.py.jinja2', context)
        f.write(base_html)