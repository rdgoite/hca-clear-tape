import requests
import json

API_URL_DEFAULT = 'http://api.ingest.dev.data.humancellatlas.org'

class IngestCoreService:

    def get_bundle_manifests(self, envelope_uuid):
        url = '%s/submissionEnvelopes/%s/bundleManifests' % (API_URL_DEFAULT, envelope_uuid)
        response = requests.get(url)
        return json.loads(response.text)['_embedded']['bundleManifests']