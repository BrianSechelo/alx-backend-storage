#!/usr/bin/env python3
""" Module Doc """
def top_students(mongo_collection):
    """ Func Doc """
    pipeline = [
            {
                "$addFields": {
                    "averageScore": { "$avg": "$topics.score" }
                    }
                },
            {
              "$sort": { "averageScore": -1 }
              }
            ]
    students = mongo_collection.aggregate(pipeline)
    return list(students)
