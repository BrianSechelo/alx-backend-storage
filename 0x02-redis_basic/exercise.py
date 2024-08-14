#!/usr/bin/env python3
"""
Doc Module
"""
import redis
import uuid
from typing import Union
class Cache:
    """ class documentation """
    def  __init__(self):
       self._redis = redis.Redis()
       self._redis.flushdb()

    def store(self, data: Union[str, bytes, int,float]) -> str:
        """ func documentation """
        keyx = str(uuid.uuid4())
        self._redis.set(keyx, data)
        return keyx
