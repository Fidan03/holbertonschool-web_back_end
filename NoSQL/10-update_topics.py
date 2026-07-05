#!/usr/bin/env python3
"""Update school topics in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Update topics for all school documents matching name."""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}},
    )
