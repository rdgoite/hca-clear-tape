import requests
import json
from Config import env

class IngestCoreService:

    def __init__(self, _env=env.DEV):
        self.env = _env

    def get_bundle_manifests(self, envelope_uuid):
        url = '%s/submissionEnvelopes/%s/bundleManifests' % (self.env.core_api_url, envelope_uuid)
        response = requests.get(url)
        return json.loads(response.text)['_embedded']['bundleManifests']