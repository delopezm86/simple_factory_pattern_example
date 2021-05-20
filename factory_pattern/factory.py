import os, sys

class Factory:

    @classmethod
    def get_instance(cls, class_name: str='', class_module: str = '.' , postfix_models_name: str = '',
                     params: dict = {})->object:
        path = '{}{}'.format(os.getcwd(), f'/{class_module.replace(".", "/")}/')
        for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
            mod = __import__('.'.join([class_module, py]), fromlist=[py])
            classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type) \
                       and (postfix_models_name in x)]
            for cls in classes:
                if not hasattr(sys.modules[__name__], cls.__name__):
                    setattr(sys.modules[__name__], cls.__name__, cls)
        class_instance = eval('{}{}()'.format(class_name.capitalize(), postfix_models_name))
        class_instance.set_params(params)
        return class_name and class_instance or None