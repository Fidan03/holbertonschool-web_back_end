#!/usr/bin/env python3
"""Find schools by topic in a MongoDB collection."""


def schools_by_topic(mongo_collection, topic):
    """Return all school documents that have a specific topic."""
    return list(mongo_collection.find({'topics': topic}))
