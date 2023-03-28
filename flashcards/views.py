from django.shortcuts import render, redirect
from .utils import mongo_handler
from django.contrib import messages
import pymongo
from collections import defaultdict
import csv
import os


def home(request):
	return render(request, 'general/home.html')

def deck(request, deck_name=None):
	mongo_collection = mongo_handler()
	if request.method == 'POST' and deck_name:
		mongo_collection.delete_many({"deck": deck_name})
		messages.info(request, 'Your deck has been removed.')
		return redirect('deck')
	if request.method == 'POST' and ('csv_file' in request.FILES):
		deck_name, ext = os.path.splitext(request.FILES['csv_file'].name)
		decoded_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
		reader = csv.DictReader(decoded_file)
		all_cards = []	
		for row in reader:
			row['deck'] = deck_name
			row['reviewed'] = 0
			all_cards.append(row)
		mongo_collection.insert_many(all_cards)
		messages.info(request, 'Your deck has been uploaded.')
		return redirect('deck')
	all_docs = list(mongo_collection.find({}))
	d = defaultdict(int)
	for i in all_docs:
		d[i['deck']] += 1
	return render(request, 'flashcards/deck.html', {'decks': dict(d)})


def card(request, deck_name, word=None):
	mongo_collection= mongo_handler()
	if word:
		res = list(mongo_collection.find({"deck": deck_name}).sort([("word", pymongo.ASCENDING)]))
		indx = [i for i, d in enumerate(res) if word in d.values()]
		new_indx = [indx[0]+1 if indx[0]+1 < len(res) else 0]
		next_card = res[new_indx[0]]
		increment_reviewed(next_card, mongo_collection)
		return render(request, 'flashcards/card.html', {'card': next_card})
	res = list(mongo_collection.find({"deck": str(deck_name)}).sort([("word", pymongo.ASCENDING)]))
	first_card = res[0]
	increment_reviewed(first_card, mongo_collection)
	return render(request, 'flashcards/card.html', {'card': first_card})


def increment_reviewed(card, mongo_handler):
	query = { 'word': card.get('word'), 'deck': card.get('deck') }
	updated_card = { "$set": { 'reviewed': card.get('reviewed') + 1 } }
	mongo_handler.update_one(query, updated_card)
	return