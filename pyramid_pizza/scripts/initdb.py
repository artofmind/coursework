import os, sys, transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    # MyModel,
    Base,
    User,
    Tovar,
    Order
    )


def usage(arg):
    commd = os.path.basename(arg[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s dev.ini")' % (commd, commd))
    sys.exit(1)


def main(arg=sys.argv):
    if len(arg) < 2:
        usage(arg)
    config_uri = arg[1]
    options = parse_vars(arg2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
