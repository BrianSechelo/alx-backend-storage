#!/usr/bin/env python3
""" Module docs """
def schools_by_topic(mongo_collection, topic):
    """ Fucn Docs """
    return mongo_collection.find( {"topic": topic} )
