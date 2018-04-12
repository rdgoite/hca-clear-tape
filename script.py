import sys
import json
from BundleService import BundleService

if __name__ == '__main__':
    service = BundleService()
    bundle_uuid = sys.argv[1]
    contents = []
    for file in service.iterate_indexed_files(bundle_uuid):
        contents.append(file)
    print(json.dumps(contents, indent=4))