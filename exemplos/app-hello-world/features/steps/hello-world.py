from behave import when, then, given
import json, requests


@given(u'a api no endereço: {api_url}')
def api_url(context, api_url):
    context.api_url = api_url


@when(u'eu realizo um {http_verb} no endpoint: {endpoint}')
def endpoint(context, http_verb, endpoint):
    if http_verb == 'GET':
        context.response = requests.get(url=context.api_url + endpoint)
    context.data = context.response.json()
    assert context.response


@then(u'devo receber status code igual a {status_code}')
def status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@then(u'devo receber content-type igual a {content_type}')
def content_type(context, content_type):

    assert context.response.headers['content-type'] == content_type


@then(u'devo receber um body com {response}')
def response(context, response):
    test_json = json.loads(response)
    response_json = context.response.json()
    assert response_json['message'] == test_json['message']