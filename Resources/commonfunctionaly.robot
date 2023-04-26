*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Start Testcase
    Open Browser    http://suninjuly.github.io/registration2.html   chrome
    Maximize Browser Window

Finish Testcase
    Close Browser
