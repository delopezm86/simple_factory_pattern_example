import random
from factory import Factory

if __name__=='__main__':
    args_dict = {
        'a': {'name': 'Maria', 'age': 20},
        'b': {'name': 'Jose', 'height': 65},
        'c': {'name': 'Raul', 'age': 30, 'expertise': 'blabla'},
        'd': {'name': 'Uncle McDonald'}
    }
    for _ in range(10):
        class_choice = random.choice(list(args_dict.keys()))
        instance = Factory.get_instance(class_choice, 'models.classes', 'Runnable', args_dict[class_choice])
        instance.run()