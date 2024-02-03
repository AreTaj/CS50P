# Watch on Youtube
# Problem Set 7

import re
import sys
# Do not import any other libraries.

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        # re.search(pattern, string, flags=0)
        # Look for "http" or "https", optional "www", requires "youtube.com/embed", and ends with some alphanumerics or underscores; returns match object if found.
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        # If url_pattern exists, ...
        if url_pattern:
            # Returns tuple of split_url
            split_url = url_pattern.groups()
            # Append [3] tuple of split_url to ""
            return "https://youtu.be/"+split_url[3]


if __name__ == "__main__":
    main()