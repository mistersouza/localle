Back to [README.md](/README.md)

# Testing

## Validation

### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-html-home.png) | ✅ |
| All Items |![All items](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validador-html-items.png) | ✅ |
| Item |![Item](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-html-item.png) | ✅ |
| Add & Edit Item |![Create Listing](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-html-add.png) | ✅ |
| Log In |![Log In](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-html-login.png) | ✅ |
| Sign Up |![Sign Up](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-html-signup.png) | ✅ |

### CSS

▷ While the live site's running smooth without any noticeable glitches, I'm wrestling with Bootstrap 5 variables to make them play nice with the CSS validation engine. It's a bit of a challenge, but I'm diving in to crack the code

Test Results CSS ==FAIL==

### JavaScript

- script.js ✅

![Validate JavaScript](https://github.com/mistersouza/localle/blob/main/static/assets/images/localle_validator-js.png)

## Browser Friends

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | ✅ | God bless Bootstrap |
| Firefox | All pages, load as expected. All features work as expected | ✅ | Amen |

## Manual Testing

- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Listings link in Navbar|Redirect to Listings Page |Pass|Navbar present on all pages |
||Click on Create Listing link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Profile link in Navbar|Redirect to My Profile Page |Pass|Navbar present on all pages |
||Click on Log Out link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Login/Sign Up in Navbar|Redirect to Login Page |Pass|Navbar present on all pages |
|Hero section|Open Home page. Ensure the hero section loads as it should|Hero section loads as it should |Pass| |
|Search form|Open the Home page. Ensure the search form section loads as it should|Search form section loads as it should |Pass| |
||Click on each input field. Ensure all choices are loaded.|All input fields appear as they should. |Pass| |
||Search listings by a combination of filters. Ensure the results displayed are accurate with the search filters|All search results match the search criteria |Pass| |
||Select a max year. Ensure the min year cannot exceed the max year|All values of min year that exceed the max year are disabled |Pass| |
||Select min year. Ensure the max year cannot be less than the max year|All values of the max year that are below the min year are disabled |Pass| |
||Select max price. Ensure the min price cannot exceed the max price|All values of min price which exceed the max price are disabled |Pass| |
||Select min price. Ensure the max price cannot be less than the max price|All values of max price which are below min price are disabled |Pass| |
||Click on the search button. Ensure the user is redirected to the listings page|The user is redirected to the listings page with accurate results |Pass| |
|Recent Listings|Open the Home page. Scroll down to recent listings. Ensure the most recent listings are showing by comparing the time added stamp|The most recent listings are displayed |Pass| |
||Open the Create Listing page and create a listing. Ensure it shows as first in the most recent listings section |The added listing is displayed as most recent |Pass| |
|Listing Card| Click on the listing card. Ensure it redirects to the correct single listing page |When clicked each card redirects to the correct single listing page |Pass| |
|| Click on the listing card button. Ensure it redirects to the correct single listing page |When clicked each card button redirects to the correct single listing page |Pass| |
|| Go to the Create Listings page and create a new listing. Ensure the details displayed on the card are accurate |The information displayed on the card is accurate |Pass| |
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|search form|||Pass|Tested on home page|
|listing card|||Pass|Tested on home page|
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Item details

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Back button|Open the single listing page. Click on the back button. Ensure it sends you back to the previous page|When clicked the button brings you back to the previous page.|Pass||
|back button|Open the single listing page and the listing to favourites. Click on the back button. Ensure it sends you back to the previous page|When clicked the button does not bring you back to the previous page due to the fact the page reloaded|Fail|This is a known bug.|
|Images section|Click on the main image. Ensure it opens using Lightbox. Ensure arrows appear to navigate through the images|When clicked the images open using lightbox. Arrows appear on the sides and allow you to navigate through the images|Pass||
|Listing details|Ensure all the car specs are accurate with the details used when creating the listing. Ensure all icons display as they should|All icons display as they should, and the information is accurate.|Pass||
|Save to favourites button|Click on the heart icon. Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|When clicked the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|Pass||
||As not authenticated user, Click on the heart icon. Ensure the page redirects to the login page|When clicked the page redirects to the login page|Pass||
||As an authenticated user, open your listing. Ensure the favourites button does not appear|When visiting your listing the favourites button does not appear|Pass||
|Seller Card|Click on the seller's image. Ensure the link leads to the user's account profile|When clicked redirects to the user's account profile|Pass||
|Email Seller form|Click on the Email Seller button. Ensure a modal pops up with a form to fill in|When clicked, the modal pops up with a form to fill in|Pass||
||Click on the Email Seller button. Ensure The listing title field is populated and read-only. |The listing title field is populated and read-only.|Pass||
||As an authenticated user, ensure the form is prefilled with the user's details|When clicked, a modal pops up with pre-filled form fields for existing details like name and email.|Pass||
||Fill all fields with correct data in the expected format. Click send a message. Ensure an email has been sent with the details entered using a test email address |Email was received with accurate details|Pass||
||Fill all fields with correct data but one. Click send a message. Ensure the form is not submitted and an appropriate message is displayed. Repeat for all fields. |Form did not submit, the appropriate message was displayed|Pass||
|Description|Scroll to the description section. Ensure the accurate description is displayed |The accurate description is displayed|Pass||

- Adding Item

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|To test car make/model dependancy first select model and ensure there are no drop down options. Then select car make. Ensure the car model field is populated with the correct options for each make|The car model dropdown has no options initially. The car model field is populated with the correct options for each make|Pass||
||Click on each drop down field to ensure correct options are displayed|Correct options are displayed|Pass||
||Fill all fields with correct data in the expected format. Click Submit. Ensure the listing was created by: 1. checking for flash message, 2. Go to Home page and find the card with the new listing |When submitted success flash message is presented. The new listing card appears on the home page's recent listings|Pass||
||Fill all fields with correct data but one. Click Submit. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||

- Editing Item

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|||Pass|Tested at create listing|
||Open edit listing page. Ensure the form is populated with the correct listing's details|The form is populated with the correct listing's details|Pass||


- Delete item

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Delete Listing|Click on the delete listing button. Ensure it deletes the listing and the user is redirected to the my listings page. |The user is redirected to the my listings page. By checking in the admin pannel can be confirmed the was deleted|Pass||

- Log In

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Sign In. Ensure Flash message appears and the user is redirected to the home page. To ensure the user is logged in: Open developer tools and navigate to application. On the side select cookies and check for sessionid being added. |When submitted success flash message is presented, the user is redirected to the home page. Sessionid is added to the cookies|Pass||
| | Fill in the form with incorrect details. Ensure the user is not logged in and flash message appears| Flash message appears in red letting the user know they have entered incorrect details. The user is not signed in| Pass| |
| | Click on the forgot password link. ensure it redirects to the reset password page.| The user is redirected to the reset password page| Pass| |
| | Click on the register here link. ensure it redirects to sign up page.| The user is redirected to the sign up page| Pass| |

- Sign Up

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Sign Up. Ensure Flash message appears and the user is redirected to the my profile page.|When submitted success flash message is presented, the user is redirected to the my profile page.|Pass||
||Fill all fields with correct data but one. Click Sign Up. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||
| | Click on the Already have an account? Log In link. ensure it redirects to the login page.| The user is redirected to the login page| Pass| |


- Sign Out

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Log out button|Click on the Log out button.To ensure the user is logged out: Open developer tools and navigate to application. On the side select cookies and check for sessionid being removed.The user should be redirected to the the home page. Ensure flash message is displayed |The user is redirected to the home page. Flash message is displayed. Sessionid is removed from cookies.|Pass||