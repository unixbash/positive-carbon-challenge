`positive-carbon-challenge` contains an application that meets the below requirements:

- Fetch the commodity price information for coffee once every 60 seconds
- Store this information in a time series DB
- Present it on a simple front end which shows real-time data on a graph and some updating stats such as
  - Rolling Average 
  - Max Price & Time
  - Min Price & Time
  - Changes over time

**Note**: With the free subscription plan data updates every 60 minutes

## Requirements
- `Docker`, `Docker-Compose`, `Python 3.9+`, `Pip` & `NPM`
- DB hosted on **localhost** [QuestDB](https://questdb.io/) database on port **8812**, with a table **qdb**, a user: **admin** and password: **quest**

## Architecture Diagram
![Architecture Diagram](images/architecture_diagram.jpg?raw=true "Architecture Diagram")

## Screenshots
![UI](images/ui.png?raw=true "React UI")

![DB](images/questdb.png?raw=true "QuestDB time-series DB")


## How to start

Clone this repo and run:

```sh
$ docker-compose build
$ docker-compose -f docker-compose.yml up
```

Open `http://localhost:3000/` to see make sure the service is running.


## Configuration

Most application configuration is present in the `./config_module.py` in the form of a Python class.
This allows the user to quickly change the application environment from dev to production (e.g. `DevelopmentConfig` -> `ProductionConfig`) 
Accomplished by updating which config is used in `app.py`:
```
cfg = import_string("config_module.DevelopmentConfig")()
```

## To be done in the future
1. Use load balancer such as **NGINX** to handle multiple requests in parallel
2. Deploy to a cloud service such as **AWS** (Elastic Beanstalk)
3. Build unit and integration **tests**
4. Integrate a **linter** for Python (Flask) or JS (React) through CI/CD pipelines
5. **Document API** using Swagger and Open API 3+
6. **API Versioning** can be done in many ways, but the most practical one for a project like this could be passing it in as query parameters (unless referencing the latest API version)
7. Use a **logging** library for debugging any issues in the future (Flask Logger)
8. Authentication, authorisation and application **security** required
9. Add a **PostgreSQL** database that allows for the user to be able to dynamically add and remove tracked commodities as well as currencies, units of measurement, etc/
10. Robust **error handling** to the added for the API 
11. **Database migration** functionality may be required down the line