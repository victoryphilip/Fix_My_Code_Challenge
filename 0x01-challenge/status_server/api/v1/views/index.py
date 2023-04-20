<<<<<<< HEAD
#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
=======
#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
>>>>>>> 4b4aa7ac407a6ec5b03a37c7adcd523d613188a3
