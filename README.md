# reqres-test
Test suite for testing Req|Res. This repo serves as a demo of how to test an API.

# Rational of approach
The approach taken was to spin up an automation framework that would be very quick an easy to get off the ground.

Utilizing pytest gives us ease of execution/reporting/coverage and since it is the predominant testing framework for python,
the learning curve should be fairly low for python developers. Also, the use of fixtures in pytest allow us to easily perform necessary
setup and teardowns.

[Schematics](https://schematics.readthedocs.io/en/latest/) is also being used in this repository. Schematics provides the ability to validate an
API's response by defining the model for the response (and objects within) and automatically validating the response
against the models. This allows validation of field existence and typing without having to explicitly call an assert.

This approach was what I chose to be able to code the most in the shortest amount of time. Based on the needs of the teams/organization, this may or may not be an appropriate approach.
Another approach I would use is [Behave](https://behave.readthedocs.io/en/stable/). Behave provides Gherkin syntax which would make it easier for non-devs to write new test cases and perhaps
even be able to automate them if the underlying methods are written to do so.

# Approach
The initial work done in this approach was to define the response models for the endpoints in the API. Since the tests are for an API, this was a necessary place to start.

Next, an `API` class was created that contain methods for interacting with the actual API. This provides wrappers around each of the API endpoints which will contain most of the
information needed to submit the request and receive the response.

After defining the models and API methods, the actual tests were created. An analysis of each endpoint was performed and test scenarios were determined.
Types of scenarios identified for coverage include:
- Status codes
- Validation of fields and types (provided by schematics)
- Edge testing of parameters and data
- Validation of various error messages
  - Entities not found
  - Invalid query arguments
  - Invalid request data
- End-to-End tests that utilize mulitple API calls to complete a scenario (POST/PUT/GET/DELETE entity)

Tests were then created starting with some of the simpler endpoints (GETS). Beginning with simpler tests gives the ability to quickly
adapt and change if there are issues that arise with the current approach.

**Note**: As this is just a coding exercise, all models/tests were not covered. There is `TODO` notation to indicate other tests that should be created.

# Pros and Cons of Approach
## Pros
- Develpoer friendly
- Easy ramp up for python developers
- Schematics provide built in structure/type validation for responses
- Pytest provides multiple features to enhance testing - parametrization, fixtures, etc.
- Very easy to extend

## Cons
- Not as simple for non-devs to understand
- Tests are not in an "easy to read" format
- Requires development experience in order to create new tests
- Making the framework more readable for non-devs would require some more work

# Repository Breakdown
The repository is broken up into mulitple folders for ease of navigation:
- `api` contains all of the method used to interact with the api as well as performing the conversion of the responses to the models.
- `models` contains all of the schematic models uses for the responses.
- `tests` contains all of the tests to be executed against the api.

The respository also contains linting (`flake8`) and formatting (`black`) which will be automatically executed on commit using `pre-commit`.

A Makefile is also provided for easier execution.

# Setup and Execution
The following can be run on the command line to set up the framework and execute the tests:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests -p no:warnings
```

Alternatively the setup and tests can be run from a Makefile using the following commands:
- `make setup` - This will create your virtualenv and install necessary requirements.
- `make test-all` - This will execute all tests within the `tests` directory