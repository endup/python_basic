import argparse

#https://docs.python.org/3/library/argparse.html#name-or-flags

parser = argparse.ArgumentParser(description='before help',allow_abbrev=False,	#不支持缩写
									prog="hello",epilog="after help")

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
print(args.accumulate(args.integers))