"""API of ``collectives`` website.

This is a very simple API meant to be used with Ajax frontend, mainly
`Tabulator <http://tabulator.info/>`_ . It offers ``GET`` endpoint to serve various tables dynamically.
But it could be extended to ``POST`` and ``DELETE`` request later.
This module is initialized by the application factory, and contains the
``/api`` blueprint.

"""


import collectives.api.admin
from collectives.api.autocomplete_user import find_users_by_fuzzy_name
import collectives.api.event
import collectives.api.userevent
import collectives.api.payment
import collectives.api.models


from .common import blueprint, marshmallow
