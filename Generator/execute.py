import os, metamodelgenerator
import updatemodels

# read and parse metamodel
generator = metamodelgenerator.MetamodelGenerator()
model = generator.create_metamodel(os.path.split(__file__)[0], 'grammar.txt', 'test.model')
parsed_model = generator.parse_metamodel(model)

print('*************************************************')
print('parsed model:')
print(parsed_model)
print('*************************************************')

# copy folders and files to target folder

# update models
updatemodels.create_model_py_file(parsed_model, generator.mapper)

# update views

# update urls

# update entities templates
