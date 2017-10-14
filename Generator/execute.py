from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
from jinja2 import Environment, PackageLoader, select_autoescape
import pydot, os

class Items(object):
    def __init__(self):
        self.model = {}

    def interpreter_for_model(self, model):
        model_items = []
        enum_items = []

        for item in model.items:
            if item.modelItem is not None:
                model_items.append(item.modelItem)
            elif item.enumItem is not None:
                enum_items.append(item.enumItem)

        models_model = []
        for model_item in model_items:
            one_model = {}
            one_model["modelName"] = model_item.name
            properties = {}
            baseProperties = []
            customProperties = []
            for property in model_item.properties:
                baseProperty = {}
                customProperty = {}
                ''' one function? '''
                if property.type.baseType is not None:
                    baseProperty["propertyName"] = property.name
                    baseProperty["propertyType"] = property.type.baseType
                    '''options = []
                    option = {}
                    for opt in property.options:'''
                    baseProperties.append(baseProperty)
                elif property.type.customType is not None:
                    customProperty["propertyName"] = property.name
                    customProperty["propertyType"] = property.type.customType
                    customProperties.append(customProperty)
            properties["baseProperties"] = baseProperties
            properties["customProperties"] = customProperties
            one_model["modelProperties"] = properties
            models_model.append(one_model)
        self.model["modelItems"] = models_model

        models_enum = []
        for enum_item in enum_items:
            one_enum = {}
            one_enum["enumName"] = enum_item.name
            '''enumItems = enum_item.enumItems
            one_enum["enumItems"] = enumItems'''
            models_enum.append(one_enum)
        self.model["enumItems"] = models_enum

        return self.model

def execute(path, grammar_file_name, example_file_name):

    meta_path = os.path.join(path, grammar_file_name)
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    model_path = os.path.join(path, example_file_name)
    model_name = os.path.splitext(model_path)[0]
    model = metamodel.model_from_file(model_path)

    items = Items()
    return items.interpreter_for_model(model)

query_set = execute(os.path.split(__file__)[0], 'grammar.txt', 'test.model')
print(query_set)