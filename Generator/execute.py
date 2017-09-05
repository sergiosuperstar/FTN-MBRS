from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot

if __name__ == '__main__':

    test_mm = metamodel_from_file('grammar.txt')
    metamodel_export(test_mm, 'test_meta.dot')
    graph = pydot.graph_from_dot_file('test_meta.dot')
    graph[0].write_png('test_meta.png')

    test_model = test_mm.model_from_file('test.model')
    model_export(test_model, 'test_model.dot')
    graph = pydot.graph_from_dot_file('test_model.dot')
    graph[0].write_png('test_model.png')