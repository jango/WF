#!/usr/bin/python

import re
import sys

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

            # Build key of the appropriate length, start adding up frequences.
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

    def __str__(self):
        """Return string representation of the frequence list."""
        output = "%s out of %s entrie(s) of length %s " % (len(self.wf),
                                                           self.word_count / self.key_length,
                                                           self.key_length)
        output += "repeated:\n\n"
        output += "%20s %20s %20s\n" % ("key", "occurence", "% occurence")
        output += "="*80 + "\n"

        if len(self.wf) > 0:
            # Sort by number of occurences before displaying.
            for (k, v) in sorted(self.wf.items(),
                                 key=lambda (k,v): v, reverse=True):

               output += "%20s %20s %20.2f%%\n" % (k, v,
                          self.wf[k] * 1.0 / (self.word_count / self.key_length))
           
            # Remove trailing newline character.
            output = output.rstrip()
        else:
            output = "No values in the frequency list."

        return output


if __name__ == "__main__":
    # Sample long string to use if no stdin data available.
    long_string = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                     sed diam nonummy nibh euismod tincidunt ut laoreet dolore
                     magna aliquam erat volutpat. Ut wisi enim ad minim veniam,
                     quis nostrud exerci tation ullamcorper suscipit lobortis
                     nisl ut aliquip ex ea commodo consequat. Duis autem vel eum
                     iriure dolor in hendrerit in vulputate velit esse molestie
                     consequat, vel illum dolore eu feugiat nulla facilisis at
                     vero eros et accumsan et iusto odio dignissim qui blandit
                     praesent luptatum zzril delenit augue duis dolore te
                     feugait nulla facilisi. Nam liber tempor cum soluta nobis
                     eleifend option congue nihil imperdiet doming id quod mazim
                     placerat facer possim assum. Typi non habent claritatem
                     insitam; est usus legentis in iis qui facit eorum
                     claritatem. Investigationes demonstraverunt lectores legere
                     me lius quod ii legunt saepius. Claritas est etiam
                     processus dynamicus, qui sequitur mutationem consuetudium
                     lectorum. Mirum est notare quam littera gothica, quam nunc
                     putamus parum claram, anteposuerit litterarum formas
                     humanitatis per seacula quarta decima et quinta decima.
                     Eodem modo typi, qui nunc nobis videntur parum clari, fiant
                     sollemnes in futurum."""

    # Initialize word frequency counter.
    wf = WF(1)
    
    # If we are being fed stuff through stdin.
    if not sys.stdin.isatty():
        while True:
            s = sys.stdin.readline()
            if not s:
                break
            wf.consume(s)
    else:
        wf.consume(long_string)

    print wf
