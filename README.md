# Word Frequency Counter

This script will read lines from stdin and spit out a list of k-words appearence
in the consumed text. By default, it counts single word occurence only, but it
can also count pairs, triplets, etc. You can also tell WF object to treat words
case dependently.

## Usage

To test that the script works, try running:
    python wordfreq.py

To run on the actual input, you can do something like that:
    python wordfreq.py < large_text.txt

## Sample
Below's what the script will produce if fed Dostoevsky's "Crime and Punishment".

### Single words.
$ python wf.py < ../pg2554.txt | more
9491 out of 212241 entrie(s) of length 1 repeated:

                 key            occurence          % occurence
================================================================================
                 the                 7289                 0.03%
                 and                 6533                 0.03%
                  to                 5144                 0.02%
                  he                 4575                 0.02%
                   a                 4312                 0.02%
                   i                 4175                 0.02%
                 you                 3813                 0.02%
                  of                 3634                 0.02%
                  it                 3188                 0.02%
                that                 3052                 0.01%
                  in                 3032                 0.01%
                 was                 2610                 0.01%
                  at                 1943                 0.01%
                 his                 1920                 0.01%
                 but                 1682                 0.01%
                 not                 1641                 0.01%
                 her                 1632                 0.01%
                   s                 1624                 0.01%
                with                 1613                 0.01%
...

### Word pairs.
$ python wf.py < ../pg2554.txt | more
72156 out of 106120 entrie(s) of length 2 repeated:

                 key            occurence          % occurence
================================================================================
              in the                  669                 0.01%
              of the                  540                 0.01%
              he was                  448                 0.00%
              to the                  438                 0.00%
               don t                  438                 0.00%
                it s                  429                 0.00%
              he had                  425                 0.00%
              on the                  419                 0.00%
                i am                  413                 0.00%
              at the                  404                 0.00%
              it was                  372                 0.00%
              that s                  333                 0.00%
             that he                  301                 0.00%
             you are                  284                 0.00%
                in a                  279                 0.00%
               to be                  278                 0.00%
              do you                  258                 0.00%
              with a                  237                 0.00%
             did not                  229                 0.00%
...
