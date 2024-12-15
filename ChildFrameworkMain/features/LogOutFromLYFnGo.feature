Feature: Logout from LYFnGo

  @logout
  Scenario: Logout acknowledge successfull
    Given Launched LfynGo login page
    When I enter username and password
    |email                    |password|
    |poobesh0012@putsbox.com  |Test@123|
    And I click on Submit button
    Then I navigated to LfnGo home page
    Then I click on profile menu
    When I click on Logout option
    And I acknowledge yes
    Then I navigated back to login screen

    @logout
  Scenario: Logout not acknowledge
    Given Launched LfynGo login page
    When I enter username and password
    |email                    |password|
    |poobesh0012@putsbox.com  |Test@123|
    And I click on Submit button
    Then I navigated to LfnGo home page
    Then I click on profile menu
    When I click on Logout option
    And I acknowledge no
    Then I stay back to home screen
