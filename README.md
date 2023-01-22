# MentaL ChatboT

A mental health chatbot that uses GPT-3 API to provide consultation, diagnosis, and treatment options for mental health issues.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- OpenAI API key

### Installing

1. Clone the repository by running `git clone https://github.com/yourusername/MentaL-ChatboT.git`

2. Navigate to the root directory of the application and create a virtual environment by running `python -m venv venv`

3. Activate the virtual environment by running `source venv/bin/activate`

4. Install the required packages by running `pip install -r requirements.txt`

5. Add your OpenAI API key to the `.env` file

6. Run the application by running `flask run`

## Accessing the Frontend

1. Once the application is running, you can access the frontend by navigating to `http://localhost:5000/` in your browser

2. Make sure that your `index.html` file is located in the `templates` folder and that the path to the HTML file is correct in the Python code

3. Also, double check that the CSS and JS files are in the `static` folder and that the path to the files is correct in the HTML file

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Web framework used
- [OpenAI](https://openai.com/) - API used

## Authors

- **Dedan Okware** - *Initial work* - [SoftCysec](https://github.com/SoftCysec)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
