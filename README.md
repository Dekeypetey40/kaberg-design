# _Kaberg Design_

![Image of home page](documentation/kaberg-design-home-page.png)

---

# Introduction

Kaberg Design is a B2C e-commerce website designed to sell a variety of products to customers. Users can make an account, purchase products, contact the store, and subcribe to the newsletter. The link to the live website is [here](https://kaberg-design-16fc49f93f52.herokuapp.com/).

## Technologies used

- [Python](https://www.python.org/) was one of the main programming languages used to create this project.
- [VScode](https://code.visualstudio.com/) was the editor used to write my code.
- [Javascript](https://www.javascript.com/) was used to make the website more interactive.
- [HTML](https://en.wikipedia.org/wiki/HTML) and [CSS](https://en.wikipedia.org/wiki/CSS) was used to present content to the user on the front end.
- [ChatGPT](https://chat.openai.com/) was used to write product descriptions and the facebook page posts.

---

# Design

## Agile Planning

An agile approach was used to plan and make this project. I made use of GitHub's issues and projects to manage my progress in the project, as well as user stories and epics. A link to my kanban board can be found [here](https://github.com/users/Dekeypetey40/projects/4).
![Kanban board](documentation/kanban-board.png)

## User stories

| Title | Number | Definition | Completed? | Label |
|-------|--------|------------|------------|-------|
| USER STORY: Account registration | [#1](https://github.com/Dekeypetey40/kaberg-design/issues/1) | As a user, I want to register for an account, so that I can add my information and view my profile. | [x] | Must Have |
| USER STORY: Order confirmation | [#2](https://github.com/Dekeypetey40/kaberg-design/issues/2) | As a user, I want to receive a confirmation after I place my order and pay, so that I know the payment went through and the order was processed. | [ ] | Should Have |
| USER STORY: Password recovery  | [#3](https://github.com/Dekeypetey40/kaberg-design/issues/3) |As a user, I want to be able to recover my password, so that I can get access to my account if I forget my password. | [x] | Should Have |
| Simple login/logout process | [#4](https://github.com/Dekeypetey40/kaberg-design/issues/4) | As a user, I want a simple login and logout process, so that I can easily get access to my account. | [x] | Must Have |
| USER STORY: Navigation bar | [#5](https://github.com/Dekeypetey40/kaberg-design/issues/5) | As a user, I want to an easy to understand navbar, so that I can navigate the site. | [x] | Must Have |
| USER STORY: Social media links | [#6](https://github.com/Dekeypetey40/kaberg-design/issues/6) | As a user, I want clickable social media links, so that I can visit those pages. | [x] | Must Have |
| USER STORY: Add shopping cart items | [#7](https://github.com/Dekeypetey40/kaberg-design/issues/7) | As a user I want to add items to my shopping cart, so that I can purchase them. | [x] | Must Have |
| USER STORY: Review items to purchase in cart | [#8](https://github.com/Dekeypetey40/kaberg-design/issues/8) | As a user, I want to see the items I have added to my cart, so that I can review my purchase. | [x] | Must Have |
| USER STORY: Add quantity in shopping cart | [#9](https://github.com/Dekeypetey40/kaberg-design/issues/9) | As a user, I want to modify the amount of a certain item from my cart, so that I can add or remove items of a certain type from my cart. | [x] | Must Have |
| USER STORY: Secure payments  | [#10](https://github.com/Dekeypetey40/kaberg-design/issues/10) | As a user, I want to to know my card details are safe, so that I am comfortable making payments. | [x] | Must Have |
| USER STORY: Profile payment details | [#11](https://github.com/Dekeypetey40/kaberg-design/issues/11) | As a registered user, I want to save my payment details in my profile, so that I can easily make payments. | [x] | Should Have |
| USER STORY: View total cost | [#12](https://github.com/Dekeypetey40/kaberg-design/issues/12) |  As a user, I want to see the total of my puirchases, so that I can check the total before buying. | [x] | Must Have |
| USER STORY: Sort by category | [#13](https://github.com/Dekeypetey40/kaberg-design/issues/13) | As a user, I want to sort the products by category, so that I can view products from a specific category. | [x] | Must Have |
| USER STORY: Paginated list of products | [#14](https://github.com/Dekeypetey40/kaberg-design/issues/14) | As a user, I want to paginated pages of products, so that I do not have to scroll too much. | [] | Should Have |
| USER STORY: Search bar | [#15](https://github.com/Dekeypetey40/kaberg-design/issues/15) |As a user, I want to search for products with the search bar, so that I can find particular products I am looking for. | [x] | Should Have |
| USER STORY: Contact the store | [#16](https://github.com/Dekeypetey40/kaberg-design/issues/16) | As a user, I want to be able to contact the store, so that I can give them feedback. | [x] | Should Have |
| USER STORY: Updating store products | [#17](https://github.com/Dekeypetey40/kaberg-design/issues/17) | As an admin, I want to edit store products, so that I can change the products in the store. | [x] | Must Have |
| USER STORY: Add new product | [#18](https://github.com/Dekeypetey40/kaberg-design/issues/18) | As an admin, I want to add a product, so that I can have new products appear in my store. | [x] | Must Have |
| USER STORY: Delete a product | [#19](https://github.com/Dekeypetey40/kaberg-design/issues/19) | As an admin/store owner, I want to delete products, so that I can remove products no longer for sale. | [x] | Must Have |
| USER STORY: Search customer model | [#20](https://github.com/Dekeypetey40/kaberg-design/issues/20) | As an admin, I want to search through the customers, so that I can find them all. | [x] | Should Have |
| USER STORY: Contact us email | [#21](https://github.com/Dekeypetey40/kaberg-design/issues/21) | As a store owner, I want to to receive an email when a customer fills out the contact us form, so that can respond to the customer. | [ ] | Should Have |
| EPIC: Smooth purchases for user | [#22](https://github.com/Dekeypetey40/kaberg-design/issues/22) | Purchases should be easy and smooth giving feedback to the user. | [x] | Must Have |
| EPIC: Smooth user interface | [#23](https://github.com/Dekeypetey40/kaberg-design/issues/23) | The interface should be nice to look at and easy to navigate | [x] | Must Have |
| EPIC: Full CRUD functionality for the admin and CRUD elements for users | [#24](https://github.com/Dekeypetey40/kaberg-design/issues/24) | An admin should have full CRUD functionality and users should have it when applicable | [x] | Must Have |
| USER STORY: Account Creation Email Confirmation | [#25](https://github.com/Dekeypetey40/kaberg-design/issues/25) | As an admin, I want to send newly registered users emails to confirm their email, so that I can be sure I contact users at the correct email address. | [x] | Should Have |
| USER STORY: Newsletter subscription | [#26](https://github.com/Dekeypetey40/kaberg-design/issues/26) | As a user, I want to sign up for the store's newsletter, so that I am informed of new deals and information. | [x] | Must Have |
| USER STORY: Unsubscribe to the newsletter | [#27](https://github.com/Dekeypetey40/kaberg-design/issues/27) | As a user, I want to be able to unsubcribe from the newsletter, so that I stop getting emails I do not want. | [ ] | Should Have |
---

## Scope

The goal of this project was to make a functioning e-store. The baseline for this project was to have full CRUD (Create, Read, Update, and Delete) functionality for both admins and users where applicable. One can see this relfected in the user stories and their labels as must have, should have, and could have. At a bare minimum, the aim was to also have a functioning payment system and a subscription form for a newsletter.

## Colour

I decided to stick with a basic colour scheme. I used green to promote the value of recycled and antique products. Otherwise, the intention was to not distract from the product images and instead highlight them. The colour scheme and background image chosen for the homepage where inspired by the color scheme imaged below.

![Colour Scheme](documentation/color-scheme.png)

## Flow Chart and Wireframes

Wireframe of the homepage
![Homepage](documentation/wireframe-home.png)
Wireframe of a blog post
![Products](documentation/wireframe-products.png)
![Product](documentation/wireframe-product-detail.png)
![Contact](documentation/wireframe-contact.png)
![Profile](documentation/wireframe-profile.png)
![Review Purchase](documentation/wireframe-review-purchase.png)
![Checkout](documentation/wireframe-checkout.png)
![Signin](documentation/wireframe-signin.png)

## Database Models

![Database Models](documentation/db-models.png)

# Features

## Navbar

- The bootstrap template had a responsive navbar that turns into a burger menu on smaller screens.
- When you have not logged in it shows register and login options and a logout option when logged in.
- When logged in as an admin the product management link becomes available.
- The link that is active is bolded so the user knows where on the webpage they are.
![Navbar logged in](documentation/navbar-logged-in.png)
![Navbar logged out](documentation/navbar-logged-out.png)
![Navbar small screen](documentation/navbar-small-screen.png)
![Navbar extended menu](documentation/navbar-menu-extended.png)

## Homepage

- The homepage is simple and paginated.
- It shows three blog posts at a time and immediately lets the user know what the purpose of the site is.
- The blue tag and read more buttons invite the reader to click them.
  - The read more button lets you read the whole blog post.
  - The tag buttons filters blog posts by tag.
- You can see how many likes each blog post has.
![Image of welcome screen](documentation/ttrpg-home-page.png)

## Reading a blog post

- Here you can see what a blog post looks like when you click read more.
- At the bottom, you can leave a comment, like the post, and read others' comments.
![Blog post](documentation/whole-post-title.png)
![Blog post text](documentation/whole-post-text.png)

## Tags

- You can see tags on each blog post, which give the user additional information as to what the post is about.
- Users can click on the tags and get a filtered list of blog posts containing that tag.
![Tags](documentation/tag-filter.png)

## Polls

- Here you can look at the list of polls that you can vote on.
- One can only vote once on each poll.
- Once you vote you get to see a piechart with the results of the poll.
![List of polls](documentation/list-of-polls.png)
![Poll Results](documentation/poll-voted.png)
![Multiple Vote Attempts](documentation/poll-voted-again.png)

## Account creation and logging in and out

- There are messages letting the user know if they have successfully signed in or out.
- If a user wants to logout the site asks them if they are sure. 
- Username and password fields are required and prompt the user if they input invalid data. 
![Invalid Username](documentation/invalid-username.png)
![Password Required](documentation/password-required.png)
![Login](documentation/login-form.png)
![List of polls](documentation/logout-prompt.png)
![List of polls](documentation/navbar-logged-in.png)
![List of polls](documentation/navbar-logged-out.png)

## Comment CRUD Functionality for Users

- Comments must be approved by an admin. 
- Users have CRUD functionality on the front end.
- If you are the user who made the comment the Edit and Delete buttons appear allowing you to modify the comment.
- If you are not the user who made the comment and try to access the edit or delete urls you will be prevented from updating that comment.

![comment approval](documentation/comment-awaiting-approval.png)
![comment](documentation/crud-comments-user.png)
![comment edit](documentation/edit-comment.png)
![comment](documentation/edited-comment.png)
![comment](documentation/confirm-delete.png)
![comment](documentation/defensive-programming.png)

---

# Future Features

- Allowing users to make blog posts.
- An about page.
- Comment likes
- Discussions on polls

---

# Testing

All testing and validation information can be found [here](TESTING.md).
---

# Deployment

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Select your region.
5. Click Create App .
6. Navigate to the settings tab and then to Config Vars.
7. Click Reveal Config Vars and add PORT, ALLOWED_HOSTS, SECRET_KEY, CLOUDINARY_URL and DATABASE_URL. Temporarily set COLLECTSTATIC to 1.
8. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes.
9. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10. Scroll to the top of the page and choose the Deploy tab.
11. Select Github as the deployment method.
12. Confirm you want to connect to GitHub.
13. Search for the repository name and click the connect button.
14. Scroll to the bottom of the deploy page and select the preferred deployment type.
15. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
16. Turn DEBUG mode to false in settings.py before final deployment.

## Database

- The app used ElephantSQL as a free cloud database that uses postgresql.
- One simply makes an account with Elephant SQL, makes a new database and copies the url over to env.py.

---

# Credits

## Python Libraries

- Cloudinary
  - Storage for static files
- AllAuth
  - This librared allowed for a seamless integration for user accounts and their validation on the site.
- crispy-bootstrap5 and crispy-forms
  - This allowed for easy to use forms that are compatible with bootstrap 5 templates
- Django
  - This framework made it fast and relatively easy to make a full-stack website.
- Django-taggit
  - This library allowed for easy implementation of tags for my blog posts. Furthermore, it allows users to filter posts by their tag.
- Bootstrap 5
  - A great css framework to easily style web pages. There is lots of free templates available and they are easy to modify to my needs.
- Django-heroku
  - This library fixed a bug I had where my custom css would not work properly on Heroku.

## Content

- A huge thank you to my mentor Aleksei Konovalov for all of his help throughout this process.
- The method to paginate something compatible with Bootstrap 5 and the current Django was from [ourcodeword](https://ourcodeworld.com/articles/read/1757/how-to-implement-a-paginator-in-a-django-class-based-listview-compatible-with-bootstrap-5)
- My knowledge on how to use django-taggit was gained through the [BugBytes](https://www.youtube.com/watch?v=213swbH8j_o&ab_channel=BugBytes) Youtube channel.
- Flaticon and hero image were taken from [Freepik](https://www.freepik.com/)
- My login/logout form templates were taken from dvrrajashekhar on [freefrontend](https://freefrontend.com/bootstrap-login-forms/#gsc.tab=0)
- Stackoverflow was of huge help at multiple points during the project.
- [Starbootstrap](https://startbootstrap.com/theme/clean-blog) was very helpful in styling my website. I used a couple templates from that website and adapted them to suit my site.
- Code Institue's I think therefore I blog project inspired my own blog website, which I customized to suit my needs.

---

Credits
Pexels
Freepik

https://www.facebook.com/profile.php?id=61552848392818