#!/usr/bin/python
import re
import sys
import csv
import argparse
import StringIO

class WF:
    def __init__(self, key_length, ignore_case=True):
        """Initialize new word frequency object."""

        # Structure to hold word count.
        self.wf = {}

        # Ignore the case?
        self.ignore_case = ignore_case

        # Total number of words.
        self.word_count = 0

        # Length of the "key", are we counting one word, pairs of words?
        self.key_length = key_length 
        
    def consume(self, text):
        """Consumes a portion of the text."""
        key = []

        # Use regex to split text in words.
        for w in re.findall(r'\w+', text):
            # Lower case if case to be ignored.
            if (self.ignore_case):
                w = w.lower()

            # Increase word count.
            self.word_count += 1

            # Build key of the appropriate length, start adding up frequencies.
            if len(key) < self.key_length:
                key.append(w)
            else:
                key_str = " ".join(key)
                self.wf[key_str] = self.wf.get(key_str, 0) + 1
    
                # Remove first part.
                del key[0]

                # Add next word.
                key.append(w)

    def get_stats(self):
        """Getter for word count structure."""
        return self.wf

    def to_csv_str(self):
        """Return CSV representation of the frequency list."""
        csv_str = ""

        # Writing output to the string file.
        f = StringIO.StringIO(csv_str)

        writer = csv.writer(f, delimiter=',', quotechar='"')

        writer.writerow(["word(s)", "occurrence count"])

        if len(self.wf) > 0:
            for k in self.wf.keys():
                writer.writerow([k, self.wf[k]])

        output = f.getvalue()

        f.close()

        return output

    def __str__(self):
        """Return string representation of the frequency list."""
        output = "%s words split in %s groups, group size %s:\n\n" % \
                                            (self.word_count,
                                            len(self.wf),
                                            self.key_length)

        output += "%20s %20s\n" % ("word(s)", "occurrence count")
        output += "="*41 + "\n"

        if len(self.wf) > 0:
            # Sort by number of occurrences before displaying.
            for (k, v) in sorted(self.wf.items(),
                                 key=lambda (k,v): v, reverse=True):

               output += "%20s %20s\n" % (k, v)
           
            # Remove trailing newline character.
            output = output.rstrip()
        else:
            output = "No values in the frequency list."

        return output

def main():
    parser = argparse.ArgumentParser(
            description='Count the frequency usage of each word(s) in a text.',
            epilog="https://github.com/jango/WF", prog='Word Frequency Counter')

    parser.add_argument('-w', type=int, default=1,
        help='number of words in a group')

    parser.add_argument('-i', default=True, action='store_true',
        help='case-sensitive count flag (defaults to false)')

    parser.add_argument('-f', type=str, choices=['csv', 'txt'],
        default='txt', help='output format')

    parser.add_argument('-v', '--version', action='version',
        version='%(prog)s 0.1a')

    args = parser.parse_args()

    # Initialize word frequency counter.
    wf = WF(args.w, ignore_case=args.i)


    # If we are being fed stuff through stdin.
    while True:
        s = sys.stdin.readline()
        if not s:
            break
        wf.consume(s)

    # Choose output format
    if args.f == 'csv':
        print wf.to_csv_str()
    else:
        print wf

if __name__ == "__main__":
    main()
