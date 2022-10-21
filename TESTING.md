Testing was constistent throughout the deployment.

<br>

 ## HTML
The W3C Markup Validator was used to validate HTML of the project.
Other than minor warning with **text/javascript** being unneccessary in **HTML** files there was no errors.

[W3C URI Validator](https://validator.w3.org/#validate_by_uri)    
<details><summary>HTML TEST (🔻click to view 🔻)</summary>
<img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/HTML/w3_org_html_validator.png?raw=true">
</details><br>
HTML Summary tested without any Errors. There is a warning for my gallery. It is asking for heading elements but that whole section is filled with my pictures so I decided to leave it like that as it is not affecting functionality of my site and the TEST passed.  

<br>

 ## CSS
The W3C CSS Validator Services was used to validate CSS of the project.  
CSS Summary tested without any errors. CSS did give warnings and when I looked into it they are just webkit tools. They are related to Google Fonts, Bootstrap and vendor extension prefixes which are most likely coming from Bootstrap.

```
    -webkit-transition    |    -webkit-text-fill-color     |    -webkit-box-shadow     |    -webkit-text-decoration-skip-ink
```  
  
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
<details><summary>CSS TEST (🔻click to view 🔻)</summary>
<img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/CSS/wrc_css_validator.png?raw=true">
</details><br>

<br>

 ## Python
 - Normally I would have used [PEP8 Python Validator](http://pep8online.com/) but the site has been reported **currently down** by multiple sources.  
 - Post can be found on **#announcements** slack channel in **Code Institute** group.  
    The link to PEP8 Down can be found [here](https://code-institute-room.slack.com/archives/CPCT0MBKL/p1664380977854349).

- Due to the issues stated above, I followed the workaround posted by **Kevin Loughrey** and installed **pycodestyle**.  
    I tested **Python** code using that method. Screenshots can be found below.

- The only warnings Python gave was **'line-too-long'** which I tried to fix in **'settings.py'** but while I could resolve it **Pylint** would start throwing identation and or whitespace issues and while the code worked it wasn't a good trade off seeing how I was comfortable with my project at this stage and this could be ignored for the sake of not breaking the code.


    ### About
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/about/forms.py.png?raw=true">
        </details>      
    - <details><summary>forms.py_breaking_example (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/about/forms.py_breaking.png?raw=true">
        </details>
        This would happen every time I tried shorting the lines with no avail. In the end I left it as I did not want to accidently break a code.

    <br>

    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/about/models.py.png?raw=true">
        </details>   
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/about/urls.py.png?raw=true">
        </details>   
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/about/views.py.png?raw=true">
        </details>   

    <br>

    ### Accounts
    - <details><summary>admin.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/accounts/admin.py.png?raw=true">
        </details>
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/accounts/forms.py.png?raw=true">
        </details>
    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/accounts/models.py.png?raw=true">
        </details>
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/accounts/urls.py.png?raw=true">
        </details>
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/accounts/views.py.png?raw=true">
        </details>  

    <br>

    ### Cart
    - <details><summary>contexts.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/cart/contexts.py.png?raw=true">
    </details>  

    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/cart/urls.py.png?raw=true">
    </details>  

    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/cart/views.py.png?raw=true">
    </details>

    <br>

    ### Checkout
    - <details><summary>admin.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/admin.py.png?raw=true">
        </details>
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/forms.py.png?raw=true">
        </details>
    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/models.py.png?raw=true">
        </details>
    - <details><summary>signals.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/signals.py.png?raw=true">
        </details>
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/urls.py.png?raw=true">
        </details>
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/views.py.png?raw=true">
        </details>
    - <details><summary>webhook_handler.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/webhook_handler.py.png?raw=true">
        </details>
    - <details><summary>webhooks.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/checkout/webhooks.py.png?raw=true">
        </details>


    <br>



    ### Home
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/home/urls.py.png?raw=true">
        </details>
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/home/views.py.png?raw=true">
        </details>


    <br>



    ### Renegade
    - <details><summary>settings.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/renegade/settings.py.png?raw=true">
        </details>

    <br>


    ### Songs
    - <details><summary>admin.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/songs/admin.py.png?raw=true">
        </details>  
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/songs/forms.py.png?raw=true">
        </details>
    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/songs/models.py.png?raw=true">
        </details>  
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/songs/urls.py.png?raw=true">
        </details>
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/songs/views.py.png?raw=true">
        </details>


    <br>



    ### Store
    - <details><summary>admin.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/admin.py.png?raw=true">
        </details>
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/forms.py.png?raw=true">
        </details>  
    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/models.py.png?raw=true">
        </details>
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/urls.py.png?raw=true">
        </details>  
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/views.py.png?raw=true">
        </details>
    - <details><summary>widgets.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/store/widgets.py.png?raw=true">
        </details>


    <br>



    ### Tour
    - <details><summary>admin.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/tour/admin.py.png?raw=true">
        </details>
    - <details><summary>forms.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/tour/forms.py.png?raw=true">
        </details>  
    - <details><summary>models.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/tour/models.py.png?raw=true">
        </details>
    - <details><summary>urls.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/tour/urls.py.png?raw=true">
        </details>  
    - <details><summary>views.py (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/Python/tour/views.py.png?raw=true">
        </details>











## Lighthouse  
Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.
<details><summary>Lighthouse Desktop Test (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Lighthouse/desktop_lighthouse_report.png?raw=true">
    </details>        
<details><summary>Lighthouse Mobile Test (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Lighthouse/mobile_lighthouse.png?raw=true">
    </details><br>

**Accessibility**, **Best Practices** & **SEO** are ranging from **90%** to **100%**.

There is however a minor issue with **Performance**.  
Issue here lies with format of the images which I discussed briefly in [Imagery](#imagery) section of our **README** file.
It's affecting the Performance on Mobile screens and Desktop but not drastically. This could be improved by updating all images with **WEBP** format.  

When I tested the **Lighthouse** in **STORE** section of our page, performance was already better as the page does not have **VIDEO** links or large pictures such as our Hero Image.

<details><summary>Lighthouse STORE Example (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Lighthouse/desktop_lighthouse_store_report.png?raw=true">
    </details>  


<br>



## Console
Results came back clean and there are no underlying issues in the backend of the project.
<details><summary>Google Console Report (🔻click to view 🔻)</summary>
    <img src="">
    </details>  


 ## JavaScript
I did not have many JS files in this project but all of the JS files passed the test without issues.  
For JS testing I used [JSHINT JavaScript Validator](https://jshint.com/).

Results of the JS files can be seen below:
- <details><summary>account_country.js (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/JS/account_country.js.png?raw=true">
    </details>
- <details><summary>emailJS.js (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/JS/emailJS.js.png?raw=true">
    </details>  
- <details><summary>product_quantity_script (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/JS/product_quantity_script.png?raw=true">
    </details>
- <details><summary>stripe_elements.js (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/JS/stripe_elements.js.png?raw=true">
    </details>  
- <details><summary>stripe_elements.js (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Testing/JS/update_delete_cart_item_script.png?raw=true">
    </details>

<br>


 ## Heroku
 During Heroku build there were no issues and logs are as they should be.  
 Snippet below:
 - <details><summary>Heroku Build Log (🔻click to view 🔻)</summary>
    <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Heroku%20Images/heroku_build_log.png?raw=true">
    </details>

<br>



## Manual Testing

* The Signup, Login and Logout all working correctly. It shows interactive toast message to user on every session change.

* Member can also reset the password, get a password reset link and follow through the process without any issues.

* All the internal links are working and bring the user to the right page on the website.

* All the external links are working and bring the user to the right social media page by 
    opening a new browser tab.
    
* The Search bar shows the product with **keywords** searched. It also displays how many products are found under that name/word and the query of our search.

* The newsletter submit form takes the email and sends the newsletter welcome email to the user. User does not have to be logged in to use that service.

* Registered User or a Guest User are both able to Add Items to Basket, Update the Quantity, Remove as needed and View the products from Cart all the way to Checkpoint so CRUD is functional there too.

* Site Owner/SuperUser CRUD is working. Site Owner is able to create, read, update and and delete **Band Members**, **Tour Events**, **Store Products** and **Songs**.

* If I add a Tour event that is past today's date it will not show up on our Home page or Tour page.

* The Stripe Payment is working correctly and it's receiving user's payment. Webhooks are registering as successful.

* Streaming Platform links are opening the links as they should.

* CRUD is also fully functional in **mobile** and **tablet** view and there are no issues rendering files.

* All of the **EDIT** and **DELETE** links on our site work without a problem and superuser can use them.

* Ticking the box on **new song** will also render that video song on the home page. Leaving the box out will only render it on **VIDEO** page meaning that it is not a new song so functionality is as it should be.

* If I add a product without **IMG** it will automatically assign the **noimg** file to that product.

* If I input something in the site URL that does not exist, site renders a **404** page with a button to go back to **Home** page.
    - <details><summary>CUSTOM 404 PAGE (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Error%20images/404.png?raw=true">
        </details><br>

* If I manage to get a Server Error through testing a custom **500** page renders automatically with a button to go back to **Home** page.
    - <details><summary>CUSTOM 500 PAGE (🔻click to view 🔻)</summary>
        <img src="https://github.com/anluke/Renegade/blob/main/README_Images/Error%20images/500.png?raw=true">
        </details>

<br>

## Admin Page
- I have tested the Admin Panel repeatedly since the start of the project development.  
All the models are working without issues.
- I have created, deleted, and updated data in all models without errors. The models have the behaviour expected for what they were built for.
