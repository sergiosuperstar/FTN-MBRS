import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_filename, context):
    path = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(path, '..', "Django.Core\\app\\"))

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, '..', "Django.Core\\app\\")),
        trim_blocks=False)
    return template_environment.get_template(template_filename).render(context)


def create_model_py_file(parsed_model, mapper):
    filename = "model.generated.py"

    context = {
        'm_models': parsed_model,
        'm_mapper': mapper
    }

    with open(filename, 'w') as f:
        python_models = render_template('models.py.jinja2', context)
        f.write(python_models)

