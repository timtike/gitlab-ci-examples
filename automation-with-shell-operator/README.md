## automation

need to run unit test

- unit test need to generate report
- generate code coverage
- check coverage percent


need to run api test

- api test need to do some data preparation
- need to assert api response
- need to



### Testing

1.unit test

- use pytest
- added code coverage
- bash run_unit_test.sh

2.rest api test

- use pytest
- it's in automation-test/rest_api
- python run_rest_api.py
- generate report in automation-test/rest_api

3.performance test

- use python locust
- it's in automation-test/performance
- bash run_performance_test.sh
- generate csv for each time performance result, we need to analyze the csv by another script

4.check_config API

- can check the third party dependency services' status
- can easily check the online config

5.test feature branch

- run unit test and api test in feature branch first
- when feature passed, then can merge to master
