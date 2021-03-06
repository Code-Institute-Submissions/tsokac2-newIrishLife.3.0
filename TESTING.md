## Table of Contents
* [Cloud-Based Validators](#Cloud-Based-Validators)
    * [W3C HTML Validator](#W3C-HTML-Validator)
    * [W3C CSS Validator](#W3C-CSS-Validator)
    * [JSHint Validator](#JSHint-Validator)
    * [PEP8 Validator](#PEP8-Validator)
* [Test Cases Description and Results](#Test-Cases-Description-and-Results)
* [Local Based Validators](#Local-Based-Validators)
  * [Python Unit Testing Framework](#Python-Unit-Testing-Framework)
  * [Jasmine](#Jasmine)
* [W3 Validator Errors and Solutions](#W3-Validator-Errors-and-Solutions)
* [Developer Tools Console Logs Errors and Solutions](#Developer-Tools-Console-Logs-Errors-and-Solutions)
* [Testing WARNINGS](#Testing-WARNINGS)

****

## Cloud-Based Validators

### [W3C HTML Validator](https://validator.w3.org/#validate_by_uri)

* HTML [Home Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Home.png) - No errors
* HTML [Trip Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Trip.png) - No errors
* HTML [Work Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Work.png) - No errors
* HTML [Life Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Life.png) - No errors
* HTML [Tips Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Tips.png) - No errors
* HTML [Registration Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Registration.png) - No errors
* HTML [Login Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Login.png) - No errors
* HTML [Add_Tip Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_H_Add_tip.png) - No errors

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* CSS [index.css Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_CSS.png) - No errors

### [JSHint Validator](https://jshint.com/)
* JS file [emailnews.js Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_emailnews.png) - No errors
* JS file [maps.js Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_maps.png) - No errors
* JS file [cards.js Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_cardsjs.png) - No errorsTESTING

### [PEP8 Validator](http://pep8online.com/)
* Python file [app.py Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_PEP8_app.png) - No errors
* Python file [forms.py Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_PEP8_forms.png) - No errors
* Python file [test.py Result](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/W3_PEP8_test.png) - No errors

****

## Test Cases Description and Results

Full test results can be found in an excel document **[HERE](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/M3_Testing.xlsx)**

![Test Results](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/wireframes/TC001.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/TC004.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/TC006.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/TC007.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/TC008.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/TC009.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/test12.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/test16.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/test20.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/test25.png)
![Test Results](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/test27.png)

****

## Local Based Validators

### [Python Unit Testing Framework](https://docs.python.org/3/library/unittest.html)
Testing was processed to ensure that routing functionality is redirecting users to the requested page route.

#### Testing covered:
* Test **Home** page load response
* Test **Trip** page load response
* Test **Work** page load response
* Test **Life** page load response
* Test **Tips** page load response
* Test **Sign Up** page load response
* Test **Login** page load response
* Command-line 7 [Tests Result](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/W3_unittest.png)

**FULL SOURCE CODE:** [test.py](https://github.com/tsokac2/newIrishLife.3.0/blob/main/test.py)

### [Jasmine](https://jasmine.github.io/)
Behavior-driven development framework for testing JavaScript code.

#### Testing DOM Events Using jQuery and Jasmine 2.0
1. STEP: Create a **testing** folder in the project root folder - **../testing**

2. STEP: Create **cardsSpec.js** file in to **../testing/spec** folder

3. STEP: Create **cardstest.html** file in a **testing** folder

4. STEP: In **cardstest.html** create basic **<!DOCTYPE html>** structure with **`<html>`**, **`<head>`** opening and closing tags

5. STEP: In the **`<head>`** element place **CDN** links in the following order - **[CDN SOURCE](https://cdnjs.com/libraries/jasmine)**:
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.js"></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine-html.js" ></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/boot.js"></script>`
  * `<script src="https://code.jquery.com/jquery-3.5.1.js"></script>`
  * `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.css"/>` **[SOURCE](https://code.jquery.com/)** 
  * `<script src="../testing/libraries/jasminejquery.js"></script>` external library **[SOURCE](https://bowercdn.net/c/jasmine-jquery-2.1.1/lib/jasmine-jquery.js)**  

6. STEP: Import custom scripts for Jasmine testing under imported **CDN's** in the following order:
  * `<script src="../testing/scripts/cards.js"></script>`
  * `<script src="../testing/spec/cardsSpec.js"></script>`

**Test Steps**

* `setFixtures('<button id="showLinks1"</button>');`        - mimicking `<button>` element on line 265 in trip.html
* `$('#showLinks1').on('click', function (){...}`           - referencing jQuery DOM events applied to `<button>` element
* `var spyEventShow = spyOnEvent('#showLinks1', 'click');`  - creating variable var `var spyEventShow;`for invoking `spyOnEvent` on to `<button>` element
* `$('#showLinks1').trigger('click');`                      - triggering DOM event
* `expect(spyEventShow).toHaveBeenTriggered();`             - including `spyEventShow` variable in to `.toHaveBeenTriggered()` test instance

**FULL SOURCE CODE:** [Jasmine - cardsSpec.js](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/testing/spec/cardsSpec.js)

**Live Version** - [Cards Test](https://tsokac2.github.io/newIrishLife.3.0/static/testing/cardstest.html)

#### Testing Validation Functions for EMAILJS API Newsletter services

1. STEP: Create a **testing** folder in the project root folder - **../testing**

2. STEP: Create **emailnewsSpec.js** file in to **../testing/spec** folder

3. STEP: Create **emailnewstest.html** file in a **testing** folder

4. STEP: In **emailnewstest.html** create basic **<!DOCTYPE html>** structure with **`<html>`**, **`<head>`** opening and closing tags

5. STEP: In the **`<head>`** element place **CDN** links in the following order - **[CDN SOURCE](https://cdnjs.com/libraries/jasmine )**:
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.js"></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine-html.js" ></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/boot.js"></script>`
  * `<script src="https://code.jquery.com/jquery-3.5.1.js"></script>`
  * `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.css"/>` **[SOURCE](https://code.jquery.com/)**: 

6. STEP: Import custom scripts for Jasmine testing under imported **CDN's** in the following order:
  * `<script src="../testing/scripts/emailnews.js"></script>`
  * `<script src="../testing/spec/emailnewsSpec.js"></script>`

**Test Steps**

* Testing if `validateName()` function exist

  ```
  describe("Validate Name", function(){
    it("validateName() function should exist", function(){
        expect(validateName).toBeDefined();
    });
  ```
* Testing if `validateName()` function return **TRUE** if input `value.length` is > that 2

  ```
  it("validateName should return TRUE", function(){
      var testPass = validateName("Tom");
      expect(testPass).toBe(true);
  });
  ```

* Testing if `validateName()` function return **FALSE** if input `value.length` is < that 2

  ```
  it("validateName should return FALSE", function(){
      var testFaild = validateName("T");
      expect(testFaild).toBe(false);
  });
  ```

**FULL SOURCE CODE:** [Jasmine - emailnewsSpec.js](https://github.com/tsokac2/newIrishLife.3.0/blob/main/static/testing/spec/emailnewsSpec.js)

**Live Version** - [Emailnews Test](https://tsokac2.github.io/newIrishLife.3.0/static/testing/emailnewstest.html)

****

## W3 Validator Errors and Solutions

**ISSUE #1**
 _Error_: Duplicate ID username - `<input type="text" id="username" placeholder="Username or Email">`

 _SOLUTION_: Create unique  ID - `id="username"` for Sign Up form  - `id="username-log"` for Login form

**ISSUE #2**
_Error_: Bad value `public\img\Logo.png` for attribute src on element img: Backslash ("\") used as path segment delimiter.

`<img src="assets\img\Logo.png" width="100" alt="New Irish Logo"></a>`

_SOLUTION_: `<img src="assets/img/Logo.png" width="100" alt="New Irish Logo"></a>` - change "\" to "/"

**ISSUE #3**
_Error_: The `aria-labeled by` attribute must point to an element in the same document.

`<div class="modal fade" id="sing-in" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">`

_SOLUTION_: ` <div class="modal fade" id="sing-in" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="sing-in" aria-hidden="true">`

_SOLUTION SOURCE_ -  [Stackoverflow](https://stackoverflow.com/questions/39831658/how-to-fix-the-aria-labelledby-attribute-must-point-to-an-element-in-the-same-d)

**ISSUE #4**
_Error_:??Duplicate attribute??class.

_SOLUTION_: Remove class duplicates in `<a href="https://www.jetcost.ie/" target="_blank" class="q-links a">FLIGHTS</a>`

**ISSUE #5**
_Error_: The??type??attribute is unnecessary for JavaScript resources

_SOLUTION_: Remove type attribute from`<script  src="assets/js/emailnews.js"></script>`

**ISSUE #6**
_Error_: No space between attributes

_SOLUTION_: Add space between `<script>` and `src=""` attribute in `<script  src="assets/js/emailnews.js"></script>`

**ISSUE #7**
_Error_: Start tag seen without seeing a doctype first. Expected `<!DOCTYPE html>`

_SOLUTION_: Add doctype before opening `<html>` DOM element

**ISSUE #8**
_Error_: `.section-home .quote a` 	Value Error : font-size only 0 can be a unit. You must put a unit after your number: 1.5

_SOLUTION_: Add unit type after font-size property value `font-size: 1.5rem;`

**ISSUE #9**
_Error_: `.section-home .intro-pitch .pitch-wrap .composition` Value Error : margin-top ??2rem is not a margin-top value : ??2rem

_SOLUTION_: Remove extra space in `margin-top:  2rem;` to `margin-top: 2rem;`

****

## Developer Tools Console Logs Errors and Solutions

**ISSUE #1**
Error:  CSS background property - bad path property `background-image:??url("../img/rent_fav.png");`

SOLUTION: `background-image:??url("../img/rent_fav.png");` - no quotes

SOLUTION SOURCE: [Stackoverflow](https://stackoverflow.com/questions/21374534/css-background-image-not-loading)

**ISSUE #2**
Error:  jQuery .show() and .hide() - not applicable on DOM elements

SOLUTION: Implement jQuery Core 3.5.1 - uncompressed version - [jQuery](https://code.jquery.com/)

**ISSUE #3**
Error: Uncaught TypeError: Cannot read property 'querySelector' of null - selector does not return any elements at the stage when the script is executed

SOLUTION: Confirm that all DOM has a unique ID selector - if element in header section has same ID like element in footer section `document.getElementById("footer-element-id")` will have value of null

**ISSUE #4**
Error:
> Google Maps API - "We have detected a publicly accessible Google API key associated with the following Google Cloud Platform project"
SOLUTION:
1. If this key is intended to be public (or if a publicly accessible key isn???t preventable):
	- Log in to the Google Cloud Console and review the API and billing activity on your account, ensuring the usage is in line with what you expected.
	- Add??API key restrictions??to your API key, if applicable.
2. If this key was NOT meant to be public:
	- Regenerate the compromised API key: Search for Credentials in the cloud console platform, Edit the leaked key, and use the Regenerate Key button to rotate the key. For more details, review the instructions on??handling compromised GCP credentials.
	- Take immediate steps to ensure that your API key(s) are not embedded in public source code systems, stored in download directories, or unintentionally shared in other ways.
	- Add??API key restrictions??to your API key, if applicable.
The security of your Google Cloud Platform account(s) is important to us.

**ISSUE #5**
Error:

![PY_1](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/P1_1.png)

SOLUTION: Define the correct path for profile.html in the `app.py` file


**ISSUE #6**
Error:

![PY_2](https://github.com/tsokac2/newirishlife.3.0/blob/main/static/wireframes/P1_2.png)

SOLUTION: Define the correct filed name in users collections on MongoDB


## Testing WARNINGS

The [New Irish Life](http://new-irish-life-3-0.herokuapp.com/home) project is based on Python and MongoDB for code infrastructure and deployment and "Live" usage on the Heroku platform.

Since developers don't have control of Heroku and MongoDB cloud services/servers, in some rare cases testers can expect console warnings regarding connection links between Heroku and MongoDB that are affecting website performance.

Similar behaviors are spotted during the development and testing process.