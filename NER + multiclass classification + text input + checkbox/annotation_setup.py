import prodigy
from prodigy.components.loaders import JSONL
from prodigy.components.preprocess import add_tokens
import spacy

def add_options(stream):
    # Helper function to add options to every task in a stream
    options = [
       {"id": 1, "text": "Positive review👍"},
       {"id": -1, "text": "Negative review👎"},
       {"id": 0, "text": "Neutral review😶"},
       {"id": 2, "text": "Positive and negative review👍👎"}
    ]
    for task in stream:
        task["options"] = options
        yield task


@prodigy.recipe(
	"blocks-recipe",
	dataset=("The dataset to use", "positional", None, str),
	source=("The source data as a JSONL file", "positional", None, str),
	)


def blocksSolution(dataset, source, lang="en"):
	with open('html_checkbox.html') as f:
		HTML_checkbox = f.read()

	blocks = [
	{"view_id": "ner_manual"},
	{"view_id": "choice", "text": None},
	{"view_id": "text_input", "field_rows":1, "field_label": "Elaborate on the above choice, if needed:"},
	{"view_id": "html", "html_template": HTML_checkbox},
	]

	with open('annotation_javascript.js') as f:
		javascript = f.read()

	nlp = spacy.blank(lang)

	stream = JSONL(source) # load the JSONL file
	stream = add_options(stream)  # add options to task

	stream = add_tokens(nlp, stream)

	stream = list(stream) # to show the percentage already annotated

	return {
	    "dataset": dataset,   # save annotations in this dataset
	    "view_id": "blocks",  # use the blocks interface
	    "stream": stream,
	    "config": {
	    	"instructions": "annotation_instructions.html",
	    	"buttons": ["accept", "reject", "ignore"],
	        "labels": ["Opinion/sentiment expression"],  # the labels for the manual NER interface
	        "blocks": blocks,
	        "custom_theme": {
	            "labels": {"Opinion/sentiment expression": "#2592da"},
	        },
	        "keymap_by_label": {"Opinion/sentiment expression": "e",
	        					"0": "p", 
								"1": "n",
								"2": "0",
								"3": "b"},
	        "history_length": 20,
	        "javascript": javascript
        }
	}