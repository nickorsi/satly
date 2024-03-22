<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/nickorsi/satly">
    <img src="static/satly_demo.gif" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Saltly</h3>

  <p align="center">
    An image light table/editor app for all your salty photos!
    <br />
    <a href="https://saltly.onrender.com">View Demo</a>
    ·
    <a href="https://github.com/nickorsi/satly/issues">Report Bug</a>
    ·
    <a href="https://github.com/nickorsi/satly/issues">Request Feature</a>
  </p>
</div>


![GitHub top language](https://img.shields.io/github/languages/top/nickorsi/satly)
![GitHub repo size](https://img.shields.io/github/repo-size/nickorsi/satly)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/nickorsi/satly)
![GitHub last commit](https://img.shields.io/github/last-commit/nickorsi/satly)


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Saltly is an app where users can upload images, view images, and edit the color tone of an image. There is no authentication/authorization handling in the app currently, so all users can see and edit all images.

This is a full-stack application written in Python using Flask as the web framework and Flask-SQLAlchemy as an Object Relational Mapper (ORM). This is a traditional HTML serving application that incorporates the use of AWS S3 cloud storage to save the image files and keep them seperate from the backend PostgreSQL database.

Deployed using Render to host the backend code and ElephantSQL to host the database.

Some tools and concepts covered during this project:
*Exposure to the application development life-cycle from project ideation to deployment
*Building a Minimal Viable Product (MVP) within a week
*Setting up and utilizing AWS S3 cloud storage
*Using Python library Pillow to handle image files
*Form validation and error handling with Flask-WTForms
*Rendering HTML dynamically with the use of Jinja
*Styling with Bootstrap and traditional CSS



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![HTML5][HTML5]][HTML5-url]
* [![CSS3][CSS3]][CSS3-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Flask][Flask]][Flask-url]
* [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url]
* [![Jinja][Jinja]][Jinja-url]
* [![WTForms][WTForms]][WTForms-url]
* [![AWS][AWS]][AWS-url]
* [![Render][Render]][Render-url]
* [![ElephantSQL][ElephantSQL]][ElephantSQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps. Note that you will need to connect your own AWS S3 bucket to allow the app to fully function.

1. Clone this repo at your desired directory.
  ```sh
  $ git clone https://github.com/nickorsi/satly.git
  ```
2. Within this new directory, create a virtual environment.
  ```sh
  $ python3 -m venv venv
  ```
3. Activate the venv.
  ```sh
  $ source venv/bin/activate
  ```
4. Install the requirements saved within the requirements.txt file.
  ```sh
  (venv) $ pip3 install -r requirements.txt
  ```
5. Run server.
  ```sh
  (venv) $ flask run
  ```
  Note: Mac users may need to run the flask server on port 5001 using the below command
    ```sh
    (venv) $ flask run -p 5001
    ```
6. Assign the AWS S3 tokens in a .env file, REMEMBER TO ADD THIS TO YOUR .gitignore FILE!
  ```python
    AWS_ACCESS_KEY_ID='Your AWS Access Key ID'
    AWS_SECRET_ACCESS_KEY='Your AWS Secrete Access Key'
    S3_BUCKET='Your S3 Bucket Name'
  ```

### Seeding Data

Seed the database with some sample images. This requires PostgreSQL to be installed.

1. Enter iPython in terminal (while in venv):
   ```sh
   (venv) $ ipython
   ```
2. Run seed file:
  ```python
  In [1]: run seedNO.sql
  ```
Note: This will create a DB called saltly and is assuming you don't have an active db called this.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add more color tone editing options for the images
- [ ] Add a "Revert" option to go back to the original image
- [ ] Add authentication/authorization so users can make photos public and only users can edit their images
- [ ] Find a better way to cache images and still have new image edits appear without hard refresh
  - Current work around is to make every image url unique, preventing caching but allowing edited photos to appear without hard refresh


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Nick Orsi - [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin Logo">](https://www.linkedin.com/in/nicholas-orsi-18ab8382/) - [www.nickorsi.com](https://www.nickorsi.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
This was built as part of the ![Rithm School](https://www.rithmschool.com/) curriculum in February 2024.

* [Matt Smida](https://github.com/mattsmida): Co Author
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Mardown Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: (https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[Python-url]: (https://www.python.org/)
[JavaScript]: (https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
[JavaScript-url]: (https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[HTML5]: (https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
[HTML5-url]: (https://developer.mozilla.org/en-US/docs/Web/HTML)
[CSS3]: (https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
[CSS3-url]: (https://developer.mozilla.org/en-US/docs/Web/CSS)
[PostgreSQL]: (https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
[PostgreSQL-url]: (https://www.postgresql.org/)
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Flask]: (https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
[Flask-url]: (https://flask.palletsprojects.com/en/3.0.x/)
[SQLAlchemy]: (https://img.shields.io/badge/SQLAlchemy-%23D63113?style=for-the-badge)
[SQLAlchemy-url]: (https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
[Jinja]: (https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
[Jinja-url]: (https://jinja.palletsprojects.com/en/3.1.x/)
[WTForms]: (https://img.shields.io/badge/WTForms-blue)
[WTForms-url]: (https://flask-wtf.readthedocs.io/en/1.2.x/)
[AWS]: (https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
[AWS-url]: (https://aws.amazon.com/free/?gclid=CjwKCAjwte-vBhBFEiwAQSv_xQ9cNbAh7bqze8OHPqAjkwd9WAcrT9ebcC_gjiMhb5iNz2KDvq9QARoCrkkQAvD_BwE&trk=fce796e8-4ceb-48e0-9767-89f7873fac3d&sc_channel=ps&ef_id=CjwKCAjwte-vBhBFEiwAQSv_xQ9cNbAh7bqze8OHPqAjkwd9WAcrT9ebcC_gjiMhb5iNz2KDvq9QARoCrkkQAvD_BwE:G:s&s_kwcid=AL!4422!3!592542020599!e!!g!!aws!1644045032!68366401852&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
[Render]: (https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
[Render-url]: (https://render.com/)
[ElephantSQL]: (https://img.shields.io/badge/ElephantSQL-%233F9BBF?style=for-the-badge)
[ElephantSQL-url]: (https://www.elephantsql.com/)
