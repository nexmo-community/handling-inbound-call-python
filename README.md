# Handling inbound voice calls with Python

## ❗❗❗ **This repo is now deprecated. You can find up-to-date sample code for this and other tasks in the [Vonage Python Code Snippets repo](https://github.com/Vonage/vonage-python-code-snippets). Check the [Vonage Developer Blog](https://developer.vonage.com/en/blog) for more blog posts and tutorials. For more sample Vonage projects, check the [Vonage Community GitHub repo](https://github.com/Vonage-Community).**

This repo provides an example of how to handle inbound calls in Python.

Three scenarios are covered:

1. Play Text-to-speech message.
2. Connect inbound call to second phone (call forward).
3. Includes scenarios 1 and 2 plus also plays audio stream into call (also shows how to transfer control of call to new NCCO).

There is another version of the scenario 3 code also provided, which instead of
using a timer, uses a Flask route. Simply navigate to
`localhost:9000/agentfree` to simulate an agent becoming available.

## Prerequisites

To run the code you need:

1. Python 3 installed
2. A Nexmo application + Nexmo number
3. Ngrok (for testing locally, or other deployment method)

## Blog post

Full details are provided in this blog post:

[Handling an inbound call with Python](https://www.nexmo.com/blog/2019/03/28/handling-inbound-calls-with-python-dr/)

