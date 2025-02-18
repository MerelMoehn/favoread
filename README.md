![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

#FavoReads

Welcome,

In this document I will explain the reason and approach behind the FavoReads app. Imagine this, you just finished reading a good book, and now you have to look for another one. You don't have any inspiration and therefore you just my browse Amazon for hours. Wouldn't it be so much nicer to get book inspiration from someone who inspires you? Do you admire that one soccer player, or that bosswoman? Check out their bookcase and find your next book to read. In addition, you might also be an inspiration to others, so make sure you share your bookcase as well!

FavoReads is an application where users can create their own online bookcase while also being able to see the bookcases of other users. 

The last update to this file was: **January 19, 2023**

# Deployed project
The app can be accessed via the following link: [Click to go to Website](https://favoreads.herokuapp.com/) 

<img src="media/readme_images/FavoReads_Impression.png">

## Repository

[Find the project repository here.](https://github.com/MerelMoehn/favoreads)

# Table of Contents

## Contents
- [General introduction and instructions](#general-introduction-and-instructions)
  * [Project Approach](#project-approach)
  * [Epics & labels](#epics-&-labels)
  * [Project Planning](#project-planning)
- [User stories](#user-stories)
- [Features](#features)
  * [Future Features](#future-features)
- [Design & wireframing](#design-&-wireframing)
  * [Colourscheme](#colourscheme)
  * [WireFrames](#epics-&-labels)
  * [Typography](#typograpy)
  * [Cards](#icons)
  * [Icons](#cards)
  * [Imagery](#imagery)
- [Data Model](#the-data-model)
  * [The Book model](#the-book-model)
  * [The Bookcase_book model](#the-bookcase_book-model)
- [Technology Used](#technology-used)
  * [Languages used](#languages-used)
  * [Frameworks & Libraries used](#frameworks-and-libraries-used)
- [Testing](#testing)
  * [Validators](#validators)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
    * [W3C CSS validator](#w3c-css-validation)
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
  * [Bugs found and solved](#bugs-found-and-solved)
    * [Unsolved bugs](#unsolved-bugs)
- [Deployment](#deployment)
  * [Heroku](#heroku)
  * [ElephantSQL](#elephantsql)
  * [Creating a local clone](#creating-a-local-clone)
- [Credits](#credits)
  * [Code](#code)
    * [Code Institute](#code-institute)
    * [Django](#django)
    * [Bootstrap](#bootstrap)
  * [Acknowledgments](#acknowledgements)





# General introduction and instructions

## Project Approach
This application is built using an agile approach. Therefore, the functionalities were broken down into Epics & User stories, and these picked up in three sprints. Each sprint consisted of one week. 

## Epics & labels
The application features were broken down into Epics and hence in User Stories. 
For each User Story, an issue was created. The corresponding Epic was depicted via a label.
There were two additional labels: Front-End, Back-End. For each User Story it was often the case that there were some BE and FE functionalities. Therefore, most User Stories were split into two User Stories, one for BE, one for FE.

[All Epics/labels can be viewed here.](https://github.com/MerelMoehn/favoreads/labels)
The following Epics were defined:
- Account Management: Sign Up, Log-In, Log-Out
- Display Users & Books: the functionality of displaying a list of books or user/bookcase owners. This Epic was focused on the inspiration goal of this application.
- Add Books: this included the submitting of a new book to the application, as well as adding an existing book to one's own bookcase. Together with the next Epic, this Epic was focused on the Inspire goal of the application.
- Bookcase management: this included the management of one's own bookcase, in which a user can edit a book's status, or delete a book from the bookcase. Together with the previous Epic, this Epic was focused on the Inspire goal of the application.
- Project Prerequisites: this Epic was all about the project set-up and anything needed for project deployment.

Additional labels used:
- Bug: to label the bugs found and solved during the project
- Documentation: to label all stories related to creating the correct and sufficient documentation.
- Front-end: to label user stories focused on the Front-end
- Back-end: to label user stories focused on the Back-end

## Project Planning
The project was planned and built in four sprints each consisting of one week. The project tool used was GitHub Projects & Issues. The issues were mapped on a kanban board using labels and swimming lanes.

When I started working on an User Story, the story was added to the milestone and dragged and dropped into "in progress", when finished, the story was dragged & dropped into the "done" lane.
To clarify, I only noticed when having finished 95% of my project that setting a story to 'done' did not close the story. Therefore most of the stories have the same closing date.

I decided to focus on creating the main back-end functionalities first before focusing on front-end. This decision was made based on the availability of support during the Christmas holidays. 

[View stories/bugs included in sprint 1.](https://github.com/MerelMoehn/favoreads/milestone/1?closed=1)
[View stories/bugs included in sprint 2.](https://github.com/MerelMoehn/favoreads/milestone/2?closed=1)
[View stories/bugs included in sprint 3.](https://github.com/MerelMoehn/favoreads/milestone/3)
[View stories/bugs included in sprint 4.](https://github.com/MerelMoehn/favoreads/milestone/4)

# User stories

In the table below is an overview of the distinct User Stories. What I mean by that is the following, as mentioned some user stories are divided into two: FE & BE. The User Story is only named once in the table below.
In addition, some User Stories have overlap between the EPICS, for example, messaging. These are also only named once, but may be implemented for other EPICS as well.

The total number of issues (including bugs) created are: 47

| User Story ID | As a/an | I want to be able to... | So that I can... |
| --- | ----------- | ----------- | ----------- |
 | [Add Books](https://github.com/MerelMoehn/favoreads/issues?q=label%3A%22add+books%22+is%3Aclosed) | 
 | 1 | Registered User | Submit a book when not already online | share this with others | 
 | 2 | Registered User | Add an existing book to my bookcase | So I can create my online bookcase | 
 | 3 | Admin | Approve/disapprove submitted books | Ensure no books are entered double or that questionable books are allowed.| 
  | [Display Books & Users & Bookcases](https://github.com/MerelMoehn/favoreads/issues?q=label%3A%22Display+users+%26+books%22+is%3Aclosed) | 
 | 4 | Registered User | View a list of bookcase (owners) | Navigate to their bookcase and be inspired | 
 | 5 | Registered User | View the bookcase of another user | View the books in their bookcase and be inspired | 
 | 6 | Registered User | View individual books | So I can specifically add that book to my bookcase | 
 | 7 | Registered User | Display my own bookcase | So I can inspire others with the books I read |
 | 8 | Registered User | Navigate between the different site pages | So I see either books, bookcases or my own bookcase |
 | 9 | Registered User | View books paginated when more than 9 | Take the content to me in structured fashion |
 | 10 | Registered User | Delete books | Make sure there are no incorrect books |
 | 11 | Registered User | Search books | Easily find a book |
 | 12 | Developer | Create auto generated slugs | Connect books & bookcase detail pages to the correct book/bookcase | 
 | 13 | Site Owner | Showcase a few books & functionalities | Give website visitors a quick sense of the types of books and functionalities available on my website | 
  | [Manage Bookcase](https://github.com/MerelMoehn/favoreads/issues?q=label%3A%22Manage+Bookcase%22+is%3Aclosed) | 
 | 14 | Registered User | Update the reading status of my book | Show others an up to date bookcase | 
 | 15 | Registered User | Delete a book out of my bookcase | Show others an up to date bookcase |
 | 16 | Registered User | Automatically add a submitted book to my bookcase | So that I don't have to do this manually |
 | 17 | Registered User | See a confirmation message of my action | So that I know what is happening |
 | [Account Management](https://github.com/MerelMoehn/favoreads/issues?q=label%3A%22Account+management%22+is%3Aclosed) | 
 | 18 | Unregistered User | Easily register for an account | Join this book community | 
 | 19 | Registered User | Easily login or logout | View bookcases, upload books, and manage my bookcase | 
 | 20 | Registered User | Easily recover my password | Access my account even if I've forgotten my password | 
 | 21 | Unregistered User | Get an impression of the application from the homepage | Understand what the project is about | 
  | [Project Prerequisites](https://github.com/MerelMoehn/favoreads/issues?q=label%3A%22project+prerequisites%22+is%3Aclosed) | 
 | 22 | Developer | Set up my project | Build the base layout of my application |
 | 23 | Developer | Create the Data Models | Support my application with data | 
 | 24 | Developer | Deploy my application early | Check frequently if everything is working properly | 
 | 25 | Developer | Create automated tests | Ensure a reliable application | 
 | 26 | Developer | Create understandable code via commenting | Help other developers understand it |
  | [Documentation](https://github.com/MerelMoehn/favoreads/issues?q=label%3Adocumentation+is%3Aclosed) |
| 27| Developer | Create Wireframes | Ensure my application is properly designed | 
| 28 | Developer | Create a LucidChart Data Model | Ensure my Data Models are designed & documented correctly | 
| 29 | Developer | Document in a ReadMe file | Ensure my application is documented correctly & sufficiently | 

# Features
This application has several features which I will highlight per page.

- On the 'Home' page (index.html) the user can make us of the following features:
  - Register
  - Log-in
  - Log-out
  - Read three main functionalities
  - Go to the detail pages of three highlighted books, ordered based on last submitted
- On the 'Submit a book' page (submit_book.html) the user can make us of the following features:
  - Fill in the form to submit a book
  - Get feedback whether the action above has succeeded or not
- On the 'My Bookcase' page (user_bookcase.html) the user can make use of the following features:
  - See all the books in his/her bookcase
  - Update the reading status of each book in the bookcase
  - Delete a book from the bookcase, this book is then deleted from the Bookcase_book model
  - Receive a feedback message when doing one of the above two actions
  - Navigate between pages of books in the bookcase (pagination)
- On the 'Bookcases' page (bookcases.html) the user can make use of the following features:
  - A search bar functionality to search for books. The user can search via title or author. Only approved books and books that are not deleted, are displayed
  - Get a feedback message when the criteria did not get a result
  - See a list of other users/bookcase owners of the application
  - Click on a user to go to their bookcase
  - Navigate between pages of users in the list (pagination)
- On the 'Bookcase detail' page (bookcase_detail.html) the user can make us of the following features:
  - See all the books in the bookcase of the selected user
  - Click on a book to go to the book_detail page
  - Navigate between pages of books in the bookcase (pagination)
- On the 'Book detail' page (book_detail.html) the user can make use of the following features:
  - See the book details
  - Add the book to his/her own bookcase
  - Delete this book, the book is then soft deleted (chosen after consultation with mentor). One can only (soft) when he/she is the one that has uploaded the book. The person that has uploaded the book is shown after the submit date
  - Get feedback whether the action above has succeeded or not

The admin user has additional functionalities:
  - Log in to the admin panel
  - Review Users, Books, and Bookcase_books
  - Approve Books

## Future Features
The following features would be nice to add in the future:

- BookClub/Commenting functionality: it would be nice if FavoReads could also act as a BookClub community. One feature could therefore be to allow commenting on a specific book to be able to discuss the book online. 

- Bookcase like functionality: it could be a nice idea to allow users to like other users' bookcases. While 'likes' are also scrutinized on social media because they are not good for mental health it could increase the application engagement.

- Book rating functionality: it would be nice of users can like or rate books in the future so that highly rated books could be recommended to users by displaying them at the top of the page.

- Extend delete functionality: the delete Book functionality is now a soft delete. This is because, after consultation with my manager, it has been decided that it would be a nice functionality in the future to delete the book permanently after 30 days when the user has soft deleted the book.

# Design & wireframing
## Colourscheme
The design of the FavoReads application is based on the image below. Four colours are extracted and used for the main elements on the page. An additional colour was picked for the typografie. 
* Color for NavBar and Icons: #41585A
* Color for buttons and excerpt: #9A602A
* Color for background and white text: #F2EEED
* Color for footer and author: #A19F9E
* Color for text: #241F1C
<img src="media/readme_images/DesignColours_favoreads.png">

## WireFrames
[Click here for related user story.](https://github.com/MerelMoehn/favoreads/issues/20)
The wireframes created for this project were made in the online tool Miro. 

The wireframes were used as a rough sketch of what the application was meant to do and look like. This included the page navigation, the different pages needed, and a rough sketch of the design.
After initial set up of the main features the design was further implemented based on the design as described above.
<img src="media/readme_images/FavoReads Wireframing (1).jpg">

## Typography

- The typography used within the application is the following font-family: Roboto, sans-serif. These fonts were used because they are a fairly safe and modern choice and do not distract the attention from the books. 

## Cards
- I have used Bootstrap cards to visually organise content and to make the bookcase pages look like an actual bookcase. I have used both horizontal as vertical cards.

## Icons
- I used icons from Font Awesome website. They are used on the index page to depict the three main features of the website.

## Imagery 
- Imagery is used to give the application a more sophisticated look and to make it feel like an actual online bookcase.
- Images are mostly displayed within Bootstrap cards to mock the idea of a bookcase depicting multiple books next to each other.
- The user is able to provide an image of the book when submitting a book. When no book is uploaded the default book image is used.
- The images have been downloaded from Unsplash.com

# Data model
[Click here for related user story.](https://github.com/MerelMoehn/favoreads/issues/14)
The data model was created in LucidChart. 
The first data model included three models: Book, Bookcase, Bookcase_Book.
After implementing the first features and templates I realized that there was no need for three different models and that two models would suffice: Book and Bookcase_book. As the Bookcase_Book combines both the owner of the bookcase and the specific books, it acts as they bookcase for different users.

## The Book model
The Book model includes the following fields:
* Title: The title of the book, which needs to be unique. 
* Slug: A unique auto generated slug that will be used to create the  URL to navigate to a specific bookpage.
* Author: The author of the book. Does not have to be unique.
* Excerpt: A short one or two sentence description of the book.
* Featured_image: A picture of the book. A default is provided when the user does not upload an image. 
* Created_on: The Data and Time the book was created on.
* Approved: A True or False field, whether or not the admin has approved the book.
* Submitted_by: A foreign key to the User that has submitted the book
* Deleted: A True or False field, to show whether or not the book has been soft deleted. Based on advise of my mentor it was not a hard delete but a soft delete.
The Book model also has a method that auto generates a slug based on the title of the book. 

## The Bookcase_book Model
The Bookcase_book model includes the following fields:
* Bookcase_owner: A ForeignKey of the model User. Registers which User has added this book to his/her bookcase.
* Book: A ForeignKey of the model Book. Registers which Book it is about.
* Status: A choice field of which the choices are: Reading, Not Started, Read. To indicate whether or not the bookcase owner has read the book in his bookcase.
* Created_on: A DateTime field indicating when the Bookcase_book was created. This data is used to order the bookcase_books on descending DateTime.

<img src="media/readme_images/Favoreads_datamodels.png">

# Technology used
## Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks & Libraries used
- [Django](https://www.djangoproject.com/)
  - This website is built using Django, a high-level Python web framework. I have also used Django to provide an admin view, create forms and test my website. Further features used include 
  - [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) I used Allauth for user authentification. 
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)I used Crispy Forms for styling my form.

- [jQuery](https://jquery.com/)
  - I used jQuery to add functionality to Bootstrap components and within my scripts.

- [Bootstrap 4](https://getbootstrap.com/) 
  - I used bootstrap throughout the site to make it responsive. I sourced code from the Bootstrap documentation when building the Navbar, Cards, Messages and Buttons.

- [Google Fonts](https://fonts.google.com/)
  - Fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome on the index page.

- [Cloudinary](https://cloudinary.com/)
  - I used images that were stored on Cloudinary.

# Testing
## Validators
### CI Python Linter
All custom code passed the the CI Python Linter validation, without any errors.
The following files were passed through the linter:
* admin.py
* apps.py
* forms.py
* models.py
* test_admin.py
* test_forms.py
* test_models.py
* test_views.py
* urls.py
* views.py

### Lighthouse
Each site page has been checked with Lighthouse and the following improvements have been made:
* Using smaller images to load page faster
* include meta tag on base.html
* Language has been set in base.html
* Non unique ARIA IDs are made unique
* Remove big layout shift with buttons for user bookcase
For pages that are not rendering images, all indicators are green. However, uploading images with different sizes decreases the performance score.

### W3C CSS Validation
The style.css code has been validated by the W3C CSS validator and passed without any errors.

## Manual Testing
In this section I explain what manual testing has been done. Note that I am referring to manual testing after the main development stage was finished. Bugs found during development were handled immediately. This section shows the test that were all expected to be succesfull after development, but where still some bugs were found. 
The test description is also indicative for the action that has been done to test it. Meaning, for the test: 'Sign up, log-in, log-out' I'm testing these functionalities by signing up, loggin-in, and logging-out.

Manual tests that have been done:
Registration:
- Sign up, log in and log out: succesfull
- Authentication: unsuccesful: a not logged in user could get by pages via the urls. [Go to bug.](https://github.com/MerelMoehn/favoreads/issues/48)
Submitting/adding/deleting book:
- Submitting a book, including feedback message: succesfull
- Uploading an image while submitting a book: unsuccesful: [Go to bug.](https://github.com/MerelMoehn/favoreads/issues/46) 
- Soft deleting books, and deleting book from bookcase, including feedback message: succesfull
- Updating the reading status of a user's own books: succesfull
- Approving a book by the admin in the admin panel: succesfull
- Adding a book the one's bookcase, including feedback message: succesfull
Book Search:
- Search for a book based on title or author: succesfull, but adjusted the placeholder text from 'Enter title' to 'Enter title or author'.
- Get feedback message when no search criteria is entered: succesfull
- Get feedback message when no match has been found: succesfull
Socials:
- Links of socials open in blank page: succesfull
General site functionality:
- Pagination: unsuccesful. Pagination was not working on the bookcases page. [Go to bug.](https://github.com/MerelMoehn/favoreads/issues/47) 
- Responsiveness, mainly focused on mobile. This resulted in multiple bugs to fix the responsiveness of the 'My Bookcase, Bookcases, Bookcase_detail and Sign-up page'. [Go to bug.](https://github.com/MerelMoehn/favoreads/issues/41) 

## Automated testing
In total there are 23 automated tests which cover 95% of the application.
One of the views: Bookcases, could not be tested because the local database does not support DISTINCT.
DISTINCT is used for getting the bookcase_owners only once, to display the list of users with a bookcase.
<img src="media/readme_images/FavoReads_automated_tests.png">
All tests pass. 
<img src="media/readme_images/FavoReads_automated_testresults.png">

## Bugs found and solved
Throughout the project there were multiple bugs found and solved. These bugs were logged on the GitHub project and can be reviewed via the following link: [Click here to review the bugs.](https://github.com/MerelMoehn/favoreads/issues?q=label%3Abug+is%3Aclosed) 

### Unsolved bugs
At the moment of submitting and deployment, there were no unresolved bugs.

# Deployment
## Heroku
The project was deployed to Heroku using the following steps:
1. I pushed my final code via the terminal after finishing the project.
2. I created a new Heroku app
3. I set the build backs to 'Python' and 'NodeJS' in that order
4. I linked the Heroku app to the repository
5. I pushed my final code via the terminal after finishing the project.
6. Then I selected 'deploy'

## ElephantSQL
The database was set up by following the steps beneath:
1. Log in to ElephantSQL.com to access your dashboard
2. Click “Create New Instance”
3. Set up your plan
4. Select “Select Region”
5. Select a data center near you
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, click the copy icon to copy the database URL
10. The proper steps were taken in the settings.py file to connect with the database.

## Creating a local clone
You can create a local clone of the repository via the following steps:
1. navigate to the main page of the repository
2. download the code
3. Copy the URL for the repository.
4. Open Terminal
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.

For more detailed instructions, navigate to the following page:
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

# Credits
## Code
### Code Institute:
  - I based the set up of this project on the Code Institute Django walkthrough projects. I have customised my website wherever possible.

### Django:
  - I referred to the Django documentation whilst building my project.

### Bootstrap:
  - I have used Bootstrap classes throughout my project, including for layout utilities and cards. I sourced code from the Bootstrap documentation when building the Navbar, Cards, Dropdown, and pagination.

## Acknowledgements
- Thank you to my mentor for helpful feedback, industry insights and recommended tools.

- Thank you to the tutors and staff at Code Institute for their support.


Thank you!