# Ubuntu_Requests

# Ubuntu-Inspired Image Fetcher Assignment
# The Wisdom of Ubuntu: "I am because we are"

In the spirit of Ubuntu, which emphasizes community and sharing, your task is to create a program that connects to the global community of the internet, respectfully fetches shared resources, and organizes them for later appreciation.

# Your Task
Create a Python script that:
1. Prompts the user for a URL containing an image
2. Creates a directory called "Fetched_Images" if it doesn't exist
3. Downloads the image from the provided URL
4. Saves it to the Fetched_Images directory with an appropriate filename
5. Handles errors gracefully, respecting that not all connections succeed

# Requirements

1. Use the requests library to fetch the image
2. Check for HTTP errors and handle them appropriately
3. Create the directory if it doesn't exist using os.makedirs() with exist_ok=True
4. Extract the filename from the URL or generate one if not available
5. Save the image in binary mode

# Ubuntu Principles to Implement

1. Community: Your program should connect to the wider web community
2. Respect: Handle errors gracefully without crashing
3. Sharing: Organize the fetched images for later sharing
4. Practicality: Create a tool that serves a real need

Save Your Work in a GitHub Repo Called "Ubuntu_Requests" and Submit the URL for this Repository to Complete the Assignment. 