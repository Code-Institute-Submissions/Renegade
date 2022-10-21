![Renegade Band](./README_Images/Page%20Images/banner/banner.png)

# WELCOME TO RENEGADE BAND PAGE 


[View the live project here.](https://renegade-band.herokuapp.com/)


This project was built for Code Institute's Portfolio 5 Assessment.  
It was built via Full-stack development program through Django Framework.  
More on Technologies used can be found below.

Site is a fictitious e-commerce band page for American Metal Band called **Renegade**.  
It allows users to access band's **merch** & **tour events** but also offers information on band members, about section and band songs, especially **new songs** *(singles)* which can be found on home page.

Project Idea came from my own interest to build a site a friend who actively plays in a band. It is a good opportunity to showcase the skills learned over the course.


![Mockup](./README_Images/Am%20I%20Responsive/layout.png)


# Table of Contents
- [Introduction](#welcome-to-renegade-band-page)
- [UX](#ux)
    - [User Stories](#user-stories)
        - [Site User](#site-user)
        - [Site Shopper](#site-shopper)
        - [Site Owner](#site-owner)
    - [Agile Methodology]()
    - [The Scope](#the-scope)
      - [Main Site Goals](#main-site-goals)
  - [Design](#design)
      - [Colours](#colours)
      - [Typography](#typography)
      - [Imagery](#imagery)
      - [Wireframes](#wireframes)
  - [Data Model](#data-model)
  - [Features](#features)
    - [Landing Page](#landing-page)
    - [Home Page - Images Carousel](#home-page---images-carousel)
    - [Home Page - Selected Products](#home-page---selected-products)
    - [Home Page - Image Banner](#home-page---image-banner)
    - [Home Page - Customers Reviews Carousel](#home-page---customers-reviews-carousel)
    - [Products Page](#products-page)
    - [Products Details](#products-details)
    - [Products Details - Features](#products-details---features)
    - [Products Details - Products on Sale](#products-details---products-on-sale)
    - [Products Shopping Bag](#products-shopping-bag)
    - [Products Shopping Bag - Products Coming Soon](#products-shopping-bag---products-coming-soon)
    - [Products Checkout](#products-checkout)
    - [Products Checkout - Success](#products-checkout---success)
    - [Products Management](#products-management)
    - [Profile Page](#profile-page)
      - [Service Reviews Page](#service-reviews-page)
      - [Add/Edit Service Review Page](#addedit-service-review-page)
    - [Signup Page](#signup-page)
    - [Signup Page - Verify Email](#signup-page---verify-email)
    - [Signup Page - Confirm Email](#signup-page---confirm-email)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Reset Password Page](#reset-password-page)
    - [Change Password Page](#change-password-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Page 404 - Page Not Found](#page-404---page-not-found)
  - [Messages and Interaction with Users](#messages-and-interaction-with-users)
    - [Sign up 1](#sign-up-1)
    - [Sign up 2](#sign-up-2)



# UX

-   ### User stories 

    -   #### Site User

        - As a Site User I can Easily register for an account so that I have a personal account and be able to view my profile.
        - As a Site User I can Easily login or logout so that I can access my personal account information.
        - As a Site User I can Easily recover my password in case I forget it so that I can recover acccess to my account.
        - As a Site User I can Receive an email confirmation after registering so that I can verify that my account registration was successful.        
        - As a Site User I can Have a personalized user profile so that I can view my personal order history and order confirmations and save my payment information.


    -   #### Site Shopper
        - As a Shopper I can View a list of products so that I can Select some to purchase.
        - As a Shopper I can View individual product details so that I can identify the price and product info.
        - As a Shopper I can Easily view the total of my basket so that I can see the current amount of my spending and avoid going overboard.
         - As a Shopper I can Sort the list of available products so that I can easily identify the best prices and sort from low to high.
        - As a Shopper I can Search for a product by name or description so that I can find a specific product I'd like to purchase.
        - As a Shopper I can Easily select the size and quantity of a product when purchasing it so that I can ensure I dont accidentally select the wrong product quantity or size.
        - As a Shopper I can View items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
        - As a Shopper I can Adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
        - As a Shopper I can Easily enter my payment information so that I can check out quickly and with no hassle.
        - As a Shopper I can Feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
        - As a Shopper I can View an order confirmation after checkout so that I can verify that I haven't made any mistakes.
        - As a Shopper I can Receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.


    -   #### Site Owner
        - As a Site Owner I can Add Tour Event so that Fans can see our current tour lineup with Country, City and Venue.
        - As a Site Owner I can Add Band Members so that I can add the new members of the band.
        - As a Site Owner I can Add a product so that I can add new items to my store.
        - As a Site Owner I can Edit/update a products so that I can change product prices, descriptions, images and other product criteria.
        - As a Site Owner I can Delete a product so that I can remove items that are no longer for sale.
        - As a Site Owner I can Edit/Delete band members so that I can keep the site updated in case of change in band members or edit their information.
        - As a Site Owner I can Edit and Delete Tour Event so that I can keep the tour lineup updated, change information and also delete tour events that are cancelled.
        - As a Site Owner I want expired Tour Event to automatically hide so that Fans or customers are not seeing old/expired tour events.
        - As a Site Owner I can Add Music Video Link so that Fans or Customers can easily see our videos and hear our music.
        - As a Site Owner I can Add New Songs so that they can also be rendered on our home page for fans and customers to check bands new songs.
        - As a Site Owner I can Edit/Delete music video links so that I can remove the songs or update the links.
        - As a Shopper I can see current number of items in my cart so that I can know exact amount of items I am ordering, including multitude of same items.


        As you can see below, all of the user stories are completed and they have all been tested as they were being implemented and through testing phase.  

        <details><summary>GITHUB USER STORIES   (🔻click to view 🔻)</summary>
            <img src="https://github.com/anluke/Renegade/blob/main/README_Images/User%20Stories/renegade_user_stories.png?raw=true">
        </details>
    
-  ### Agile Approach
    Site functionality and development all through this project was managed using GitHub Projects which can be found here [Renegade Band User Stories](https://github.com/users/anluke/projects/4).


-  ### The Scope

    -   #### Main Site Goals

        - To provide users with a good website experience with Band Merch & Tour Events.
        - To provide users with a visually pleasing website that is intuitive and easy to navigate.
        - To provide a website with a clear purpose.
        - To provide tools that allow users to search for products.
        - To provide users with an easy and safe way to buy their products.

-   #### Colours

![Colours](./README_Images/Colors/Colors%20charts.png)<br>

- Color Scheme is simple but still modern. As I'm a fan of **"Dark Mode on everything"**, I decided to go with Black background with white text. Hero Image touches on **Orange** and **Yellow** color with darker tones. **Cancel** button is in **warning-red** color while **Tour** buttons are all blue. Most of the continuity buttons are colored in **warning-color** as that gives a clear distinction of a button navigation to next step. Warning/Danger colors have nothing to with names, I just used them directly from bootstrap as they represented the best option for me.  
Checkout button inside the **toast** checkout popup is also labeled light blue.  
**EDIT** button is left white, **DELETE** is red and ***Update** is light blue.  
Black color was used for both header and footer with white text.




#### Typography

- Roboto font is used as the main font for the whole project.

#### Imagery

- Most of the images are **.PNG** and **.JPEG** format.  
Future improvement could be made by transforming them all into **.WEBP** file to improve the site performance but due to the length of this project I realised that a bit too late and left it as a future minor improvement.





-   #### Wireframes

    <details><summary>Desktop Wireframes (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_homepage_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_store_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_product_info_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_tour_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_about_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_member_info_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_videos_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_empty_cart_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_cart_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_checkout_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_order_confirmation_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_account_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_sign_up_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_log_in_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop/desktop_sign_out_wi.png?raw=true">   
    </details>

    - <details><summary>ADMIN Desktop Wireframes (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_home_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_store_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_product_info_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_add_product_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_tour_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_add_tour_event_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_edit_tour_event_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_about_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_add_member_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_edit_member_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_member_info_admin_wi.png?raw=true">
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/desktop-admin/desktop_videos_admin_wi.png?raw=true">
        </details> 

    <br>

    <details><summary>Tablet Wireframes (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_mobile_nav_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_home_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_store_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_tour_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_about_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_videos_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_account_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/tablet/tablet_checkout_wi.png?raw=true">
    </details>

    <br>

    <details><summary>Mobile Wireframes (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_home_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_store_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_product_info_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_tour_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_videos_wi.png?raw=true">
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Wireframes/mobile/mobile_checkout_wi.png?raw=true">
    </details>

    <br>

-   ## Data Model

    ![Data Model](./README_Images/Data%20Model/Renegade%20Data%20Model.png)<br>



# Features













<!-- # Features -->



-   ### Responsivity

The application is responsive on all device sizes, thanks to the [Bootstrapious](https://bootstrapious.com/) (bootstrap4)
 theme. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized.


-  #### Interactive elements
    * Nav links for Home, Menu, Blog, About, My bookings, Signup, Login and Logout link.
    * Form input fields on signup, logout, update and delete posts.
    * Buttons - including form buttons (signup, login, logout, table booking, edit and delete posts buttons and page navigation buttons (when there is too many blog posts)

-   ### Features to add in future   
    -   #### I would like to add a notification pop up that shows up on screen when user logs in/logs out.
    -   #### I would like to add a possibility of deleting comments but only if you are an owner.
    -   #### I would like to add more options to the Sign In form and have Registration only be active once the user has verified their account through email address.
<br>

# Sections

## Navigation
![Navbar](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/navbar.png?raw=true)

Above is a Navbar that's constisting of Logo at, **LOGIN** & **SIGNUP** in the middle and **Home, Blog, About, Create** on the right hand side.

This is how **navbar** looks like when user is signed in:

![Navbar-Logged](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/navbar-logged.png?raw=true)

And also below is the display of site navbar when reduced with 'hamburger' menu. Navbar is fully responsive.

![Hamb-Nav-Open](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/hamb-nav-open.png?raw=true)


## Hero

![Hero](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/hero.png?raw=true)

## Home

<details><summary>Home Page Full (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/home-page-large.png?raw=true">
</details>  

- Site home page has a guitar for the hero image. A small button to scroll down a bit and a introduction.  
- Just below the hero and intro section there is a small banner with 'famous' quote. And below that we have our Latest Blogs. This is where they will appear as they're created.


## Banner

![Banner](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/side-banner.png?raw=true)  
A banner with the famous quote from Mr. Jimmy Page. It separates the Latest blog section and our Hero section.


## Latest Blogs:

![Latest Blog](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/latest%20blogs.png?raw=true)  

Latest Blog section that covers our latest created blogs. As they are created the list moves from left to right and updates accordingly.


## Newsletter section:

![Newsletter](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/newsletter.png?raw=true)

Here we can see our Newsletter section. User can input their email address and they should receive an introductionary email from our Site.

<details><summary>Email Received Proof (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/email-received.png?raw=true">
</details>  


## Footer

![Footer](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/footer.png?raw=true)  

Site footer is at the bottom of the page, featuring Company Name, Email & Social Media section.



## Blog

<details><summary>Blog Post Section (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog.png?raw=true">
</details>

Blog is the site where you can see all the blog posts, and make use of the Navigation bar to switch between slides if there's more then 3-4 blogs posted.

It has a category section that displays all the current 'Active' categories that the users selected and also latest posts on the top.

It also features the number of views by users that are logged in along with the number of comments aside.

<details><summary>Blog Post As Author/Owner (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog-post-author.png?raw=true">
</details>  

<details><summary>Blog Post As Non Owner (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog-post-nonauthor.png?raw=true">
</details>  

This shows that admin created the first post and can delete that one but he can't delete or update Jonathan's post.

An Admin account is just used a normal user and if it would be necessary to delete that post it can be done through Admin portal. Deletion from the portal is something we can expand this project down the line.


## Sign up Section

![Sign Up](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/signup.png?raw=true)

We have our three input forms for signing in. User needs to follow the guide provided under the input forms in order to successfully create an account. After he creates an account it automatically logs him in.


## Log in Section

![Log In](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/login.png?raw=true)

Similar to our Sign up form. It only has two input forms. Password and Username.


## About


And below is our About page. It only holds text and it's purpose is to educate user on the purpose of the site along with some information for the future projects, etc.

<details><summary>About Section (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/about.png?raw=true">
</details>


## Admin Section

And of course we have our Admin section. We need to access this section by going into 'SITE URL' and then just add **/admin/** at the end.

![Admin Logged](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/admin-logged.png?raw=true)



<br>


# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries, Programs & Packages Used
1. [Django:](https://www.djangoproject.com/)
    - The Python-based Django framework was used to set up the structure, functionalities,  data model and database of the website.
1. [Bootstrapious Template:](https://bootstrapious.com/)
    - Derived from Bootstrap 4. Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    -    Used for Roboto Font.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - Originally used by my template. I am putting it on the list as it can be found within my files but I have not personally used it for this project.
1. [Email JS:](https://www.emailjs.com/)
    - Send an email to the user or visiting guest when using 'Newsletter' submit form on our home page.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)
    - To style the forms inside our Django app. Installed as a Django package.
1. [Tinymce4 Lite:](https://karansthr.gitlab.io/fosstack/how-to-set-up-tinymce-in-django-app/index.html)
    - WYSIWYG HTML Text Editor for 'Content' input form in our 'Create' tab.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Lucidchart:](https://www.lucidchart.com/) was used to create the data model of the project .
    <details><summary>Data Model</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/data-model/data-model.png?raw=true">
    </details>   
1. [PostgreSQL:](https://www.postgresql.org/)
    - Used PostgreSQL as per instructions of CI lessons in PP4.
1. [Cloudinary:](https://cloudinary.com/)
    - I used cloudinary for cloud-based storage and partly for linking of my website images.
1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.


# Testing

Testing was constistent throughout the deployment especially with Python.

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project. The issue is that this project is using a template and if loaded directly via link from Heroku or via GitPod link it will throw many errors as can be seen below:

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)    
    - <details><summary>HTML TEST</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/HTML-TEST-IMG/html.png?raw=true">
    </details>  

    HTML Summary tested without any Errors. There is a warning for my gallery. It is asking for heading elements but that whole section is filled with my pictures so I decided to leave it like that as it is not affecting functionality of my site and the TEST passed.  
<br>
    
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - <details><summary>CSS TEST</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/CSS-TEST-IMG/css.png?raw=true">
    </details>  
    CSS Summary tested without any errors. CSS did give warnings and when I looked into it they are just webkit tools. They are related to Google Fonts and vendor extension prefixes which will not affect the CSS performance. A lot of them have also been imported through Bootstrapious.

```
    -webkit-transition    |    -webkit-text-fill-color     |    -webkit-box-shadow     |    -webkit-text-decoration-skip-ink
```  

- [PEP8 Python Validation](http://pep8online.com/)  

    The only warnings Python gave was 'line-too-long' which I tried to fix in 'settings.py' file and other files and it did not look right and in some cases was breaking the page. I have decided to leave them in as they are not major issues:
    #### Accounts
    - <details><summary>urls.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Accounts/urls.png?raw=true">
    </details>  

    - <details><summary>views.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Accounts/views.png?raw=true">
    </details>  

    #### Guitarportal
    - <details><summary>settings.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Guitarportal/settings.png?raw=true">
    </details>  

    - <details><summary>urls.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Guitarportal/urls.png?raw=true">
    </details> 

    #### Marketing
    - <details><summary>admin.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Marketing/admin.png?raw=true">
    </details>  

    - <details><summary>models.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Marketing/models.png?raw=true">
    </details>  

    #### Posts
    - <details><summary>admin.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/admin.png?raw=true">
    </details>  

    - <details><summary>forms.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/forms.png?raw=true">
    </details>  

    - <details><summary>models.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/models.png?raw=true">
    </details>  

    - <details><summary>views.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/views.png?raw=true">
    </details>  
    <br>
- ### Lighthouse  
  
  Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop. Snippet bellow:

    - <details><summary>Lighthouse Desktop Test</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/lighthouse/lighthouse_desktop.png?raw=true">
    </details>  

    - <details><summary>Lighthouse Mobile Test</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/lighthouse/lighthouse_mobile.png?raw=true">
    </details>  

    Due to outdated jQuery version and other files that came with 'Bootstrapious' there are slight discrepancies, but it's functional and the test passed.

<br>

-   [JSHINT JavaScript Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

    As I didn't write much JS, I can only post emailJS that I added to submit a newsletter request. Snippet below:
    The guide was followed by Code Institite's lesson on Email JS.

    - <details><summary>JSHINT</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/JavaScript/jshint%20test.png?raw=true">
    </details>  


- ### Manual Testing

    * The Signup, Login and Logout all working correctly.

    * All the internal links are working and bring the user to the right page on the website.

    * All the external links are working and bring the user to the right social media page by 
    opening a new browser tab.
    
    * The Categories Page shows the genres and guitar brands. It picks up new categories from created posts.

    * The newsletter submit form takes the email and sends the newsletter welcome email to the user. The don't have to be logged in to use that service.

    * The pagination system is working. It adds another page after 3 posts or so.

    * The comment form has no issues and it submits a new comment once the form is completed by a
        registered user. 

    * CRUD is working. User is able to create, read, update and and delete their own posts. Superuser is able to delete posts in the backend 'admin' area regardless of the level.

    * When switching between accounts, the 'views' icon is incrementing as it should be.

    * When comment is posted it also incremenets an icon on the latest page section and the actual blog post.

<br>

- ### Unresolved Bugs


    - <details><summary>Chrome Console</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Console%20test/console.png?raw=true">
    </details>  

    Tested this feature few days ago just after successfully uploading to Heroku. I was told by one of the Tutors that it is most likely and issue between Heroku and Cloudinary Everything else seems to work so this is only error which does not seem to be affecting my site's functionality.


## Deployment

The site was deployed via Heroku.
1.  Log in to Heroku or create an account if required.
2.  Then, click the button labelled New from the dashboard in the top right corner and from the drop-down menu select Create New App.  You must enter a unique app name
3.  Next, select your region.
4.  Click on the Create App button.
5.  In your app go to Resources tab and add a Heroku Postgres database.
6.  The next page you will see is the project’s **Deploy Tab**. Click on the Settings Tab and scroll down to **Config Vars** and enter:
    *   **CLOUDINARY_URL** = your cloudinary key
    *   **DATABASE_URL** = the url of your heroku postgres database
    *   **SECRET_KEY** = a secret key for your app.
    *   **PORT = 8000**
    *   **DISABLE_COLLECTSTATIC = 1** during development and remove when deploying to production

7.  Scroll to the top of the page and now choose the Deploy tab.
8.  Select Github as the deployment method.
9.  Confirm you want to connect to GitHub.
10. Search for the repository name and click the connect button.
11. Scroll to the bottom of the deploy page and select preferred deployment type:
12. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
13. Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.

NB: Ensure in Django settings, **DEBUG is False**, create a **Procfile** and save database and cloudinary urls and secret key to **env.py.**

## Credits

*   Bootstrapious template downloaded from [Bootstrapios.com](https://bootstrapious.com/)
*   MS4 Project Preparation & Planning from [Code Institute's YouTube Channel](https://www.youtube.com/watch?v=qAseQckru9o)
*   Got a lot of help in understanding Models, Views from [TheNetNinja YouTube Channel](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
*   [Just Django](https://www.youtube.com/c/JustDjango)helped me out greatly with understanding my Models and also template tags. I based my layout on his template but removed some things I did not need and accomodated for my purpose.
*   HERO image from: [PRS Guitars](https://prsguitars.com/)
*   Banner cover image with Quote [Wallpapercave](https://wallpapercave.com/wp/KARQiCN.jpg)
*   Gallery Image 1: James Hetfield [faceoffrockshow](https://www.faceoffrockshow.com/post/james-hetfield)
*   Gallery Image 2: Mark Tremonti [musicradar.com](https://www.musicradar.com/news/mark-tremonti-my-top-5-tips-for-playing-live)
*   Gallery Image 2: Dan Donegan [nme.com](https://www.nme.com/wp-content/uploads/2022/07/Disturbed-Dan-Donegan-696x442.jpg)
*   Gallery Image 3: Adam Dutkiewicz [loudwire.com](https://loudwire.com/killswitch-engage-adam-d-pandemic-depression-worst-year-my-life/)
*   Blog Story 1 video [Mark Tremonti](https://www.youtube.com/watch?v=xG6NctwsOxs)
*   Blog Story 2: video [James Hetfield](https://www.youtube.com/watch?v=1Eq9RVKT9XQ)
*   Blog Story 3: video [Dimebag Darrell](https://www.youtube.com/watch?v=p40B6-p5u8w&feature=emb_title)


## Special Thanks:

- To all the Tutors, especially Scott and Ger. They helped me out when I was badly stuck.
- Also want to thank my Mentor for his support and guidance and the material he sent that helped me get the better idea for this project.


## Plans for implementation

- Project was hard. I wanted to do so much more but I couldn't risk it as I was quite late to start with already.  
There is definitely room for improvement but I wanted to get at least a working MVP with CRUD implementation that looks nice and can be implemented down the line.
- I have learned a lot during this PP4.