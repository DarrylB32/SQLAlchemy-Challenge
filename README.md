# SQLAlchemy-Climate_and_Weather_Analysis
This project utilizes Python and SQLAlchemy to do basic climate analysis of Honolulu, Hawaii. After the analysis, a Flask API app was created to explore database. As such, the project can be broken up into two main parts: the Climate Analysis and the Climate App.

### Climate Analysis

Precipitation Analysis
* Designed a query to retrieve the last 12 months of precipitation data.
* Selected only the `date` and `prcp` values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by `date`.
* Plotted the results using the DataFrame `plot` method.
![precipitation](ReadMe_Resources/precipitation.png)
* Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations.
* Listed the stations and observation counts in descending order.
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filtered by the station with the highest number of observations.
* Plotted the results as a histogram with `bins=12`.
![station-histogram](ReadMe_Resources/station-histogram.png)

### Climate App
After completion of initial climate analysis, I designed a Flask API based on the queries that were just developed.
### Routes
*  `/`
	* Home page.
	* Lists all routes that are available.
*  `/api/v1.0/precipitation`
	* Converts the query results to a dictionary using `date` as the key and `prcp` as the value.
	* Returns the JSON representation of the dictionary.
*  `/api/v1.0/stations`
	* Returns a JSON list of stations from the dataset.
*  `/api/v1.0/tobs`
	* Queries the dates and temperature observations of the most active station for the last year of data.
	* Returns a JSON list of temperature observations (TOBS) for the previous year.
*  `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
	* Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
	* When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
	* When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

### Tech Stack
* Python
* Jupyter Notebook

### User Instructions
 * Clone the repository: git clone https://github.com/DarrylB32/SQLAlchemy-Climate_and_Weather_Analysis 
 * Using terminal, navigate to the folder that has the **Climate_App.py** file and input:
	* python Climate_App.py
 * Copy and paste the URL link into your browser
### Additional Notes
 * The earliest date the database has is January 1, 2010. Start and end
 * Dates should be input in the following format: YYY-MM-DD
