import os, metamodelgenerator
import updatemodels, updatebasehtml, createtemplates, copyEngine, createurlfile
import globals
import updateviews

# prepare globals
constants = globals.Constants()

# read and parse metamodel
generator = metamodelgenerator.MetamodelGenerator()
model = generator.create_metamodel(os.path.split(__file__)[0], 'grammar.txt', 'test.model')
parsed_model = generator.parse_metamodel(model)

print('*************************************************')
print('parsed model:')
print(parsed_model)
print('*************************************************')

# copy folders and files to target folder
copyEngine.copySourceToTargetDestination(constants.goBack + constants.djangoCoreSource, constants.goBack + constants.targetDestination)

# update models
updatemodels.create_model_py_file(parsed_model, generator.mapper)

# update views
updateviews.create_views_py_file(parsed_model, generator.mapper)

# update urls
createurlfile.create_urls_py_file(parsed_model)

# update entities templates
updatebasehtml.create_base_html_file(parsed_model)
createtemplates.create_base_html_file_for_entities(parsed_model)
createtemplates.create_add_html_file_for_entities(parsed_model)
createtemplates.create_update_html_file_for_entities(parsed_model)
createtemplates.create_confirm_delete_html_file_for_entities(parsed_model)

