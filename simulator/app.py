import time
import click
import logging
import re
from pathlib import Path

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)


COMPLETE_PATTERN = re.compile('^(.*INFO.*)plot-k.*\.plot([^\.].*)$')


def write_plot(plot_path):
    with open(plot_path, 'w') as f:
        f.write('This is a fake plot!\n')


@click.command()
@click.option('--template', default = '',
              type = click.STRING, help = 'The template log')
@click.option('--destination', default = '',
              type = click.STRING, help = 'Where to put the generated fake plot')
@click.option('--duration', default = '',
              type = click.FLOAT, help = 'The total simulation duration in seconds')
def main(template, destination, duration):
    interval = duration / 2630.0
    plot_path = Path(destination)
    with open(Path(template), 'r') as f:
        for line in f:
            m = COMPLETE_PATTERN.match(line)
            if m is not None:
                write_plot(plot_path)
                print(f'{m.groups()[0]}{plot_path.name}{m.groups()[1]}\n')
            else:
                print(line, end = '')
            time.sleep(interval)


if __name__ == '__main__':
    main()
