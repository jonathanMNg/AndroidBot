import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--gather-resources-type', help='resources type to gather', choices=['oil', 'farm', 'steel', 'mineral'], default='oil')
parser.add_argument('--command', '-c', help='Single command [withdraw|explore|sendalltroops]')
parser.add_argument('--low-power', '-l', help='Low power consumption mode', action='store_true')
args = parser.parse_args()


if hasattr(args, 'low_power'):
    if args.low_power:
        print("Hello")
    else:
        print("Bye")
