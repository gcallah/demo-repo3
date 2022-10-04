# demo-repo3

An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

We will write a API-driven adventure game where characters explore a world,
meet threats, find treasure, etc.

## Requirements

### Game endpoints:
- List all available games
- Get a description of a game
- Create a game
- Delete a game

### User endpoints:
- Signup
- Signin
- List all available users
- Get a description of a user
- Delete a user

### Character type endpoints:
- List all available character types
- Get a description of a character type

### In-game actions:
- List all active characters
- Describe a locale
- Allow character to move
- Allow character to act
- Allow character to talk to other characters in locale

## Design

Each of the main requirements will correspond to an API endpoint.

We will need to carefully consider a security system, and modify the design of
these endpoints to reflect our security policy.
