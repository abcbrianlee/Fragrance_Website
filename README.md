# Fragrance Website
The Fragrance Website is a platform created using Python, JavaScript, HTML, CSS, SQLite3, and Flask. It allows users to explore and discover different colognes and perfumes, register and log in to the website, leave reviews and ratings for products, explore different products with product similiarities, and add items to their cart.

# Technologies Used
* <b>Python<b><br>
* <b>JavaScript<b><br>
* <b>Flask<b><br>
* <b>HTML/CSS<b><br>
* <b>SQLite3<b><br>
  
# Project Description
  The Fragrance Website offers a secure user registration and login system, with password encryption to ensure data safety. All user information is stored in SQLite3 databases. The project includes the following key components:
- **User Management:** Users can create accounts, log in, and securely access their personalized profiles. Some features not available unless a user is logged in.

- **Product Catalog:** A wide range of colognes and perfumes are available in the product catalog. The data for these products is stored in a product table in the database.

- **Notes and Fragrance Composition:** The website provides information about the different fragrance notes found in the products. It includes a notes table and a product notes table that associate products with specific notes. A notes library is included to allow user's to browse products based on their notes preferences.

- **Reviews and Ratings:** Users can leave comments and ratings for products they have experienced. These reviews are stored in a review table, associated with the relevant product and user.

- **Detailed Product Pages:** Clicking on individual products leads users to dedicated pages with detailed information. Users can access the review section to read and write reviews if they are logged in. All user reviews are immediately reflected in the database.

- **Smelling Notes Exploration:** Users can explore products based on specific smelling notes. Clicking on a note takes users to a page dedicated to finding the best products containing that note.

  ## Getting Started
1. Clone the repository: `git clone https://github.com/your-username/fragrance-website.git`
2. Install the necessary dependencies:<br>

- blinker==1.6.2
- click==8.1.3
- Flask==2.3.2
- Flask-Login==0.6.2
- Flask-SQLAlchemy==3.0.3
- greenlet==2.0.2
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.2
- Pillow==9.5.0
- SQLAlchemy==2.0.15
- typing_extensions==4.5.0
- Werkzeug==2.3.4
3. Configure the database connection: Update the configuration file with your database credentials.
4. Run the application: `python main.py`
5. Access the website in your browser at `http://localhost:5000`
  
  ## Contributions
  Contributions to the Fragrance Website project are welcome! If you find any bugs, have feature requests, or would like to make improvements, please open an issue or submit a pull request.
