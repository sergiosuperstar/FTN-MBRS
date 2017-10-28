import os, metamodelgenerator
import updatemodels, updatebasehtml, create_base_page_for_entities, copyEngine

# read and parse metamodel
generator = metamodelgenerator.MetamodelGenerator()
model = generator.create_metamodel(os.path.split(__file__)[0], 'grammar.txt', 'test.model')
parsed_model = generator.parse_metamodel(model)

print('*************************************************')
print('parsed model:')
print(parsed_model)
print('*************************************************')

# copy folders and files to target folder
djangoCoreSource = "../Django.Core/"
targetDestination = "../Target/Django.Core/"
copyEngine.copySourceToTargetDestination(djangoCoreSource, targetDestination)

# update models
updatemodels.create_model_py_file(parsed_model, generator.mapper)

# update views

# update urls

# update entities templates
updatebasehtml.create_base_html_file(parsed_model)
create_base_page_for_entities.create_base_html_file_for_entities(parsed_model)