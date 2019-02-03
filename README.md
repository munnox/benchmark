# Benchmarks

Simple set of performance benchmarks to test the speed of computers.

# Background

Many times I find myself working with different computer architectures
including pi's VM's docker containers. I find what id would like to have
is a simple benchmark system which can be easier accessed and run.

It should have the follow features:

* Low / Simple Dependencies
* Pragmatic
    Use tests and operaation which give the best idea of real world performance

Currently the chosen language is python version 3.7 since this is the latest and should be the most stable.
The trick is here to run simply and agnostic to the machine.

For a simple beginning all that is needed is to have python 3 installed and run:

`time python3 test.py`
