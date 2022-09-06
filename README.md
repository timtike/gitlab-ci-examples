# gitlab-ci-examples

will add some examples of gitlab-ci good practise


#### multiple_micro_services_together

```
many micro services in one repo,  include:Frontend,Backend-APIs, Lambda,Automation, Shared Code

update frontend code -> run frontend cicd -> and automation test

update shared code -> run all services cicd -> and automation test
```