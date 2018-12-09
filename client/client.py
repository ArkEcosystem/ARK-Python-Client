import inspect
import pkgutil
from importlib import import_module
from pathlib import Path

from client.connection import Connection
from client.exceptions import ArkParameterException
from client.resource import Resource


VERSION_TO_STRING_MAPPING = {
    'v2': 'two',
}


class ArkClient(object):

    def __init__(self, hostname, api_version='v2'):
        """
        :param string hostname: Node hostname. Examples: `http://127.0.0.1:4002` or
            `http://my.domain.io/api/`. This is to allow people to server the api
            on whatever url they want.
        :param string api_version: Version of the API you want to use. Defaults to v2.
        """
        if api_version not in ['v2']:
            raise ArkParameterException('Only version "v2" is supported')

        self.api_version = api_version

        self.connection = Connection(hostname, api_version.replace('v', ''))
        self._import_api()

    def _import_api(self):
        """
        Dynamically imports endpoints for correct API version.
        """
        version = VERSION_TO_STRING_MAPPING[self.api_version]
        # Get all modules under the wanted version folder

        modules = pkgutil.iter_modules([str(Path(__file__).parent / 'api' / version)])
        for _, name, _ in modules:
            module = import_module('client.api.{}.{}'.format(version, name))
            for attr in dir(module):
                # If attr name is `Resource`, skip it as it's a class and also has a
                # subclass of Resource
                if attr == 'Resource':
                    continue

                attribute = getattr(module, attr)
                if inspect.isclass(attribute) and issubclass(attribute, Resource):
                    # Set module class as a property on the client
                    setattr(self, name, attribute(self.connection))
