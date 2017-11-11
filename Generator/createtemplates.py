import os
from jinja2 import Environment, FileSystemLoader
import globals

constants = globals.Constants()
pathToThePages = constants.goBack + constants.targetDestination + "app\\templates\\app\\"
def render_template(template_filename, context):
    path = os.path.dirname(os.path.abspath(__file__))
    print(os.path.join(path, constants.goBack, constants.targetDestination + "app\\templates\\app\\"))

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(path, constants.goBack, constants.targetDestination + "app\\templates\\app\\")),
        trim_blocks=False)
    return template_environment.get_template(template_filename).render(context)

class EntityDetails(object):
    def __init__(self, name, main_property, property_list, entity_properies_name_for_display):
        self.Name = name
        #implement logic for creating urls from entity name
        self.UrlForNew = name + "_form"
        self.UrlForEdit = name + "_update_form"
        self.UrlForDelete = name + "_confirm_delete_form"
        self.UrlForDetails = name + "_details"
        self.MainProperty = main_property
        self.Properties = property_list
        self.PropertyNames = entity_properies_name_for_display

def create_base_html_file_for_entities(parsed_model):
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        filename = pathToThePages + model_name + ".html"
        entity_properties = []
        entity_properies_name_for_display = []

        for modelBaseProperty in model["modelProperties"]["baseProperties"]:
            entity_properties.append(modelBaseProperty["propertyName"])
            entity_properies_name_for_display.append(modelBaseProperty["propertyName"].capitalize())
        for modelCustomProperty in model["modelProperties"]["customProperties"]:
            entity_properties.append(modelCustomProperty["propertyName"])
            entity_properies_name_for_display.append(modelCustomProperty["propertyName"].capitalize())

        main_property = entity_properties[0]

        context = {
            'm_model': EntityDetails(model_name, main_property, entity_properties, entity_properies_name_for_display)
        }

        with open(filename, 'w') as f:
            base_html = render_template('entity_list.html.jinja2', context)
            f.write(base_html)

class EntityCreateDetails(object):
    def __init__(self, name):
        self.Name = name
        #implement logic for creating urls from entity name
        self.UrlForList = name
        self.MainProperty = None

def create_add_html_file_for_entities(parsed_model):
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        filename = pathToThePages + model_name + "_add_form.html"

        context = {
            'm_model': EntityCreateDetails(model_name)
        }

        with open(filename, 'w') as f:
            create_html = render_template('entity_create.html.jinja2', context)
            f.write(create_html)


def create_update_html_file_for_entities(parsed_model):
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        filename = pathToThePages + model_name + "_update_form.html"

        context = {
            'm_model': EntityCreateDetails(model_name)
        }

        with open(filename, 'w') as f:
            update_html = render_template('entity_update.html.jinja2', context)
            f.write(update_html)


def create_confirm_delete_html_file_for_entities(parsed_model):
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        filename = pathToThePages + model_name + "_confirm_delete_form.html"

        m_model = EntityCreateDetails(model_name)
        # let's say that first property of model is main property
        if len(model["modelProperties"]["baseProperties"]) == 0:
            m_model.MainProperty = model["modelProperties"]["customProperties"][0]["propertyName"]
        else:
            m_model.MainProperty = model["modelProperties"]["baseProperties"][0]["propertyName"]
        context = {
            'm_model': m_model
        }

        with open(filename, 'w') as f:
            update_html = render_template('entity_confirm_delete.html.jinja2', context)
            f.write(update_html)


def create_details_html_file_for_entities(parsed_model):
    for model in parsed_model["modelItems"]:
        model_name = model["modelName"]
        filename = pathToThePages + model_name + "_details.html"
        entity_properties = []
        entity_properies_name_for_display = []

        for modelBaseProperty in model["modelProperties"]["baseProperties"]:
            entity_properties.append(modelBaseProperty["propertyName"])
            entity_properies_name_for_display.append(modelBaseProperty["propertyName"].capitalize())
        for modelCustomProperty in model["modelProperties"]["customProperties"]:
            entity_properties.append(modelCustomProperty["propertyName"])
            entity_properies_name_for_display.append(modelCustomProperty["propertyName"].capitalize())

        main_property = entity_properties[0]

        context = {
            'm_model': EntityDetails(model_name, main_property, entity_properties, entity_properies_name_for_display)
        }

        with open(filename, 'w') as f:
            details_html = render_template('entity_details.html.jinja2', context)
            f.write(details_html)