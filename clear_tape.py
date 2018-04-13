import os
import sys
import json

from Config import env
from IngestCoreService import IngestCoreService
from BundleService import BundleService


CT_ENV = 'CT_ENV'


def determine_env():
    env_config = env.DEV
    if CT_ENV in os.environ:
        env_name = os.environ[CT_ENV]
        if env_name in env.MAP:
            env_config = env.MAP[env_name]
        else:
            raise Exception('Failed to set env to unknown name [%s]' % (env_name))
    return env_config


def run():
    env_config = determine_env()
    core_service = IngestCoreService(env_config)

    output_directory = './output'
    prepare_output_directory(output_directory)
    output_prefix = determine_output_prefix(output_directory)

    submission_id = determine_submission_id()
    manifest_iteration = core_service.iterate_bundle_manifests(submission_id)

    bundle_service = BundleService(env_config)
    process_bundles(bundle_service, manifest_iteration, output_prefix)


def prepare_output_directory(output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


def determine_output_prefix(output_directory):
    prefix = 'bundle'
    if len(sys.argv) == 3:
        prefix = sys.argv[2]
    output_prefix = '%s/%s' % (output_directory, prefix)
    return output_prefix


def determine_submission_id():
    if not len(sys.argv) < 2:
        submission_id = sys.argv[1]
        return submission_id
    else:
        raise Exception('Submission ID required.')


def process_bundles(bundle_service, bundle_manifests, output_prefix):
    count = 1
    for manifest in bundle_manifests:
        bundle_uuid = manifest['bundleUuid']
        print('Preparing bundle #%d with id [%s]...' % (count, bundle_uuid))
        bundle = compile_bundle(bundle_service, bundle_uuid)
        file_name = '%s_%d.json' % (output_prefix, count)
        with open(file_name, 'w+') as file:
            file.write(json.dumps(bundle, indent=2))
            count = count + 1
            print('done')

def compile_bundle(bundle_service, bundle_uuid):
    contents = []
    for file in bundle_service.iterate_indexed_files(bundle_uuid):
        contents.append(file)
    return contents


if __name__ == '__main__':
    try:
        run()
    except Exception as exception:
        print('Unexpected %s: %s' % (type(exception), exception))
        sys.exit(1)
