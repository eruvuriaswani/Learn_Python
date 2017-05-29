"""."""
import yaml
from apps import models


def get_testcases(yml_file):

    with open(yml_file) as stream:
        try:
            tcs = yaml.load(stream)
            for d in tcs:
                yield d, tcs[d]
        except yaml.YAMLError as exc:
            print(exc)
            return -1, -1


def pytest_generate_tests(metafunc):
    if "tc_name" in metafunc.funcargnames:
        yaml_file = "test.yaml"
        for tc, apis in get_testcases(yaml_file):
            #print(tc, apis)Api
            metafunc.addcall(funcargs=dict(tc_name=tc, api_list=apis))


def get_api_detail(api_id, headers=None):
    result = False
    api = models.ApiRequests.query.filter_by(id=api_id).first()
    url = api.url
    print(url)
    return result, headers


def test_api(tc_name, api_list):
    print("testcase: ", tc_name, api_list)
    headers = None
    for api in api_list:
        # lets get api details
        result, headers = get_api_detail(api, headers)
        print(api)
    assert True
