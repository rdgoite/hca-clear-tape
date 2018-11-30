import requests

from Config import env


class IngestCoreService:

    def __init__(self, _env=env.ENV['DEV']):
        self.env = _env

    def iterate_bundle_manifests(self, envelope_uuid):
        page_size = 20
        current_page_number = 0
        current_page = self._get_bundle_manifests(envelope_uuid, current_page_number, page_size)
        total_pages = current_page['page']['totalPages']
        while current_page_number < total_pages:
            for manifest in current_page['_embedded']['bundleManifests']:
                yield manifest
            current_page_number += 1
            if current_page_number < total_pages:
                current_page = self._get_bundle_manifests(envelope_uuid, current_page_number, page_size)

    def _get_bundle_manifests(self, envelope_uuid, page_number, page_size):
        url = '%s/submissionEnvelopes/%s/bundleManifests' % (self.env.core_api_url, envelope_uuid)
        response = requests.get(url, {'page': page_number, 'size': page_size})
        return response.json()
