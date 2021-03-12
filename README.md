# html-cv-generator
A generator for résumés in HTML and PDF using Flask. Generator for https://cmatte.me/CV/

## Features
- CV renders correctly in both HTML and PDF formats.
- Links handler: when printed to PDF, links are written as orderly-numbered footnotes.
- Error detection when a URL variable is undefined.

## Dependencies
- python3
- Flask

## How to use
- Define your route in generator.py (see example on line 53).
- Create a html file extending layout.html on the model of normal.html. This file declares used blocks and define some variables.
- Edit layout.html to define your URLs and set your basic layout up (you can keep the original one).
- Create the different block files.
- Add links with `{{ renvoi(URL, 'DISPLAYED TEXT') }}` for footnotes generation (play with bdp_length in normal.html if the footnotes block size is incorrect).
- Run with `python generator.py` and open http://127.0.0.1:5000/
