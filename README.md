 #        QA-DevOps DfE Cloud Specialism - Final Project (Pizza App)
 Pizza repository contains my final deliverable QA DevOps Fundamental project.
 
## Contents:
* [Pizza App ERD](#The-Pizza-ERD)
* [The Project Tracking](#The-Project-Tracking)
* [The Testing](#The-Testing)
* [The Pizza App](#The-Pizza-App)


## Pizza App ERD:
![pizza app diagram](https://user-images.githubusercontent.com/97620234/156920546-628642e1-224c-434b-888c-2dd35b31b57c.png)

## The Project Tracking
The Jira board was used to track the application. The link to project tracking board can be found here https://erhnaks.atlassian.net/jira/software/projects/QP/boards/4

![Jira Board](https://user-images.githubusercontent.com/97620234/156923917-ef72d51e-21e0-451b-ae6e-a80f4bfbb20f.png)


## The Testing
Unit tests were writtent to test CRUD functionality to ensure that these fucntions worked as intented.

The coverage reports showing test achieved 88% report coverage.

**Coverage Report %88** 
HTML Report

![test_coverage_report](https://user-images.githubusercontent.com/97620234/156923008-3595b4d3-afc2-45c3-8c41-3111c0fb92a7.png)

Pytest Coverage Report;

![test_report](https://user-images.githubusercontent.com/97620234/156922992-8a9f9076-6420-426e-9679-306896e389d0.png)


## The Pizza App:

When app launch the user is shown the homepage:

![Pizza app homepage](https://user-images.githubusercontent.com/97620234/156920895-294f1f69-33ce-437c-bb26-624cbfd0ca70.png)

The application **Navbar** provides links to the endusers to add a chef, view created chef's and their pizza's.  T create a chef, the user simply clicks on the link and the app takes them to the **create** a chef page:

![Pizza app Create a Chef Page](https://user-images.githubusercontent.com/97620234/156920978-431d876c-48e2-48bb-84f3-256ac62c6705.png)

The user is then redirected to a page where they can the presented with their created chef details.

![Created a chef](https://user-images.githubusercontent.com/97620234/156921821-f94f3ecb-4bba-454e-b154-cf6f2bedadff.png)

User then be able to **create** a pizza with their desired seletions of pizza crust, base, and toppings at createapizza page;

![Pizza app Create a Pizza page](https://user-images.githubusercontent.com/97620234/156921052-7f1cc4b7-8ee9-4221-934e-0fc79db3149c.png)

User is then taken to homepage where they can see their custom made pizza on **read** page(s):

![Pizza app Created Chef and a Pizza related to the chef](https://user-images.githubusercontent.com/97620234/156921154-6ec1f88f-953d-494d-944b-59eece8badc8.png)

Users can **update** their chef name or delete their name and any of their created custom made pizza in the homepage:

![Pizza app Updated Chef Name and a Pizza related to the chefname auto updated](https://user-images.githubusercontent.com/97620234/156921279-4f6cbe50-caff-4915-92a0-008056187805.png)

User can **delete** their chef or pizza details;

![Deleted a pizza and the app kept the updated chef](https://user-images.githubusercontent.com/97620234/156921378-220afc23-c177-4a49-9af5-e30c38cbe6d0.png)




