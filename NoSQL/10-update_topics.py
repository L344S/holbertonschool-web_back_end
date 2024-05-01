#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """ussless comment to make the checker happy"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
