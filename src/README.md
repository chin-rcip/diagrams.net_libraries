# Create shape library (XML) and Update diagrams by libraries' version

## Requirements

- Python 3.7+
- `pip3 install -r requirements.text`

## Create shape library (XML)

```bash
usage: create_library.py [-h] -s STYLE -f FILENAME -b BASEONTO
                         [-e EXTONTO] [-m] [-q] [-l LANG]

Create shape library XML

options:
  -h, --help            show this help message and exit
  -s STYLE, --style STYLE
                        Libraries style JSON filename
  -f FILENAME, --filename FILENAME
                        Shape library XML filename
  -b BASEONTO, --baseOnto BASEONTO
                        Path to base ontology RDF file
  -e EXTONTO, --extOnto EXTONTO
                        Path to extension ontology RDF file
  -m, --metadata        Include shape's metatada (URI, labels, link)
  -q, --quantification  Include property's quantification
  -l LANG, --lang LANG  Specify the main language of the library, default
                        is "en"
```
For example:

```bash
# Create library for a base ontology, using style version 2, with quantification and metadata, and French as language of the labels
python3 create_library.py -s libraries_style_v2.json -f library_shape.xml -b base_ontolofy.rdfs -m -q -l fr
```
```bash
# Create library for an extension ontology, using style version 2, metadata, and English as language of the labels (by default)
python3 create_library.py -s libraries_style_v2.json -f library_shape.xml -b base_ontolofy.rdfs -e extension_ontology.rdfs -m
```

## Update diagrams (XML) by libraries' version

**NOTE: DO NOT change the filename of the `libraries_style_v{1,2}` JSON.**

```bash
usage: update_diagram.py [-h] [-c] [-s] [-d] [-f] XML {v1,v2}

Update diagrams by version of libraries

positional arguments:
  XML              Path to draw.io XML file (uncompressed)
  {v1,v2}          Version of libraries

options:
  -h, --help       show this help message and exit
  -c, --color      Update color
  -s, --space      Update label spacing
  -d, --dimension  Update dimensions, width and height for class, widthStroke for
                   property
  -f, --font       Update font (size, style)
```

For example, update diagram created using libraries verion 1 to version 2 style:

```bash
# color only
python3 update_diagram.py test.xml v1 -c
```
```bash
# color, space, dimension and font
python3 update_diagram.py test.xml v1 -c -s -d -f
```