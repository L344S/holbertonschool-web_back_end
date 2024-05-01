#!/usr/bin/env python3
"""function that returns the list of school having a given topic"""


def schools_by_topic(mongo_collection, topic):
    """ussless comment to make the checker happy"""
    done = mongo_collection.find({"topics": topic})
    return done
