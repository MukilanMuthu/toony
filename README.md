# toony
Comic panel generator assignment project for Dashtoon.

## Steps involved
 - The barebones core files were created first to ensure the functionality of the app. This required using Flask and its other packages which are included in the README.md . 
 - Once the app was barely functional, the focus was shifted towards web page designing and structuring.
 - As soon as the app looked presentable, small features were added like adding a separate download button for individual images and the option to toggle whether the image must contain a speech bubble. This was implemented by simply adding the statement " with empty speech bubbles" to the input prompt at the backend. 
 - Finally, sensitive information like the Flask App secret key and the API authorization key was added in a `.env` file and was deployed to [pythonanywhere](https://toony.pythonanywhere.com/) successfully.

## Future expansions
 - Although this project was informative and fun, some areas can be improved.
 - Adding the option to compile all the images as a single comic layout.
 - Adding users and image storage for individual user accounts with a database.
 - Using TailwindCSS instead of Bootstrap for granular control over the design.
