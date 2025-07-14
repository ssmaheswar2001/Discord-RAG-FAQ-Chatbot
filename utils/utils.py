from pymongo.errors import OperationFailure
from pymongo.collection import Collection
import requests
from typing import Dict
import time
import os

SLEEP_TIMER = 5

def create_index(collection: Collection, index_name: str, index_definition: Dict) -> None:
    """
    Create a search index

    Args:
        collection (Collection): Collection to create search index against
        index_name (str): Index name
        index_definition (Dict): Index definition
    """
    try:
        print(f"Creating the {index_name} index")
        collection.create_search_index(model=index_definition)
    except OperationFailure:
        print(f"{index_name} index already exists, recreating...")
        try:
            print(f"Dropping {index_name} index")
            collection.drop_search_index(name=index_name)

            # Poll for index deletion to complete
            while True:
                indexes = list(collection.list_search_indexes())
                index_exists = any(idx.get("name") == index_name for idx in indexes)
                if not index_exists:
                    print(f"{index_name} index deletion complete")
                    break
                print(f"Waiting for {index_name} index deletion to complete...")
                time.sleep(SLEEP_TIMER)

            print(f"Creating new {index_name} index")
            collection.create_search_index(model=index_definition)
            print(f"Successfully recreated the {index_name} index")
        except Exception as e:
            raise Exception(f"Error during index recreation: {str(e)}")


def check_index_ready(collection: Collection, index_name: str) -> None:
    """
    Poll for index status until it's ready

    Args:
        collection (Collection): Collection to check index status against
        index_name (str): Name of the index to check
    """
    while True:
        indexes = list(collection.list_search_indexes())
        matching_indexes = [idx for idx in indexes if idx.get("name") == index_name]

        if not matching_indexes:
            print(f"{index_name} index not found")
            time.sleep(SLEEP_TIMER)
            continue

        index = matching_indexes[0]
        status = index["status"]
        if status == "READY":
            print(f"{index_name} index status: READY")
            print(f"{index_name} index definition: {index['latestDefinition']}")
            break

        print(f"{index_name} index status: {status}")
        time.sleep(SLEEP_TIMER)