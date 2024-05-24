import click

from pyquantms.diann.create_diann_cfg import create_diann_cfg
from pyquantms.features.add_sage_feature import add_sage_feature
from pyquantms.mzml.mzml_statistics import mzml_statistics

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


cli.add_command(create_diann_cfg)
cli.add_command(add_sage_feature)
cli.add_command(mzml_statistics)

if __name__ == "__main__":
    cli()
