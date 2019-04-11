"""

Calculating the perplexity on a test set is one way of evaluating the effectiveness of the
language model. Write a script called ngram_perplexity.py, that takes in an ngram
language model as input (output of Part 1), lambda values, a test file and and output
file and calculates the perplexity of the test file.
The script should run with the following command:
./ngram_perplexity.py <input_file> <lambda1> <lambda2> <lambda3>
<test_file> <output_file>

Perplexity can be calculated like this:

    for each sentence in the test data file:
    add the number of words in the sentence (excluding <s> and </s>) to the total
    number of words
    for each word(i) in the sentence (excluding <s>, but including </s>:
    if the word(i) is unknown, increment an unknown word counter and
    continue
    Calculate the interpolated log-probability of the trigram as below:
    log( P(word(i) | word(i-2) word (i-1)) )
    Add this log-prob to a running total
    divide the negative sum of the log-probs by the total number of words added to the
    number of sentences minus the number of unknown words.
    Raise this value to the power of 10

Build a model using dickens_training.txt. Calculate the perplexity for the following
lambda values on dickens_test.txt:

------------------------------------------------------------
|     lambda 1      |     lambda 1     |     lambda 1      |
| (unigram weight)  | (bigram weight)  | (trigram weight)  |
|----------------------------------------------------------|
|        0.1        |      0.1          |       0.8        |
|----------------------------------------------------------|
|        0.2        |      0.5          |       0.3        |
|----------------------------------------------------------|
|        0.2        |      0.7          |       0.1        |
|----------------------------------------------------------|
|        0.2        |      0.8          |        0         |
|----------------------------------------------------------|
|        1.0        |       0           |        0         |
|----------------------------------------------------------|

"""
