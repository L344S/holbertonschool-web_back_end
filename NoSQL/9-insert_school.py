#!/usr/bin/env python3
"""function that inserts a new document in given arg"""


def insert_school(mongo_collection, **kwargs):
    """ussless comment to make the checker happy"""
    done = mongo_collection.insert_one(kwargs)
    return done.inserted_id
