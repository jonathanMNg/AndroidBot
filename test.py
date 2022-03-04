import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('--gather-resources-type', help='resources type to gather [oil|steel|farm], default is oil')
parser.add_argument('--vm-index', help='Index value of Memu Emulator e.g 0|1|2|3')

args = parser.parse_args()

print(args)
print(sys)
