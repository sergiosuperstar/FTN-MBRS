import os, metamodelgenerator
from jinja2 import Environment, FileSystemLoader

# read and parse metamodel
generator = metamodelgenerator.MetamodelGenerator()
model = generator.create_metamodel(os.path.split(__file__)[0], 'grammar.txt', 'test.model')
parsed_model = generator.parse_metamodel(model)

print (parsed_model)

# copy folders and files to target folder

# update models
PATH = os.path.dirname(os.path.abspath(__file__))
print (PATH)
print (os.path.join(PATH, '..', "Django.Core\\app\\"))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, '..', "Django.Core\\app\\")),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_model_py_file():
    fname = "model.generated.py"

    context = {
        'm_models': parsed_model,
        'm_mapper': generator.mapper
    }
    #
    with open(fname, 'w') as f:
        pythonModels = render_template('models.py.jinja2', context)
        f.write(pythonModels)

create_model_py_file()

# update views

# update urls

# update entities templates
