# OC_project7
## Create GrandPy Bot, the grandpa robot
### Specifications
#### Features
  - Interactions in AJAX: question sent by pressing enter: the answer is displayed without reloading the page.
  - You will use the Google Maps API and the Media Wiki API.
  - Nothing is saved (reloaded page == lost history).
  - Several different answers can be made [optional].
  
#### User journey
The user opens his browser and enters the URL you provided him. He arrives in front of a page containing the following elements:

 - header: logo and catchphrase.
 - central area: empty area (which will be used to display the dialog) and form to send the request.
 
The user types in the form field and presses the enter key:

> "Hi GrandPy, do you know the address of OpenClassrooms?"

The message is displayed in the box above which displays all the messages exchanged. An icon turns to indicate that GrandPy is thinking.

Then a new message appears:

> "Of course my chick, here it is: 7 quoted Paradis, 75010 Paris."

Below, a Google Maps map also appears with a marker indicating the requested address.

GrandPy sends a new message:

> "But have I ever told you the story of this neighborhood that saw me in short pants?" The Cité Paradis is a public road located in the 10th district of Paris .This is a tee, a branch leads to 43 street of Paradis, the second at 57 street of Hauteville and the third dead end. [Learn more about](https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis)"

### Deliverables
  - Text document explaining the process
    - difficulties encountered / solutions found
    - Github link
    - site link deployed to use your project in production
    - pdf format not exceeding 2 A4 pages
    - written in English or Frenchs
  - Deposit source code on Github
### Constraints
  - Responsive and searchable interface on mobile
  - Test Driven Development
  - Code written entirely in English: functions, variables and comments
  - Using AJAX to send questions and view answers
  - Tests using mocks for APIs
  - Put in line with Heroku
