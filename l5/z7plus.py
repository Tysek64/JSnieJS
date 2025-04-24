import click
import datetime
import pathlib

@click.command()
@click.argument('station', type=str)
@click.argument('infix', type=str)
@click.argument('frequency', type=click.Choice(['1g', '24g']))
@click.argument('year', type=str)
@click.option('--quantity', '-Q', type=str, default='')
@click.option('--measurements', '-M', type=pathlib.Path, default='measurements')
@click.pass_context
def main (ctx, station, infix, frequency, year, quantity, measurements):
    '''
    STATION     - Measured stations code\n
    INFIX       - File Infix\n
    FREQUENCY   - Frequency of measurements {1g | 24g}\n
    YEAR        - Year of measurement\n
    QUANTITY    - Measured quantity (when not set it is assumed to be same as infix)
    '''
    ctx.ensure_object(dict)
    ctx.obj['STATION'] = station
    ctx.obj['INFIX'] = infix
    ctx.obj['QUANTITY'] = infix if quantity == '' else quantity
    ctx.obj['FREQUENCY'] = frequency
    ctx.obj['YEAR'] = year
    ctx.obj['MEASUREMENTS'] = measurements
    from z7 import test_files_by_parameters
    return test_files_by_parameters(measurements, station, infix, frequency, year, quantity)

if __name__ == '__main__':
    main()