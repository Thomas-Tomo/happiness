# **HAPPY HACKS - Introduction**

## ***Are you feeling in need of some happiness?***

> "*Even a happy life cannot be without a measure of darkness, and the word ‘happy’ would lose its meaning if it were not balanced by sadness. It is far better to take things as they come along with patience and equanimity*".
> 
> Carl Jung

So why not welcome youself to our *World Happiness Day Hackathon project*, also know as **Happy Hacks**? - a rejoiceful place, full of fun emojis and happy ideas for the world!

HAPPY HACKS is a place where users can receive inspirational '**Happy Hacks**', that they can use to motivate and guide themselves towards happiness, with advice from others. The home page invites users to click a button to receive a random 'hack', generated by other users. Users can create their own hacks by completing a form and attach an emoji to the post, sharing their own tips for the benefit of others. The text and associated emojis assist users in being able to filter posts for themed suggestions that are relevant to them.

View live website here: [Happy Hacks](https://happiness-generator-c0a5ad8756d8.herokuapp.com/).

![Am I Responsive](/static/docs/responsive.jpg)

<hr>

## **TABLE OF CONTENTS**

- [**Team Goal**](#happy-hackers-team-goal)
- [**Design**](#design)
   * [Colours](#colours)
   * [Typography](#typography)
   * [Wireframes](#wireframes)
   * [Database Schema](#database-schema)
- [**Features**](#features)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [Add Hack Page](#add-hack-page)
  * [Hacks Page](#hacks-page)
  * [Team Page](#team-page)
  * [CRUD Functionality](#crud-functionality)
- [**Testing**](#testing)
- [**Technologies Used**](#technology-used)
- [**The Team**](#the-team)

<hr>

## **Happy Hackers Team Goal**

- To create a site around the theme of 'happiness'
- To allow users to share personal experience about how they keep happy
- To provide users with suggestions of how to keep happy
- To incorporate css frameworks, such as bootstrap
- To use images, colours, emoticons and sounds to create a happy feel
- To build an interactive site using DJANGO with CRUD functionality
- To provide all team members with an opportunity to contribute

<hr>

## **DESIGN**

### **Colours**
- Research indicated that the happiest colour was yellow, with oranges also featuring.
- We selected a palette of complimentary colours with a happy theme.
- Colours were selected using the coolors color palette generator.
- An image incorporating yellow flowers was used as the background<br><br>

![Coolors Palette](/static/docs/palette.png)

<hr>

### **Typography**
- The fonts used throughout the site were selected from Google Fonts.
- Fonts were selected for their simple and readable design to avoid distracting from the content.
- Roboto Slab and Quicksand were selected.
- Later, Lilita One, was selected for the home page title for impact.
- All fonts were sourced through [Google fonts](https://fonts.google.com/).

![Fonts](/static/docs/fonts.png)
![Title Font](/static/docs/lilitaonefont.jpg)

<hr>

### **Media**
- [Balsamiq](https://balsamiq.com/) was used for the design of wireframes.
- [Fontawesome](https://fontawesome.com/) was used for the icons on various buttons.
- [DrawSQL](https://drawsql.app/) was used to sketch out the database models at an early stage.

<hr>

### **Wireframes**
Wireframes for different views are linked here:

![Mobile Wireframe](/static/docs/mob-wireframe.jpg)
![Mobile Wireframe](/static/docs/mob-wireframe-2.jpg)

![Desktop Wireframe](/static/docs/desktop-wireframe.jpg)
![Desktop Wireframe](/static/docs/desktop-wireframe-2.jpg)

<hr>

### **Database Schema**

- The database scheme was completed an an early stage, but later ammended to include emoji's

![Database Schema](/static/docs/dataschema1.jpg)

<hr>

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**
- The navigation bar is located at the top of each page on the site.
- The menu contains links for the 'Home Page' (which is also linked via the Brand Logo), the 'Add Hack', 'Hacks', 'Team' page links, along with 'Login' and 'Register' links. 
- Once the user is logged in the menu the 'Register' link is replaced with the 'Logout' page link.
- The navbar is fully responsive and collapses into a burger menu for mobile devices.

![Desktop Nav](/static/docs/navbar.jpg)

#### **Mobile Navigation**
- Presented as a burger menu for design responsiveness.
- Once clicked a dropdown menu appears including all the page links as above.

![Mobile Nav](/static/docs/nav-mob.jpg)

![Mobile Nav Expanded](/static/docs/nav-mob-expanded.jpg)

<hr>

### **Footer**
- Located at the bottom of the page the footer loads text with todays date and a random happy thought.

![Footer](/static/docs/footer.jpg)

<hr>

### **Home Page**
- Upon landing on the homepage the user is presented with the title 'Happy Hacks Generator'.
- Below the title, a message instructs the user to press the button to 'generate happiness'.
- When the button is pressed, a random post (hack) is displayed to the user.
- A button at the left, illustrated with a music note, will play a happy song.
- A button at the right, illustrated with a '+' sign, will take the user to the 'Add Hack' page.

![Home Page](/static/docs/home.jpg)

![Home Page Hack](/static/docs/home-hack.jpg)

<hr>

### **Add Hack Page**
- The Add Event page is essentially a form to complete.
- If the user is not logged in, they will be redirected to login.
- The user can type their 'happy hack' and pick an emoji to illustrate the hack.
- A sound will be played when the user successfully submits a post.

![Add Event](/static/docs/add-hack.jpg)

![Add Emoji](/static/docs/add-emoji.jpg)

<hr>

### **Hacks Page**
- The Hacks page displays all the hacks in the order they were last created.
- User can type in the search box or select an emoji to filter posts so they can find suggestions that interest them.

![Hacks Page](/static/docs/hacks.jpg)

<hr>

### **Team Page**
- The team page displays cards for each member.
- Team member main roles in the project are provided.
- Each member has a space to record their own 'Happy Hack'.
- Links are provided for team members' Github and LinkedIn profiles.

![Team Page](/static/docs/team.jpg)

<hr>

### **CRUD Functionality**
- The edit and delete hack page can be accessed via the Hacks page.
- Hacks which the logged in user has created show a button which reveals an 'edit' or 'delete' link.

![CRUD Links](/static/docs/crud.jpg)

<hr>

## **TESTING**

- Testing and results can be found [here](TESTING.md)
- Manual tests were carried out throughout the process.
- Responsiveness has been checked and adjusted in Chrome Dev Tools and the site has been viewed on mobiles and an mac without issues.

<hr>

## **Technologies Used**
   * DJANGO
   * HTML
   * CSS
   * Bootstrap

<hr>

## **The Team**

- The team worked incredibly well and managed to overcome the different time demands, supported junior member with conflict issues and got stuck into the code.
- All members were encouraged to get involved in some way and gain experience in Hackathons and agile practices.
- Regular meetings were held on slack, often to assist others in overcoming problems.
