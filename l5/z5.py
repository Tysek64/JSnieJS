import argparse
import datetime
import pathlib
import z5utils
import z5log

if __name__ == '__main__':
    z5log.configureLogging()

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(required=True)

    randParser = subparsers.add_parser('randStation')
    randParser.set_defaults(func=z5utils.randName)

    statParser = subparsers.add_parser('stats')
    statParser.add_argument('stationName', help='Name of station')
    statParser.set_defaults(func=z5utils.stats)

    parser.add_argument('quantity', help='Measures quantity')
    parser.add_argument('frequency', help='Frequency of measurements', choices=['1g', '24g'])
    parser.add_argument('startDate', help='Measurements\' start date', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
    parser.add_argument('endDate', help='Measurements\' end date', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))

    parser.add_argument('--metadata', '-m', help='Path to file containing metadata', type=pathlib.Path, default='stacje.csv', required=False)
    parser.add_argument('--measurements', '-M', help='Path to folder containing files with measurements', type=pathlib.Path, default='measurements', required=False)

    args = parser.parse_args()
    args.func(args)
