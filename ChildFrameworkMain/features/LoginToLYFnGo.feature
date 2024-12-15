Feature: Test login functionality

  @login
  Scenario: Login with valid credentials
    Given Launched LfynGo login page
    When I enter username as "poobesh0012@putsbox.com" and password as "Test@123"
    When I click on Submit button
    Then I navigated to LfnGo home page

  @login
  Scenario Outline: Login with invalid credentials
    Given Launched LfynGo login page
    When I enter username as "<email>" and invalid password as "<password>"
    When I click on Submit button
    Then I verify error message
    Examples:
    |email                  |password|
    |poobesh0012@putsbox.com|Test@12221|
    |poobesh0012@putsbox.com|Test@1232|

