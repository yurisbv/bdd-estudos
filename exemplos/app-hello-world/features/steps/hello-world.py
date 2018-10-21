from behave import when, then, given
import json, requests


@given(u'a api no endereço: {api_url}')
def api_url(context, api_url):
    context.api_url = api_url


@when(u'eu realizo um {http_verb} no endpoint: {endpoint}')
def endpoint(context, http_verb, endpoint):
    if http_verb.replace("'", "") == 'GET':
        context.response = requests.get(url=context.api_url.replace("'", "") + endpoint.replace("'", ""))
    context.data = context.response.json()
    assert context.response


@then(u'devo receber status code igual a {status_code}')
def status_code(context, status_code):
    assert context.response.status_code == int(status_code.replace("'", ""))


@then(u'devo receber content-type igual a {content_type}')
def content_type(context, content_type):

    assert context.response.headers['content-type'] == content_type.replace("'", "")


@then(u'devo receber um body com {response}')
def response(context, response):
    test_json = json.loads(response.replace("'", ""))
    response_json = context.response.json()
    assert response_json['message'] == test_json['message']