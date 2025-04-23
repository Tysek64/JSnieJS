import datetime
import pathlib
import click
import z5utils
import z5log

@click.group()
@click.argument('quantity')
@click.argument('frequency', type=click.Choice(['1g', '24g']))
@click.argument('startdate', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
@click.argument('enddate', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
@click.option('--metadata', '-m', type=pathlib.Path, default='stacje.csv')
@click.option('--measurements', '-M', type=pathlib.Path, default='measurements')
@click.pass_context
def main (ctx, quantity, frequency, startdate, enddate, measurements, metadata):
    '''
    QUANTITY    - Measured quantity\n
    FREQUENCY   - Frequency of measurements {1g | 24g}\n
    STARTDATE   - Measurements\' start date\n
    ENDDATE     - Measurements\' end date
    '''
    ctx.ensure_object(dict)
    ctx.obj['QUANTITY'] = quantity
    ctx.obj['FREQUENCY'] = frequency
    ctx.obj['STARTDATE'] = startdate
    ctx.obj['ENDDATE'] = enddate
    ctx.obj['MEASUREMENTS'] = measurements
    ctx.obj['METADATA'] = metadata

@main.command('randStation')
@click.pass_context
def randNameWrapper (ctx):
    return z5utils.randName(ctx.obj['QUANTITY'], ctx.obj['FREQUENCY'], ctx.obj['STARTDATE'], ctx.obj['ENDDATE'], ctx.obj['MEASUREMENTS'], ctx.obj['METADATA'])
    
@main.command('stats')
@click.pass_context
@click.argument('stationname')
def statsWrapper (ctx, stationname):
    '''
    STATIONNAME - Name of station
    '''
    return z5utils.stats(stationname, ctx.obj['QUANTITY'], ctx.obj['FREQUENCY'], ctx.obj['STARTDATE'], ctx.obj['ENDDATE'], ctx.obj['MEASUREMENTS'], ctx.obj['METADATA'])
    
if __name__ == '__main__':
    z5log.configureLogging()
    main()
