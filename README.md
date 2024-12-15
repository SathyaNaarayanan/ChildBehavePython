# ChildframeWork

Pre-Requisite:
Installation
    - IDE: Pycharm (Professional if applicable) 
    - Language: Python
    - Packages: behave, selenium, allure-behave
    - Reports to view in HTML:
      - java
      - node.js
      - npm
      - install allure-command line using below in command prompt
        npm install -g allure-commandline
    Add Python\scripts, java, nodejs, allure-command-line, npm in environmental variables

How to Run the test Execution:
    
    Method 1:
    In terminal use the below commands,
    1. behave <subDirectorypackage-name>/features #to run all the scenario in feature path
    2. behave <subDirectorypackage-name>/features --tags@one #to run specific scenario
    
    Method 2:
    1. Add configuration of the feature path to execute
    ![img.png](img.png)
    Click Edit Configuration and click ok
    Ref. ![img_1.png](img_1.png) 
    Now can able to Run or debug on our choice
    
    Method 3:
    To get the report post execution run the below command in the terminal
    behave ChildFrameworkMain/features -f allure_behave.formatter:AllureFormatter -o Reports
    To view the reports in HTML format -> Go the project structure and open command prompt and type
    allure serve Reports -> this will host the local browser and show the graphical report

Loggers:
    Logger file name #LYFnGO-Logger.log is added under sub-directory package to view the log files

Framework understanding:
    



    
    