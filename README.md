# log-filter
Python access log filter 


## Usage:
 `$ cat access.log | ./log_filter.py --ip x.x.x.x`  
 `$ cat access.log | ./log_filter.py --ip x.x.x.x/x`
  
    
## Tests
```
➜  git:(master) python3 -m pytest -v
============================================================================================================ test session starts =============================================================================================================
platform darwin -- Python 3.7.0, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/boban/jobs/log-filter, inifile:
collected 6 items

tests/main_test.py::test_ip_validation PASSED                                                                                                                                                                                          [ 16%]
tests/main_test.py::TestFilter::test_filtering_1 PASSED                                                                                                                                                                                [ 33%]
tests/main_test.py::TestFilter::test_filtering_2 PASSED                                                                                                                                                                                [ 50%]
tests/main_test.py::TestFilter::test_filtering_3 PASSED                                                                                                                                                                                [ 66%]
tests/main_test.py::TestFilter::test_filtering_4 PASSED                                                                                                                                                                                [ 83%]
tests/main_test.py::TestFilter::test_filtering_5 PASSED                                                                                                                                                                                [100%]

========================================================================================================== 6 passed in 0.05 seconds ==========================================================================================================
```
