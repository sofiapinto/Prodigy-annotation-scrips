import prodigy
from prodigy.components.loaders import JSONL
from prodigy.components.preprocess import add_tokens
import spacy


@prodigy.recipe(
	"blocks-recipe",
	dataset=("The dataset to use", "positional", None, str),
	source=("The source data as a JSONL file", "positional", None, str),
	)


def blocksSolution(dataset, source, lang="en"):
	blocks = [
	{"view_id": "ner_manual"}
	]

	with open('annotation_javascript.js') as f:
		javascript = f.read()

	nlp = spacy.blank(lang)

	stream = JSONL(source) # load in the JSONL file

	stream = add_tokens(nlp, stream)

	stream = list(stream) # to show the percentage already annotated

	return {
	    "dataset": dataset,   # save annotations in this dataset
	    "view_id": "blocks",  # use the blocks interface
	    "stream": stream,
	    "config": {
	    	"instructions": "annotation_instructions.html",
	    	"buttons": ["accept", "reject", "ignore"],
	        "labels": ["Weather",
	        			"Location",
	        			"Date/time"],  # the labels for the manual NER interface
	        "blocks": blocks,
	        "custom_theme": { #changing colors
	            "labels": {"Weather": "#4393c3",
	            			"Location": "#af8dc3", 
	            			"Date/time": "#fdae61"		
	            },
	            "ignore":"#FFD700"
	        },
	        "keymap_by_label": {"Weather": "w", #each NER label will be associated with a key
	        					"Location": "l", 
		            			"Date/time": "d"},
	        "history_length": 20,
	        "javascript": javascript
	        }
	}