"Ohio is the only state that shares no letters with 'mackerel'."

Ever wonder what other words have no letters in common with only one state?  Me neither, before today!  Spoiler alert: apparently there's 38969.  At least.  That's just words in NLTK's Brown corpus.

Ohio is the most popular (least popular?) state, coming in at 1085.  Next closest is Mississippi, at 678.  Third is Alabama with 599.  Ohio doesn't have any A's or E's, so that helps.

Instructions:

$ git clone git@github.com:ryanfox/states-words.git
$ pip install -r requirements.txt
$ python states.py

If you get an NLTK error about the Brown corpus, you need to download it to your local machine.  It's 3.2MB, comprised of ~1.3 million words.  To do that, run python and type

>>> import nltk
>>> nltk.download()

From there navigate to the Brown corpus and you're good to go.  What else can you find about the names of states?
