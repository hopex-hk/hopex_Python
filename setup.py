from setuptools import setup

setup(
    name="hopex-client",
    version="1.0.0",
    packages=['hopex',
              'hopex.exception', 'hopex.constant',
              'hopex.utils',
              'hopex.client',
              'hopex.services', 'hopex.services.account', 'hopex.services.home', 'hopex.services.market',
              'hopex.services.trade', 'hopex.services.wallet',
              'hopex.connection', 'hopex.connection.impl', "performance"
              ],
    install_requires=['requests', 'urllib3']
)
