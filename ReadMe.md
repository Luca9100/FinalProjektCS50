HouseParty App

Video Demo: https://youtu.be/B2WUcT-oAQo

Description:

The HouseParty App is a comprehensive web application designed to organize and manage guest registrations for a house party. This README provides an in-depth overview of the application's structure, functionality, and the rationale behind certain design decisions.

Project Files Overview:

style.css:
This CSS file defines the styling for the web pages in the application.
It sets a default font family and aligns text to the center.
The form elements and buttons are styled for consistency and visual appeal, with adjustments to width, padding, margins, and border settings.
The button element has additional hover effects to enhance user interaction.
guest.html:
A HTML file displaying the list of registered guests.
Utilizes Flask's template rendering to dynamically list guests from the database.
Each guest's details (name, surname, email, relationship status, picture, and favorite song) are displayed in a table format.
Includes a link to return to the home page.
index.html:
The home page of the application.
Provides links to register for the party and view registered guests.
This simple and user-friendly interface ensures easy navigation through the application.
register.html:
A registration form for party attendees.
Collects various details like name, surname, email, relationship status, picture, and favorite song.
The form uses POST method to submit data and includes multipart/form-data encoding type for image upload.
A link to return to the home page is also provided.
app.py:
The main Flask application script.
Connects to a SQLite database using SQLAlchemy for storing guest details.
Defines the Guest model with attributes corresponding to the registration form fields.
Routes for viewing guests, home page, and registration are defined, with the registration route handling both GET and POST requests for form submission.
Includes a function to check for allowed file extensions for image uploads and a utility to create the database.
The app is set to run in debug mode for easier development and testing.

Design Decisions and Challenges:

Flask Framework: Chosen for its simplicity and flexibility, Flask enables rapid development of web applications with the ability to scale up as needed.
SQLAlchemy: A powerful ORM that simplifies database interactions, making code more maintainable and robust.
Bootstrap and Custom CSS: While the project currently uses custom CSS for styling, integrating a framework like Bootstrap in the future could provide responsive design and more advanced features with minimal effort.
Image Uploads: Allowing image uploads adds a personal touch to the guest list but introduces complexities like file validation and storage. Using werkzeug.utils.secure_filename ensures safe file names.
Unique Email Validation Issue: One significant design challenge was handling cases where a user attempts to register with an email that is already in use. Initially, the system threw an error when a user tried to register with an email that already existed in the database. To improve user experience, this was modified to instead display a friendly message stating that the email is already taken. This required adjustments in both the backend logic in app.py and the frontend display to guide users appropriately without causing confusion or frustration.
Future Enhancements:

Implement user authentication to manage access.
Integrate a more robust frontend framework for a responsive design.
Add functionalities like guest list export, email notifications, and RSVP tracking.
Conclusion:
The HouseParty App serves as an efficient tool for organizing house parties, simplifying guest management and enhancing the overall planning experience. The project demonstrates fundamental web development concepts, including front-end design, backend processing, and database management. The unique email validation issue highlights the importance of considering user experience in application design, ensuring the app is not only functional but also user-friendly.

Adding a Video Presentation:

A video presentation will be added to this README to provide a comprehensive walkthrough of the application, showcasing its features and demonstrating its usage. Stay tuned for the video link to be updated.