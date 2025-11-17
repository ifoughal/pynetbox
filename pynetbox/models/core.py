"""
(c) 2017 DigitalOcean

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from urllib.parse import urlsplit

from pynetbox.core.endpoint import DetailEndpoint, RODetailEndpoint
from pynetbox.core.query import Request
from pynetbox.core.response import JsonField, Record
from pynetbox.models.circuits import Circuits, CircuitTerminations
from pynetbox.models.ipam import IpAddresses


class DataSources(Record):
    @property
    def sync(self):
        """ Performs a sync operation on the ``data-source`` detail endpoint.

        Triggers a synchronization job for the data-source object.


        ## Examples

        ```python
        data_source = nb.core.data_sources.get(123)
        data_source.sync.create()
        ```
        """
        return DetailEndpoint(self, "sync")
