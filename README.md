# Pulse

[![Build Status](https://travis-ci.com/ctrl-alt-delete-3308/pulse.svg?branch=master)](https://travis-ci.com/ctrl-alt-delete-3308/pulse)

Providing unified keyword search across major social media platforms,
*Pulse* empowers users to understand the Internet's opinion. Built
on [Django](https://www.djangoproject.com/), continually deployed on
[Heroku](https://www.heroku.com).

## What Platforms are Supported?

We currently support search on the following social media platforms:

* Twitter
* Reddit
* YouTube

## Contributing

Have an issue, feature idea or code to add? Great! There are no
hard-spelled guidelines here. Just submit a pull request to the master
branch and we'll get the conversation going.

## Directory Structure

As Pulse was created within the Django framework, it follows typical Django formatting
styles. Pulse wide settings are located with the 'pulse_project' directory. Supplemental
apps for the project are located within the 'users' or 'pulse_search' directories. These
apps modify the overarching Pulse project. Within the 'users' directory files pertaining
to the creation, modification, or display of users including login support, account page
views, etc are located. Within the 'pulse_search' directory files pertaining to all other
functionality, including our search features, are located.

## License

This project is licensed under the MIT License. Please see the included
`LICENSE.md` file in this repository.
