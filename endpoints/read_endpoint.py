import ANAPSID.Decomposer.parseEndpoints


def read_endpoint(f):
    with open(f) as efile:
        endpoints = ANAPSID.Decomposer.parseEndpoints.parse(efile)
    for tup in endpoints:
        print(tup)


if __name__ == '__main__':
    read_endpoint("endpointsFedBench")
