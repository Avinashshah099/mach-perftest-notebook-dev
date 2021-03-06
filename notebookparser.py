import argparse

'''
Argument parsing is going to get very complex very quickly so
we leave the parser in it's own file.
'''

def parse_args():
    parser = argparse.ArgumentParser(description="Process data into a customized data format "
                                                 "and analyze it using standardized technique.")
    parser.add_argument("--config", "-c", type=str, required=True,
                        help="Configuration to use for processing and analyzing data.")
    parser.add_argument("--debug", action="store_true", default=False,
                        help="Enable additional debug logging.")
    return parser.parse_args()
