/**
 * Function will display small notification message below newsletter section
 */
function newsMessage() {
    let email = document.getElementById('email');
    const newsSuccess = document.getElementById('newsletter-success');
    const newsFail = document.getElementById('newsletter-fail');

    // If mail value is empty, return the faulty message we set in our index page
    if (email.value === '') {
        newsFail.style.display = 'block'
    } else {
        setTimeout(() => {
            email.value = '';
        }, 2000);
        // if not return the success message we set in our index page
        newsSuccess.style.display = 'block';
    }
    // in any case, set time limit on both and vanish after 4 sec
    setTimeout(() => {
        newsFail.style.display = 'none';
        newsSuccess.style.display = 'none';
    }, 4000);
}


/**
 * Send emailJS function that will send an email to email address input by user
 */
function sendMail(contactForm) {
    emailjs.send('gmail', 'renegade', {
            'to_email': contactForm.email.value,
        })
        .then(
            function (response) {
                console.log('SUCCESS', response);
                newsMessage();
            },
            function (error) {
                console.log('FAILED', error);
            }
        );
    return false;
}