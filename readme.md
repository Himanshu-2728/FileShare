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

### Provide the path 

After you start enter the method 0, you will be asked to enter the path of the file you want to share

    `Please enter the path: <yourPath>`

After providing the path, you will be provided with the hostname and a port which is to be entered on the receiving pc

### Provide Hostname and Port

    `Please enter the host name: `
    `Please enter the port: `

Enter the hostname and port displayed on the host pc
And then, you are good to go


# Thank You

Thank you for checking out this file sharing application! If you have any feedback or suggestions, please feel free to open an issue or submit a pull request. I hope you find this app useful!