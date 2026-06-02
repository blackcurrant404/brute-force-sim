# BRUTE FORCE SIMULATOR

## V1 PLAN
- read common passwords from the txt-file
- import "verify" function from the "security-log-sim" project to perform password attempts
- iterate through the list until correct password is found, print the result to the terminal

## V2 PLAN
- switch from direct function calls to HTTP-based authentication requests
- send login attempts via POST requests to /login endpoint
- stop execution when correct password is found
- support for multiple usernames
- logging (found passwords linked to usernames)