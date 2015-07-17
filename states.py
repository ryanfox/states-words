from collections import defaultdict
from nltk.corpus import brown

states = ['alabama',
          'alaska',
          'arizona',
          'arkansas',
          'california',
          'colorado',
          'connecticut',
          'delaware',
          'florida',
          'georgia',
          'hawaii',
          'idaho',
          'illinois',
          'indiana',
          'iowa',
          'kansas',
          'kentucky',
          'lousiana',
          'maine',
          'maryland',
          'massachusetts',
          'michigan',
          'minnesota',
          'mississippi',
          'missouri',
          'montana',
          'nebraska',
          'nevada',
          'new hampshire',
          'new jersey',
          'new mexico',
          'new york',
          'north carolina',
          'north dakota',
          'ohio',
          'oklahoma',
          'oregon',
          'pennsylvania',
          'rhode island',
          'south carolina',
          'south dakota',
          'tennesse',
          'texas',
          'utah',
          'vermont',
          'virgina',
          'washington',
          'west virginia',
          'wisconsin',
          'wyoming']


wordsthatdontshareanyletters = defaultdict(list)

for word in brown.words():
    wordletters = set(word.lower())

    for state in states:
        stateletters = set(state)

        residual = stateletters - wordletters

        # if removing all letters in the word didn't change the letters in the state, they share no letters
        if residual == stateletters:
            wordsthatdontshareanyletters[word].append(state)


# keep track of most popular states
statetotals = defaultdict(int)

for word, states in wordsthatdontshareanyletters.items():
    if len(states) == 1:
        statetotals[states[0]] += 1
        print word, states

print 'total words: ', len(wordsthatdontshareanyletters)
print
print 'total words by state: '
for state, count in statetotals.items():
    print state, count