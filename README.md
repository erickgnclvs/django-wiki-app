# Django Wikipedia App

This project is a part of the Harvard CS50 Web Programming course. You can find the course and project details [here](https://cs50.harvard.edu/web/2020/projects/1/wiki/).

## Project Overview

The Django Wikipedia app aims to create a Wikipedia-like online encyclopedia using Django framework. It allows users to view and search for encyclopedia entries, which are stored in Markdown format.

## Getting Started

To get started with the project, follow these steps:

1. Download the project's source code and unzip it.
2. Open the directory in your preferred development environment.
3. Make sure you have Django installed. If not, you can install it using `pip install Django`.
4. In the project's root directory, run the Django development server with the command `python manage.py runserver`.
5. Access the application by visiting `http://localhost:8000` in your web browser.

## Features

The Django Wikipedia app includes the following features:

- Entry Page: Visiting `/wiki/TITLE` displays the content of the requested encyclopedia entry.
  - If the entry does not exist, an error page is shown.
- Index Page: The index page lists all encyclopedia entries, and clicking on an entry takes the user directly to that entry's page.
- Search: Users can search for encyclopedia entries by typing a query into the search box.
  - If an exact match is found, the user is redirected to the corresponding entry's page.
  - If no exact match is found, a search results page is displayed with entries containing the query as a substring.
- New Page: Clicking "Create New Page" allows users to create a new encyclopedia entry.
  - Users provide a title and Markdown content for the new entry.
  - If an entry with the same title already exists, an error message is shown.
- Edit Page: Each entry page includes a link to edit the content of that entry.
  - Clicking the link takes the user to a page with a textarea pre-populated with the existing Markdown content.
  - After making changes, the user can save the updated entry.
- Random Page: Clicking "Random Page" in the sidebar takes the user to a randomly selected encyclopedia entry.

## Project Structure

The project's structure consists of the following components:

- `wiki/urls.py`: Contains the URL configuration for the app.
- `wiki/views.py`: Defines the views for handling different functionalities.
- `wiki/templates/encyclopedia/`: Contains HTML templates for rendering the app's pages.
- `wiki/util.py`: Provides utility functions for working with encyclopedia entries.
- `wiki/entries/`: Directory for storing the Markdown files representing encyclopedia entries.

## Requirements

To run the Django Wikipedia app, make sure you have the following dependencies installed:

- Django (installable via `pip install Django`)
- python-markdown2 (installable via `pip install markdown2`)
