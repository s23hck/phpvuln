import os
import sys
import inspect
import importlib


from lib.common.vuln.abc import Vulnerability

vulnerability_classes_path = os.path.join('lib', 'vulns')


def sys_to_mod_path(*args):
    return os.path.join(*[x[:-3] if x.endswith('.py') else x for x in args]).replace(os.path.sep, '.')


def get_vulnerability_classes():
    items = os.listdir(vulnerability_classes_path)
    items.remove('__init__.py')

    classes = []

    for item in items:
        if not item.endswith('.py'):
            continue

        module_name = sys_to_mod_path(vulnerability_classes_path, item)

        if not importlib.import_module(module_name):
            continue

        for _class in inspect.getmembers(sys.modules[module_name], inspect.isclass):
            #class_name = _class[0]
            class_object = _class[1]

            if class_object == Vulnerability:
                continue

            classes.append(class_object)

    return classes
