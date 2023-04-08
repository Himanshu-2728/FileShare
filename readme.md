# Description

This is a Python-based command-line file sharing application that allows users to share and receive files over a network using sockets. The application consists of a server and a client, with the server running on a specified IP address and port number, and the client sending requests to the server to either share or receive files.

## Getting Started

### Pre Requisitories 

* Python 3.5+
* Git

### Installation

1. Clone the project to your local machine 

    `git clone https://github.com/Himanshu-2728/FileShare.git `

2. Change the working directory

    `cd FileShare `

3. Install the required packages

    `pip install -r requirements.txt `

## Usage 

### Starting the server
To start the app, run the following command in your terminal

    `python server.py`

Enter the method, 0 for sharing and 1 for receiving a file 

For sharing:
    `Enter method: 0`

For receiving:
    `Enter method: 1`