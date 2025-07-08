Feature: Test login functionality

  @login @one
  Scenario: Login with valid credentials
    Given Launched LfynGo login page
    When I enter username as "user1" and password as "Test@123"
    When I click on Submit button
    Then I navigated to LfnGo home page

  @login
  Scenario Outline: Login with invalid credentials
    Given Launched LfynGo login page
    When I enter username as "<email>" and invalid password as "<password>"
    When I click on Submit button
    Then I verify error message
    Examples:
    |email|password|
    |user1|Test@12221|
    |user2|Test@1232|

