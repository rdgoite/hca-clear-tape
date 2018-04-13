class Environment:

    def __init__(self, dss_api_url, core_api_url):
        self.dss_api_url = dss_api_url
        self.core_api_url = core_api_url

DEV = Environment('https://dss.dev.data.humancellatlas.org/v1', 'http://api.ingest.dev.data.humancellatlas.org')
PROD = Environment('https://dss.data.humancellatlas.org/v1', 'http://api.ingest.dev.data.humancellatlas.org')