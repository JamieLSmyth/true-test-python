# True Test for Python
This is an example project designed to show the power of combining different automated testing techniques to create the most stable possible projects.  The idea behind this project was to give a basic framework for using all of the following techniques:

* Test Driven Development - Test first, implemenation later (Not really shown here, but the ideas hold true)
* Acceptance Criteria/Behavior Driven Development - Given/When/Then Structure
* Properties Based Testing - Random value generation for large acceptable sample space
* Mutation Testing - Test that your tests are actually validating the code

This is a Python implementation of the Java based [True Test](https://github.com/JamieLSmyth/true-test) project.

The Application is written in Python and utilizes the [Nimoy](https://github.com/browncoat-ninjas/nimoy) framework which is based on the [Spock](http://spockframework.org) framework, the [Behave](https://behave.readthedocs.io/en/stable/) framework, [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) for property based testing and [MutMut](https://mutmut.readthedocs.io/en/latest/) for mutation testing.

## Running the unit tests (nimoy)
```shell
nimoy --power-assertions true
```

To get coverage results with nimoy execut
```shell
coverage run -m nimoy.main
```

## Running the functional test (behave)
```shell
behave
```

To get coverage results with behave execut
```shell
coverage run -m behave
```

## Running the mutation tests 
```shell
mutmut run
```

This will run validate the nimoy tests as mutation testing is most valuable for unit testing.  If you would like to use mutation testing to validate the functional tests (not recommend in the real world) you can use
```shell
mutmut run --runner="python -m behave"
```

mutmut aggressively caches results for performance reasons so if you want to run all the mutations again you need to remove the cache
```shell
rm .mutmut
```
