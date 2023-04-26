*** Settings ***
Resource    /Users/guladulatova/PycharmProjects/pythonProject3/Resources/authenticationDefinedKeywirds.robot
Library    SeleniumLibrary
Resource    /Users/guladulatova/PycharmProjects/pythonProject3/Resources/CommonFunctionality.robot
*** Variables ***
${firstname}    Ivan
${email}        Sup@erSecr

*** Test Cases ***
Verify log and pas for a new user form
    [Documentation]  Authorization test
    [Tags]   functional
    [Setup]     Start Testcase
    Fill Form And Click
    Wait Until Element Is Visible    css:h1
    Element Text Should Be     css:h1       Congratulations! You have successfully registered!
    [Teardown]  Finish Testcase




*** Keywords ***


