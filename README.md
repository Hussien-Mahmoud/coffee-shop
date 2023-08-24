# coffee-shop

## Django website made to replicate a real life website used for a real coffee shop.

this website is used to manage and display the menu of the coffee shop
and for the customers to be able to buy products from it eg. like coffee beans.
it also has a blog and a sections for displaying customer reviews.

 > **Warning**
 > the website isn't finished and some of it's features aren't available yet


## technologies used:
1. Django (models, admin site, DTL, etc...)
2. Whitenoise - for handling static files
3. google cloud storage - for handling media files
4. PostgreSQL - for Database
5. gunicorn - as the server
6. docker & docker compose


## How to install and run:
**This process has 2 ways**

### 1: With Docker and Docker Compose (Recommended):
> [!NOTE]
> This method will use PostgreSQL as the database and without support for media files in production
#### Prerequisites:
1. Internet connection
2. docker and docker compose installed [install form here](https://docs.docker.com/engine/install/).

#### Run the website:
1. clone this repository 
   > if you have git installed use this command `git clone https://github.com/Hussien-Mahmoud/coffee-shop`
2. Open Terminal/CMD.
3. Change directory (cd) to **path/to/coffee-shop**.
 
   If you cloned the repo with the previous command just type `cd coffee-shop`.

4. run the following command `docker compose up`.

   > if this doesn't work and gives you a permission error try `sudo docker compose up`
    
   This will take sometime at first because it is initializing but will launch the website instantly after the first time.
5. Open the browser and open the following url: `localhost`

### 2: Without Docker:
> [!NOTE]
> This method will use SQLite as the database and without support for media files in production
#### Prerequisites:
1. Internet connection
2. Python 3.11 installed
3. Pip3 installed
#### Set up:
1. clone this repository 
   > if you have git installed use this command `git clone https://github.com/Hussien-Mahmoud/coffee-shop`
   
2. Open Terminal/CMD.
3. Change directory (cd) to **path/to/coffee-shop**.
 
   If you cloned the repo with the previous command just type `cd coffee-shop`.

4. Run the following command to install required packages: `pip3 install -r ./requirements.txt`


#### Run the website:
1. Run the following command to start the server: `python manage.py runserver`
2. Open the browser and open the following url: `127.0.0.1:8000`