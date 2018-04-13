import requests

from Config import env


class BundleService:

    def __init__(self, _env=env.DEV):
        self.env = _env

    def iterate_indexed_files(self, bundle_uuid):
        bundle = self.get_bundle(bundle_uuid)
        for file in bundle['files']:
            if (file['indexed']):
                file_url = '%s/files/%s' % (self.env.dss_api_url, file['uuid'])
                response = requests.get(file_url, {'replica': 'aws'})
                yield response.json()


    def get_bundle(self, uuid):
        bundle_url = '%s/bundles/%s' % (self.env.dss_api_url, uuid)
        response = requests.get(bundle_url, {'replica': 'aws'})
        return response.json()['bundle']
