#!/usr/bin/env python3
""" Module docs """
def schools_by_topic(mongo_collection, topic):
    """ Fucn Docs """
    return list(mongo_collection.find( {"topic": topic} ))
