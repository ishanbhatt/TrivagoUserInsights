# Build user insights system for trivago
The Challenge
-------------
Three teams in trivago really want to know about a user in real time to add some personalization to their products. For now, there are two specific insights they are interested in:



for a particular user, what are the top-N amenities selected.
for a particular user, what are the top-K hotels clicked on the most for a particular user.


As a member of User Profiling team, you are tasked with designing and implementing a service to provide this information through an API.

# HOW TO RUN

1) Run locally
    1. Clone the repo
    2. Put selections.csv and clicks.csv into /tmp location
    3. pip install -r requirements.txt && python runserver.py OR
    4. pip install -r requirements.txt && ./gunicorn.sh
    
2) For docker lovers
    1. docker pull ishanbhatt/trivago_user:test
    2. docker run -d --name trivago -v /PATH/TO/selections.csv:/tmp/selections.csv -v /PATH/TO/clicks.csv:/tmp/clicks.csv -p 5300:5300 trivago_user:test
    
# HOW TO TEST
    
1) curl requests
    1. curl -X GET "http://localhost:5300/amenities?user_id=134043176577210003&limit=10"
    2. curl -X GET "http://localhost:5300/amenities?user_id=134043176577210003
    3. curl -X GET "http://localhost:5300/hotels?user_id=1637496642982613300&limit=10"
    4. curl -X GET "http://localhost:5300/hotels?user_id=1637496642982613300
    
2) httpie requests
    1. http :5300/amenities user_id==134043176577210003 limit==1
    2. http :5300/hotels user_id==1637496642982613300
    
3) Go to http://localhost:5300/ to use Swagger API

# Load Test Results

I used locust(included in requirements.txt) to load tests the api. And the results are stored in load_images folder.

Code for the same is in locust_load package. If you want to run it just do ./locust_runner.sh and open http://localhost:8089 and set up your load profle

