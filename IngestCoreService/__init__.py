import requests
import json
import Environment

class IngestCoreService:

    def __init__(self, env=None):
        self.env = env
        if not env:
            self.env = Environment.DEV

    def get_bundle_manifests(self, envelope_uuid):
        url = '%s/submissionEnvelopes/%s/bundleManifests' % (self.env.core_api_url, envelope_uuid)
        response = requests.get(url)
        return json.loads(response.text)['_embedded']['bundleManifests']