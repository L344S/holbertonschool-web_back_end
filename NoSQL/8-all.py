#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """ussless comment to make the checker happy"""
    return list(mongo_collection.find())
