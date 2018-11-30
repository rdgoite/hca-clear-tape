class Environment:

    def __init__(self, dss_api_url, core_api_url):
        self.dss_api_url = dss_api_url
        self.core_api_url = core_api_url


def _create_env(env_name):
    return Environment(f'https://dss.{env_name}.data.humancellatlas.org/v1',
                       f'http://api.ingest.{env_name}.data.humancellatlas.org')


MAP = {env_name.upper(): _create_env(env_name) for env_name in ['dev', 'staging']}
MAP['PROD'] = Environment('https://dss.data.humancellatlas.org/v1',
                          'http://api.ingest.data.humancellatlas.org')