from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

data_conn = create_engine('oracle://gao:gao123159@172.17.254.200:1521/mydev', echo=True, pool_size=10)
Session = sessionmaker(bind=data_conn, autocommit=False, autoflush=False)


def module_to_dict(module):
    module_json = dict()
    keys = dir(module)
    keys = list(filter(lambda key: key == '__tablename__' or key[0:1] != '_', keys))
    for key in keys:
        if callable(getattr(module, key)):
            continue
        module_json[key] = getattr(module, key)
    return module_json


def dict_to_module(module_class, module_dict):
    for key in module_dict.keys():
        setattr(module_class, key, module_dict[key])
    return module_class