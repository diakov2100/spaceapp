"""
This script runs the spaceapp application using a development server.
"""

from os import environ
from spaceapp import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
