<<<<<<< HEAD
#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
=======
#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
>>>>>>> 4b4aa7ac407a6ec5b03a37c7adcd523d613188a3
