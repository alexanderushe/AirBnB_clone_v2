from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine =  create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import base_model
        session = self.__session
        object_dict = {}
        if cls is not None:
            if type(cls) is str:
                cls = base_model.classes[cls]
            objects = session.query(cls).all()
        else:
            all_classes = base_model.classes
            objects = []
            for name, cls in all_classes.items():
                objects += session.query(cls).all()

        for obj in objects:
            key = '{}.{}'.format(obj.__class__.name__, obj.id)
            object_dict[key] = obj
        return object_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        self.__session.remove()
