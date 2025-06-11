#!/usr/bin/python3
"""
This module holds a model that defines the all common attr/metthods
for other class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines all common attributes/methods for other classes
    """

    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ returns a human readable str form of the class instance & attr"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Updates the public instance attributes """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance
        used for data serialization and deserialization
        """
        the_dict = {}
        the_dict['__class__'] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                the_dict[key] = val.isoformat()  # convert to str obj
            else:
                the_dict[key] = val
        return the_dict
