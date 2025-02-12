import sys
import os
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
trusted_certificate_authorities = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            exception = NetworkSecurityException(e, sys)
            print(exception)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            exception = NetworkSecurityException(e, sys)
            print(exception)

    def insert_data_to_mongo_db(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            exception = NetworkSecurityException(e, sys)
            print(exception)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phishingDataset.csv"
    DATABASE = "DINESH"
    collection = "NETWORK_DATA"
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_to_mongo_db(records, DATABASE, collection)
    print(f"{no_of_records} inserted.")