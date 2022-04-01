# Prodigy annotation scripts

This repository contains scripts/recipes for text manual annotation using [Prodigy](https://prodi.gy/) annotation tool by [Explosion](https://explosion.ai/) (the creators of [spaCy](https://spacy.io/)). In order to use Prodigy for your annotation tasks you need a license, but [researchers can apply for an interim license to use Prodigy free in their research](https://prodi.gy/docs/faq).

The following recipes were inspired in code found in [Explosion AI's GitHub repository](https://github.com/explosion/prodigy-recipes) with the help of [Prodigy's Support Forum](https://support.prodi.gy/).


## [Named Entity Recognition and Text Classification](https://github.com/sofiapinto/Prodigy-annotation-scripts/tree/main/NER%20%2B%20classification)
Recipe for manually annotating text:
1. identify named entities (for named entity recognition);
2. classify text into categories (for binary classification or multiclass classification into 3 classes).

In the example below the annotatores can highlight 3 named entities in sentences: weather related keywords, location and date/time. The squared buttons at the bottom are used for the data classification task: to classify text into weather related, non-weather related or unsure.

![NER_classification_gif](https://github.com/sofiapinto/Prodigy-annotation-scripts/blob/main/gifs/prodigy_NER_class.gif)

