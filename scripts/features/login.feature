Feature: Instragram Login
	In order to test the Instagram web application
	As a mobile user
	I want to be able to login into the application
	using already existing login credentials
	
Scenario: Login
	Given I open login page "https://www.instagram.com/accounts/login/"
	When I login with email "YOUR_USERNAME" and password "YOUR_PASSWORD"
	Then I am on main page

	