# Word Frequency Counter
Word Frequency Counter allows you to count the frequency usage of each word or
multiple words in an arbitrary text.

This script will read lines from stdin and spit out a list of k-words appearance
in the consumed text. By default, it counts single word occurrence only, but it
can also count pairs, triplets, etc. You can also tell WF object to treat words
case-sensitive.

## Usage

    python wf.py -h
    Count the frequency usage of each word(s) in a text.

    optional arguments:
    -h, --help     show this help message and exit
    -w W           number of words in a group
    -i             case-sensitive count flag (defaults to false)
    -f {csv,txt}   output format
    -v, --version  show program's version number and exit


## Sample

Below's what the script will produce if fed Dostoevsky's "Crime and Punishment".

### Single words.

    ./wf.py < pg2554.txt | more

    212241 words split in 9491 groups, group size 1:

                 word(s)      occurrence count
    =========================================
                     the                 7289
                     and                 6533
                      to                 5144
                      he                 4575
                       a                 4312
                       i                 4175
                     you                 3813
                      of                 3634
                      it                 3188
                    that                 3052
                      in                 3032
                     was                 2610
                      at                 1943
                     his                 1920
                     but                 1682
                     not                 1641
    --More--

### Word pairs.


    ./wf.py -w 2 < pg2554.txt | more

    212241 words split in 72156 groups, group size 2:

                 word(s)      occurrence count
    =========================================
                  in the                  669
                  of the                  540
                  he was                  448
                  to the                  438
                   don t                  438
                    it s                  429
                  he had                  425
                  on the                  419
                    i am                  413
                  at the                  404
                  it was                  372
                  that s                  333
                 that he                  301
                 you are                  284
                    in a                  279
                   to be                  278
    --More--
