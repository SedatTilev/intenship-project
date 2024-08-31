Feature: Reelly sale status tests

  Scenario: User can filter by sale status Out of Stocks
    Given Open the login page
    When Log in to the page
    Then Verify the right page opens
    When Filter by sale status of “Out of Stocks”
    Then Verify each product contains the Out of Stocks tag