*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Fill Form And Click
    Input Text    css:.form-control.first    ${firstname}
    Input Text    css:.form-control.third    ${email}
    Click Element    css:button[type=submit]