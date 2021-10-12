Feature: Validation of well-known websites

Scenario Outline: Test website
    Given A URL of <url>
    When I make a HTTP request
    Then I should be able to download the HTML
    And said HTML should validate

    Examples:
    |       url                 |
    | https://sudoblark.com/#/  |
    |   https://nojs.club/      |