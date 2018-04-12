import requests

# TODO replace this to use environment variable instead
API_URL = 'https://dss.dev.data.humancellatlas.org/v1'

class BundleService:

    def get_bundle(self, uuid):
        bundle_url = '%s/bundles/%s' % (API_URL, uuid)
        return requests.get(bundle_url, {'replica': 'aws'})