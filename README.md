<h1 align="center">New Irish Life</h1>

Web-based travel guide for providing correct information on how easily start living and working in Ireland.
Finding work, a place to stay where to buy good cheap food in Ireland can be difficult but with the correct preparation,
advice, and planning this task can be made a lot easier.
This website is a great starting point.

![Website Main Mockup](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Main.png)

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [User Story](#User-Story)
    * [Design process](#Design-process)
* [Features](#FEATURES)
    * [Home](#HOME)
    * [Trip](#TRIP)
    * [Work](#WORK)
    * [Life](#LIFE)
    * [Tips](#TIPS)
    * [Sign Up](#SIGN-UP)
    * [Login](#LOGIN)
    * [Profile](#PROFILE)
    * [Add Tip](#ADD-TIP)

* [Technologies used](#TECHNOLOGIES-USED)
* [Testing](#TESTING)
* [Deployment](#DEPLOYMENT)
* [Credits](#Credits)

****

# UX

**Story:**
<h4 align="center">Four years ago, one Croatian landed in Dublin, Ireland. On the web, 
there was a lot of info about life in Ireland, but not essentials information in one place.
</h4>
<h3 align="center">Well, not anymore!</h3>

### User Story

**As a new Irish resident, I want all _NECESSARY AND IMPORTANT_ information for my [New Irish Life](http://new-irish-life.herokuapp.com/home) in one place and available from any device connected to the internet, so I can organize my life in a fun and simple way.**

**In the [Trip](http://new-irish-life.herokuapp.com/trip) section, I want to have quick access to the most popular online travel brands and quick links pointing me to _"FLIGHTS"_, _"HOTELS"_, _"CAR HIRE"_, and brands _" REVIEWS"_.**

**I the [Work](http://new-irish-life.herokuapp.com/work) section, I want to have quick access to the most popular recruitment websites and quick links pointing me to _"JOB SEARCH"_, _" EXPECTED SALARIES"_, _"COMPANIES"_ and agency _" REVIEWS"_.**

**I the [Life](http://new-irish-life.herokuapp.com/life) section, I want to have quick access to the most up-to-date rental website links pointing me to _"SHARE ROOMS"_, _"STUDENTS"_, _" APPARTMENT TO BUY"_, and holiday options, most popular mobile network providers, and most popular grocery shops.**

**Straight after arrival at Dublin Airport if I click on a [Trip](http://new-irish-life.herokuapp.com/trip) section I want to see Google Maps with some option for bus, train, or tram stations with visible markers in different colors for the fastest navigation.**

**I the [Tips](http://new-irish-life.herokuapp.com/tips) section,  I want to read posts from other users and their pieces of advice for the best traveling routes, work opportunities, study options, and good food places.**

**By frequently referring to New Irish Life content, I want to have the ability to [create](http://new-irish-life.herokuapp.com/registration) my profile for full New Irish Life usage.**

**In the [Sign Up](http://new-irish-life.herokuapp.com/registration) process, I want to have the ability to register with my Username, Email, and password-strength of my choice. During the registration process, I want to be alerted if my Username and Email are unique or already in use.**

**In the [Login](http://new-irish-life.herokuapp.com/login) process, I want to login with my Username and Password and be redirected to my Profile page with a welcoming message, where I can see my details: Username, Email, Join Date. I want to have an option to DELETE my profile with a pop-up warning and confirmation message.**

**When I log out I want to see a successful logout message and be redirected to the [Home](http://new-irish-life.herokuapp.com/home) page.**

**As an active user, I want to have the choice to create Tips from my experience living in Ireland and have an option for 4 categories: Trip, Work, Study, and Food. If I want to update my Tips I want to see an update or delete option for all of my posted tips.**

**As not an active user I want the ability to search [Tips](http://new-irish-life.herokuapp.com/tips) from other users with targeting tips title or tips description for specific keywords.**

**I want to stay up-to-date with all fresh information regarding work and lifestyle by subscribing to my email for newsletter services. I want to know if my email is valid when I'm submitting my request for newsletter services.**

**When I'm submitting my name and email for newsletter services I want to receive a message that my request is submitted with the confirmation message.**

**When I'm browsing through the website I want to access each URL directly so it feels like a single app website.**

**With [New Irish Life](http://new-irish-life.herokuapp.com/home), all of this is possible!**


### Testing User Stories from User Experience (UX)
* Definition by **HOME** section - As a First Time Visitor, I want to easily understand the main purpose of the site and my benefit of the [New Irish Life](http://new-irish-life.herokuapp.com/home):
  * Upon entering the site user can see a clear navigation bar and company logo.
  * The main purpose is represented with a short introduction paragraph and hero image gallery.
  * Website content is pointed with four visual design cards for each section of the site.
  * Footer is well structured and offers links for the main site section and full operating Newsletter form service.
  * User can share [New Irish Life](http://new-irish-life.herokuapp.com/home) on four social media links presented in the bottom part of the footer.
  * The main navigation menu and footer are replicated through all main sections of the website.

* Definition by **TRIP** section - As a First Time Visitor, I want to easily understand section purpose with a short and fun intro paragraph and slide-show intro gallery:
  * User can choose the most popular online travel brands to organize in card elements.
  * Each card element contains the main link, the brand website screenshot, the **_"Quick links..."_** option, and a brand description.
  * User can have access to the best Irish public transportation services.
  * Users can navigate through embedded Google Map with colorful markers representing the most important bus stations, train stations, and tram stations in Dublin, Ireland.

* Definition by **WORK** section - As a First Time Visitor, I want to easily understand how to start a job search process with the best possible preparation for the Irish work market:
  * Users can quickly understand where to start the job search process.
  * User can understand what kind of [CV](https://tsokac2.github.io/newIrishLife.3.0/static/downloads/Tomislav_Sokac_CV.pdf) template is necessary for a successful job search mission.
  * User can find the best option for online education with the best offers.

* Definition by **LIFE** section - As a First Time Visitor, I want to easily find the best online rental marketplaces, the most popular mobile networks provider, and large-chain grocery shops
  * User can choose one of the four most popular Irish online rental portals with quick links for share accommodation or buy options.
  * Users can quickly decide for best mobile network providers regarding broadband speed, bill pay offers, Tv broadband offers.
  * Users can check the four largest grocery shop chains with previous user reviews, best deals, work offerings.

* Definition by **SIGN UP** section - As a First Time Visitor, I want to see straight up what kind of details are needed for a successful registration:
  * By entering Username, the user can see if chosen Username is already taken or is below 2 characters, or it is completely valid.
  * By entering an Email address, the user can see if the email address is valid or already in use, or is completely valid.
  * By entering the password, the user must confirm the password for additional data security.

* Definition by **LOGIN** section - After the first successful registration, I want to be redirected to the login page and enter my username and password:
  * By entering the Username and password and if either input details are invalid, the user is receiving a warning message.
  * By entering the correct username and password the user is redirected to the profile page.

* Definition by **PROFILE** section - After the first successful login, I want to be redirected to my profile page: 
  * On the profile, page the user can see the following details: Username, Email, and Joining Date.
  * User has the choice to DELETE their profile.
  * If the user clicks on the DELETE button, a pop-up message is appearing for delete confirmation.
  * If the user clicks "YES" to confirm the delete process, the user is redirected to the HOME page with the message:  **_"Your profile is deleted!"_**.

* Definition by **TIPS** section - As a First Time Visitor, I want to easily read through other users tips and tricks regarding work, commuting, study options, and restaurants choices:
  * A user can search posts with keywords targeting tip title and tip description witch will result in redirecting to a search result page.
  * By focusing on tips categories titles, users can quickly navigate and read from desired column section.
  * If the user is logged in, users can **_Create_**, **_Update_**, and **_Delete_** tips.
  * When the user creat tip, the user is redirected to the **TIPS** section with the success message **_Tip successfully added!_**


### Design process
**1.** Draft all main sections - **HOME**, **TRIP**, **WORK**, **LIFE**, **TIPS**, **SIGN UP**, **LOGIN**, and **PROFILE**.

**2.** Brief list of all pop-ups and alert messages and their front-end placement.

**3.** List all color pallets - usage - background color, font color, border.

**4.** List all font styles for best UX, regarding user profile details, movie quotes, post titles, and descriptions.

**5.** A list of free images from the free-image web platforms for each project section.

**6.** Draft web-page layout using Adobe Photoshop and Balsamiq for the main layout and Adobe Illustrator for layout components such as Logo, borders, navigation elements.

**7.** List possible Fowtawesome Icon for best UX in picture experiences and a draft of custom icons.

**8.** Plan Python and Flask implementation into project root infrastructure folder.

**9.** List Semantic Mark-up to structure HTML code.

**10.** List CSS folder structure for SASS Pre-processor configuration.

**11.** List of preferable Python packages for best possible performance and UX. 

**12.** Plan database collections structure - user collection details, user tips collection details, and tips categories list

**13.** Plan and implement Google Maps API for orientation purposes.

**14.** Plan and implement Emailjs API service for Newsletter form.

**15.** Take notes for all major development issue, their solutions, challenges, project credits, and SLACK community guidance.


### Wireframes
* **HOME** section general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Home.png)
* **TRIP**, **WORK**, and **LIFE** sections general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Trip.png)
* **TRIP**, **WORK**, and **LIFE** - **_"Quick links"_** cards general idea for Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_MW.png)
* **TRIP GOOGLE MAPS** section general idea - for Large and Small screens devices [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Trip_Maps.png)
* **TIPS** section general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Tips.png)
* **SIGN UP** section general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Registration.png)
* **LOGIN** section general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Login.png)
* **PROFILE** section general idea - for Large and Small screens devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_Profile.png)
* **FOOTER** section general idea - for Small devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_MF.png)
* **MAIN MENU** section general idea - CSS Grid elements - for Small devices - [View](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_MM.png)

### Main Layout
* MENU: HOME | TRIP | WORK | STUDY | TIPS  --LOGO--  SIGN UP | LOGIN - after user login - +TIPS | PROFILE | LOGOUT
* MAIN SECTIONS: Website features - HOME, TRIP, WORK, LIFE,  SIGN UP, LOGIN - +TIPS | PROFILE
* FOOTER: Footer Menu links - Newsletter Subtraction - Social Media links - Copyrights

****

# FEATURES

## HOME
Simple introduction of web page purpose and what value it is bringing to an end-user.

Formatted in three main sub-sections:
* Movie reference pitch - from -  _"The Hobbit: An Unexpected Journey"_
* Welcoming **_"Hero"_** area with picture composition
* Quick box-model overview of the web page main sections
* Footer section including; Mirroring top left menu for **HOME**, **TRIP**, **WORK**, **LIFE**, **TIPS**, followed with **Newsletter** user email subscribe services form [View Screenshot](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/email.png) and finishing with social networks links for user sharing purposes
* The Footer section is replicated across all website sub-section pages for better UX

## TRIP
Section introduction with intro reference and **"call-to-action"** headings

Formatted in two main sub-sections:
* **_CHOOSE WISELY_** Flights booking web services
* **_HOP ON_** Ireland public transportation's most popular options and guidelines
* **Quick Links...** quick link option for precise user search in specified link area - [View Screenshot](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/quicklinks.png)
* **Google Maps** with a tracker for public transportation and _"Hot"_ locations in Dublin city with 3 markers in different colors for **Dublin Bus**, **Dart Train**, and **Luas** services - [View Screenshot](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/googlemap.png)

## WORK
Introduction and quick links of the most popular Irish online recruitment sites with an additional section for online education possibilities

Formatted in two main sub-sections:
* **_START HERE_** Most popular job search services for the Irish job market
* **_BACK TO SCHOOL_** Most popular online courses and full-time education institutions
* **_Quick Links..._** quick link option for precise user search in specified link area - [View Screenshot](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/quicklinks_work.png)

## LIFE
Section with life essentials factors after moving to Ireland

Formatted in three main sub-sections:
* **_ACCOMMODATION_** Online rental agencies
* **_MOBILE NETWORKS_** Mobile/internet networks providers
* **_GROCERY SHOPS_** Irish Top food chains for grocery shopping
* **_Quick Links..._** Quick link option for precise user search in specified link area - [View Screenshot](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/quicklinks_life.png)

## TIPS
Section with tips and useful advice from other users

Formatted in three main sub-sections:
* **_TIPS_** Introduction and purpose of the tips section
* **_SEARCH_** Ability to search posted tips by referring to tip title and tip description
* Tips cards container with four tip categories including  _Trip_, _Work_, _Study_, and _Food_ 

## SIGN UP
Section with the option to _create_ a user profile for full website management

Formatted in three main sub-sections:
* **_Create Account_** Registration form including inputs fields for; _Username_, _Email_, _Password_, Confirm Password_ and _Sign Up_ button
* Overview of the website purpose displayed in four cards - **_Trip_**, **_Work_**, **_Life_**, **_News_**
* Home hero area with photo composition styling

## LOGIN
Section with the option to _login_ to a user profile for full website management

Formatted in three main sub-sections:
* **_Already a member_** Login form including inputs fields for; _Username_, _Password_ ,and _Login_ button
* Overview of the website purpose displayed in four cards - **_Trip_**, **_Work_**, **_Life_**, **_News_**
* Home hero area with photo composition styling