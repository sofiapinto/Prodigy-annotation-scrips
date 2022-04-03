# Named Entity Recognition (NER) + Multiclass Classification + Text Input + Checkbox

**Annotation recipe** with a **NER** block, a **multiclass classification** block, a **text input** block and a **checkbox** block. The **checkbox** created with html code comes as a solution to the fact that Prodigy recipes can only have 1 block of each type. Besides checkboxes one can also add radio buttons, for example.

In the example below we have an annotation setup that receives reviews and the annotator can:
- highlight opinion/sentiment expressions (e.g. "good", "horrible", "amazing", "the best I've ever had", etc.);
- classify reviews as positive, negative, neutral or both positive and negative;
- write more about their decision with the text input block;
- point out if they think the user who wrote the review was being sarcastic by clicking on the checkbox;
- accept, reject or ignore the annotation in hand.

The reviews used for the purpose of this example were retrieved from [Yelp Reviews Dataset available in Kaggle](https://www.kaggle.com/code/omkarsabnis/sentiment-analysis-on-the-yelp-reviews-dataset/data).

Notice that one can either click or use keyboard shortcuts to annotate.

![NER_multiclass_textinput_checkbox_gif](https://github.com/sofiapinto/Prodigy-annotation-scripts/blob/main/gifs/prodigy_NER_multiclass_textinput_checkbox.gif)

## Files

* *annotation_setup.py*: the main file with the annotation setup, using a blocks recipe;

* *annotation_javascript.js*: code to make the first NER label the default label and to do the key binding for the checkbox;

* *annotation_instructions.html*: instructions on how to use the tool that can be checked by the annotator (by clicking the help button on the upper left hand side);

* *html_checkbox.html*: html code to create the checkbox block;

* *extract_annotations.py*: code to export the annotated data to a json file;

* *reviews.jsonl*: file with text reviews to annotate (the input file needs to be of type jsonl);

## Instructions for the annotators

***To annotate*** 

1. Open a command line

2. cd to the folder where your code and data are stored, *e.g.*:

```
cd "Documents/GitHub/Prodigy-annotation-scripts/NER + multiclass classification + text input + checkbox"
```

3. Run the following command

```
python -m prodigy blocks-recipe annotated_reviews reviews.jsonl  -F annotation_setup.py
```
where *annotated_reviews* is the name of the database where the annotations will be stored.

5. Open http://localhost:8080/

6. Once you've finished annotating for the day, click save, close http://localhost:8080/, CRTL+C and close the command line.

***Once you have finished annotating ALL reviews***

1. Open a command line

2. cd to the folder where your code and data are stored, *e.g.*:

```
cd "Documents/GitHub/Prodigy-annotation-scripts/NER + multiclass classification + text input + checkbox"
```

3. Run the following command

```
python extract_annotations.py annotated_reviews annotated_reviews.json
```

4. A new file called *annotated_reviews.json* will be in your folder. 