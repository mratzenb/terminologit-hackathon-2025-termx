from argparse import ArgumentParser
import os
import urllib.request
from urllib.error import HTTPError

SUPPORTED_RESOURCE_TYPES = ["CodeSystem", "ValueSet"]

def upload_resource(url: str, resource: str) -> bool:
    print(f"Uploading resource to {url}", flush=True)
    
    req = urllib.request.Request(url, resource.encode("utf-8"), method="POST")
    req.add_header('Content-Type', 'application/json+fhir')
    req.add_header('Accept', 'application/json+fhir')
    try:    
        with urllib.request.urlopen(req) as f:
            print(f.read().decode("utf-8"), flush=True)
    except HTTPError as e:
        print(e, flush=True)
        print(e.read().decode(), flush=True)
        return False
    return True


def main():
    parser = ArgumentParser()

    parser.add_argument(
        "--target",
        required=True,
        dest="target"
    )

    parser.add_argument(
        "--source",
        required=True,
        dest="source"
    )

    args = parser.parse_args()
    if not (
        type(args.target) == str and
        args.target.startswith("http") and
        args.target.endswith("fhir")
    ):
        print(f"Invalid target {args.target}\nCorrect example: 'http://server.tld/fhir'", flush=True)
        exit(42)


    if not (
        type(args.source) == str and
        args.source.endswith("/") and
        os.path.exists(args.source) and
        os.path.isdir(args.source)
    ):
        print(f"Invalid source {args.source}\nCorrect example: '/some/path/to/directory/'", flush=True)
        exit(43)


    for resource_type in SUPPORTED_RESOURCE_TYPES:
        resource_names = os.listdir(f"{args.source}{resource_type}")
        for resource_name in sorted(resource_names):
            print(f"Uploading Resource {resource_name}", flush=True)
            with open(f"{args.source}/{resource_type}/{resource_name}", "r", encoding="utf-8") as f:
                try:
                    assert upload_resource(f"{args.target}/{resource_type}", f.read()), f"Could not upload resource {resource_type} {resource_name}"
                except Exception as e:
                    print(e, flush=True)


if __name__ == '__main__':
    main()
