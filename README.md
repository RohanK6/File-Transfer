# File-Transfer

Sharing files has never been easy for people who just want to share a file or two every so often. Using popular sites like MediaFire, where they have to register for an account, upload the file then send the link to the site where their friend has to then download from (often being redirected to various ad.fly links and such) are just a few of the issues people have. I decided to combat this by creating a File Transfer website that takes away all of the difficulties.

Sharing files with friends through the internet has never been so easy! Follow these easy steps to get started at: http://filetransferapp.pythonanywhere.com/transfer

## Navigating to the home page
![Main Screen](https://imgur.com/ngJwLOG.png)
This is the home page for the website. You can navigate through the site by using the navigation bar at the top or by clicking the buttons at the center of the page.

## Upload file
![Upload](https://imgur.com/P2Hrprj.png)
To start, you need to upload the file you want to send to the site. Fill out the required metadata here, including a file name, description, then choose the file that is located on your computer. This data will be saved in the database.

## Recieve code
![Code](https://imgur.com/qBxZPd0.png)
Once you upload the file, you'll receive a code on the screen. Simply click it to copy it to your clipboard. This code is unique only to the file that you uploaded, and you can send this code to your friend so they can download that specific file. For this example, the file uploaded was a .txt file containing lorem ipsum text. The code was 712F93CF5A2A434488865659B.

## Download file
![Download](https://imgur.com/io4d3w8.png)
Once the person recieves the code, all they have to do is navigate to the site and proceed to the download page. 

## Enter code
![Enter Code](https://imgur.com/5JP2gZ1.png)
Enter the code into the text box that is unique to the file (in this case, we will enter 712F93CF5A2A434488865659B, corresponding to the test file that was uploaded). Click the "submit" button to proceed.

## Final step
![Download File](https://imgur.com/vyMmJPB.png)
Finally, simply click the "download" button to start the download process to your computer. 

## Conclusion
The process is simple as that! In this current version, no account is needed or no redirects to ad.fly websites to prolong the download process. Completing this project, I learned various things that will be useful in future projects:
* File upload / storage using Django
* Django forms and storing metadata into the admin page
* Generating unique keys for each file, ensuring one key corresponds to exactly one file
* Django templates (used with the navigation bar across all of the pages)
* Rendering variables in Python onto the page for users to view (for the serial keys)
* Implementing JavaScript functions for copy buttons and custom buttons
