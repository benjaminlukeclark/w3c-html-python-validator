from pathlib import PurePath
from src.HTMLValidator import HTMLValidator
import os
from behave import given, when, then
import requests
import random


@given("A URL of {url}")
def step_imp(context, url):
    context.url = url


@when("I make a HTTP request")
def step_imp(context):
    context.http_request = requests.get(context.url, allow_redirects=True, verify=False)


@then("I should be able to download the HTML")
def step_imp(context):
    file_name = os.getcwd() + "/" + str(random.randint(0, 100)) + ".html"
    html_file = open(file_name, "w")
    html_file.write(context.http_request.text)
    context.html_file_name = file_name


@then("Said HTML should validate")
def step_imp(context):
    html_validator = HTMLValidator()
    file_validation_return = html_validator.validate_html_file(context.html_file_name)
    os.remove(context.html_file_name)
    assert file_validation_return["messages"] == []
