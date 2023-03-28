from pymongo import MongoClient
from django.conf import settings

def mongo_handler():
	client = MongoClient(f'mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}/{settings.MONGO_DB}')
	return client[settings.MONGO_DB][settings.MONGO_COLLECTION]

	