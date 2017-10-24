from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
from jinja2 import Environment, PackageLoader, select_autoescape
import pydot, os


class MetamodelGenerator(object):
    def __init__(self):
        self.model = {}
        self.mapper = {'string': 'TextField',
                       'char': 'CharField',
                       'int': 'IntegerField'
                       }

    def parse_metamodel(self, model):
        model_items = []
        model_item_names = []
        enum_items = []
        enum_item_names = []

        for item in model.items:
            if item.modelItem is not None:
                model_items.append(item.modelItem)
                model_item_names.append(item.modelItem.name)
            elif item.enumItem is not None:
                enum_items.append(item.enumItem)
                enum_item_names.append(item.enumItem.name)

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
                    options = []
                    for opt in property.options:
                        option = {}
                        if opt.unique is not None:
                            if baseProperty["propertyName"] == 'boolean':
                                return "Boolean type doesn't support unique option"
                            option["optionName"] = 'unique'
                            option["optionValue"] = 'True'
                        elif opt.null is not None:
                            option["optionName"] = 'null'
                            option["optionValue"] = 'True'
                        elif opt.maxValue is not None:
                            if baseProperty["propertyName"] == 'boolean':
                                return "Boolean type doesn't support max value option"
                            option["optionName"] = 'maxValue'
                            option["optionValue"] = opt.maxValue.number
                        elif opt.minValue is not None:
                            if baseProperty["propertyName"] == 'boolean':
                                return "Boolean type doesn't support min value option"
                            option["optionName"] = 'minValue'
                            option["optionValue"] = opt.minValue.number
                        elif opt.blank is not None:
                            option["optionName"] = 'blank'
                            option["optionValue"] = 'True'
                        elif opt.default is not None:
                            option["optionName"] = 'default'
                            option["optionValue"] = opt.default.Name
                        elif opt.validator is not None:
                            option["optionName"] = 'validators'
                            validators = []
                            for val in opt.validator.validatorValues:
                                validator = {}
                                if val.validatorMax is not None:
                                    validator["validatorName"] = 'validatorMax'
                                    validator["validatorValue"] = val.validatorMax.maxValidatorValue
                                elif val.validatorMin is not None:
                                    validator["validatorName"] = 'validatorMin'
                                    validator["validatorValue"] = val.validatorMin.minValidatorValue
                                validators.append(validator)
                            option["optionValue"] = validators
                        elif opt.ref is not None:
                            return "Base Types cannot have ref option"
                        elif opt.cardinality is not None:
                            return "Base Types cannot have cardinality option"
                        options.append(option)
                    baseProperty["options"] = options
                    baseProperties.append(baseProperty)
                elif property.type.customType is not None:
                    if property.type.customType not in model_item_names and property.type.customType not in enum_item_names:
                        return "Custom Type '" + property.type.customType + "' doesn't exist"
                    customProperty["propertyName"] = property.name
                    customProperty["propertyType"] = property.type.customType
                    options = []
                    for opt in property.options:
                        option = {}
                        if opt.ref is not None:
                            option["optionName"] = 'ref'
                            option["optionValue"] = opt.ref.refName
                        elif opt.cardinality is not None:
                            option["optionName"] = 'cardinality'
                            option["optionValue"] = opt.cardinality
                        elif opt.null is not None:
                            option["optionName"] = 'null'
                            option["optionValue"] = 'True'
                        elif opt.default is not None:
                            option["optionName"] = 'default'
                            option["optionValue"] = opt.default.Name
                        else:
                            return "Custom Types can only have ref, cardinality or null options"
                        options.append(option)
                    customProperty["options"] = options
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
            enum_options = []
            for items in enum_item.enumItems:
                item = {}
                item["key"] = items.key
                item["value"] = items.value
                enum_options.append(item)
            one_enum["enumItems"] = enum_options
            models_enum.append(one_enum)
        self.model["enumItems"] = models_enum

        return self.model

    def create_metamodel(self, path, grammar_file_name, example_file_name):

        meta_path = os.path.join(path, grammar_file_name)
        meta_name = os.path.splitext(meta_path)[0]
        metamodel = metamodel_from_file(meta_path)

        model_path = os.path.join(path, example_file_name)
        model_name = os.path.splitext(model_path)[0]
        model = metamodel.model_from_file(model_path)

        return model;


