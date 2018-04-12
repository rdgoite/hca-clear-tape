import requests
import json

# TODO replace this to use environment variable instead
API_URL = 'https://dss.dev.data.humancellatlas.org/v1'

class BundleService:

    def get_files(self, bundle_uuid):
        bundle = self.get_bundle(bundle_uuid)
        return [file['uuid'] for file in bundle['files']]

    def get_bundle(self, uuid):
        bundle_url = '%s/bundles/%s' % (API_URL, uuid)
        response = requests.get(bundle_url, {'replica': 'aws'})
        return json.loads(response.text)['bundle']
