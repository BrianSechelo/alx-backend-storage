#!/usr/bin/env python3
""" Module doc """
def update_topics(mongo_collection, name, topics):
    """ Func doc """
    mongo_collection.update_many({"name": name},{ "$set": {"topics": topics}})
