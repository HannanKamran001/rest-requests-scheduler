# Rest Requests Scheduler

Scheduler that lets you schedule REST requests for a given point in time in the future.

#### Requirements

- Django and Django Rest Framework
- PostgreSQL
- Redis

#### How To Use The Tool
Instructions are listed below that can be followed in order to use the deployed tool:

- You can find the deployed tool in the link mentioned in the email
- Login using the credentials provided in the email
- On Homescreen, click on the `Add` button in front of the `Api schedulers`
- Now, you can fill up the form and schedule a request by clicking on the `SAVE` button at the end of the page
- Sample GET and POST requests are listed below as a reference
- You can navigate to the `list` page of `Api schedulers` and see the list of all rest requests that has been scheduled for future as well as in the past. You can also apply filter on the list by selecting the respective status option from the filter box

#### Sample Requests

These are the sample GET and POST requests that you can use to test the tool

GET request:

```sh
Request url: https://www.google.com
Request type: GET
Request headers: {}
Request body: {}
Executable time: Date:2021-03-26, Time: 20:37:59
```

POST request:

```sh
Request url: https://ensyh99s9ku0n4o.m.pipedream.net
Request type: POST
Request headers: {}
Request body: {"url": "http://example.com/", "email": "user@example.com", "mock_data": "true", "ip_address": "92.188.61.181", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30"}
Executable time: Date:2021-03-26, Time: 20:37:59
```

#### Test Suite

I have added a couple of unit tests for the `scheduled_task` that is supposed to run at the scheduled time as unit tests are not for the testing of third party libraries. I believe the more efficient way to test out this tool is to have some monitoring system in place.