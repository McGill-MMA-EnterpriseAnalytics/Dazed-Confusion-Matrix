# Predictive Policing Research

## Article 1: Predictive Policing as a New Tool for Law Enforcement? Recent Developments and Challenges

[https://link.springer.com/article/10.1007/s10610-017-9361-2](https://link.springer.com/article/10.1007/s10610-017-9361-2)

[https://digital.hbs.edu/platform-rctom/submission/using-machine-learning-for-crime-prediction/#\_edn3](https://digital.hbs.edu/platform-rctom/submission/using-machine-learning-for-crime-prediction/#_edn3)

- What is predictive policing?
  - Three main objectives
    - Predicting perpetrators
    - Predicting victims
    - Predicting when and where there is a higher risk of new crime events
      - Predict future crimes as precise as possible in time and space and use that information to proactively guide police patrol routes or the locations of police controls
      - &quot;the use of historical data to create a spatiotemporal forecast of areas of criminality or crime hot spots that will be the basis for police resource allocation decisions with the expectation that having officers at the proposed place and time will deter or detect criminal activity
  - Inform crime prevention strategies
  - Predictive policing can be situated under intelligence-led policing (ILP)
    - Main objective is to apply crime data analysis to inform policy, policing strategy, and tactical operations in order to reduce and prevent crime
    - Emphasize proactive use of police resources, in contrast to reactive crime response strategies
  - Prospective hotspot analysis
    - Hotspots are formed not by the areas with the highest concentration of crime, but by the aggregation of risk zones surrounding each incident
    - These risk zones are temporary, making the hotspots dynamic
    - Main precursor to predictive policing
  - Risk terrain modeling
    - Using geographic information system, a risk map is created of locations sensitive to high crime rates, based (only) on their spatial properties and the interactions of those properties
- How does predictive policing work?
  - Data must be linked to a grid map of the area where it is used with the help of geocoding
  - Train a model to output the risk percentage for each grid cell based on the current values of the indicators
  - Can take into account available police operational capacity to create risk thresholds
  - Predictive policing can be applied to any crime type where:
    - Strong indicators for the risk of a crime event are known
    - Data regarding these indicators can be collected beforehand
    - Most suitable are typically crimes where the victim and perpetrators are strangers
      - Home burglary
      - Theft
      - Mugging
    - Less effective for drug crimes and relational violence
  - Three variables are always needed – time, place and type of crime (we have that)
  - Other variables that can be distinguished
    - Crime history variables
      - Time since last crime event
      - Number of crimes last month/six months/year
      - Number of crimes in neighboring grid cells
    - Time dependent variables
      - Weather
      - Seasons
      - Events
      - Holidays
      - Week/weekend
    - Opportunity variables
      - Population density
      - Escape routes such as distance to highway
      - Presence of public places (bars, shops, etc)
    - Precursor crimes
      - Preceding crime events
      - Escalation of violence
- Types of statistical models
  - Neural networks
    - Learn to recognize patterns in the data and self-correct in iterative cycles based on the known values of the response variable
    - Issue is that it is black box
  - Time space models
- Current Existing Applications
  - Crime Anticipation System (CAS)
    - Only the top 3% highest risk areas are mapped
    - Could predict 15% of home burglaries correctly and 36% almost correctly (the crime was predicted in a neighboring gridcell of an actual crime event)
    - Mugging was 33% and 57% almost
  - PreCobs
    - Only applicable to home burglaries
    - Each grid cell is 250m by 250m large
    - Uses time, place, and characteristics such as modus operandi and house type of past burglaries in the area
  - PredPol
    - Based on mathematical model which originally served to predict aftershocks of earthquakes
    - Only uses three variables
      - Time, place, and type of crime
      - Claims that this avoids any form of profiling or subjectivity
      - Grid cells are 150m by 150m
      - Different crime types are displayed on the same map
  - Hunchlab
    - Uses several hundred variables to make predictions
      - Choice is motivated to avoid skewing results towards areas of increased police activity when using only police registered crime data
    - Does not use a fixed size for grid cells (size can be chosen between 100 by 100 to 250 by 250 ![]
- How should it be evaluated?
  - Effectiveness of the predictive analysis
    - Main focus
  - Crime rates before predictive policing was introduced versus after
  - Costs relative to current methods being replaced by predictive policing\
- What are the Ethical, Juridical, and Ideological considerations that need to be made?
  - Gathering of data -\&gt; privacy concerns
  - Whether a prediction is good enough for police to take action
  - Does it lead to a higher risk of ethnic profiling and the neglect of basic principles such as the presumption of innocence
- Recommendations for predictive policing
  - Reliable data collection
  - Clear communication between units and hierarchy levels
  - Police response strategy

Takeaways for our project

- We could try to predict high risk grid cells for different types of crime
  - To do this we have to build the grids with the long/lat data
  - https://stackoverflow.com/questions/55199436/generate-grid-of-latitude-longitude-coordinates-that-fall-within-polygon
  - [https://data.baltimorecity.gov](https://data.baltimorecity.gov/)
  - If we decided that by grid is too hard, we can do it by district
- Our data should be suitable for this type of prediction
- We should explore neural networks as our model
- We should address ethical concerns such as racially biased algorithms, and overpolicing

# Baltimore Specific Research:

## Article 1: Baltimore tried reforming the police. They fought every change.

https://www.washingtonpost.com/outlook/baltimore-police-reforms-crime/2020/06/18/7d60e91e-b041-11ea-8758-bfd1d045525a\_story.html

- &quot;The better answer is to give police departments the resources they need to implement meaningful reforms&quot; – Joe Biden
- Baltimore police promised aggressive fixes to their department after the death of Freddie Gray in 2015, that were thwarted by a more aggressive police force
- Officers refused reform
  - Some doubled down on harassing citizens, violating their constitutional rights, and even fabricating probable cause to maintain &quot;law and order&quot;
- More than 300 people have been killed every year since 2015

## Article 2: Baltimore police union issues scathing report describing department in chaos due to mismanagement

[https://www.baltimoresun.com/news/crime/bs-md-ci-cr-police-union-report-20191008-tj75tobwjjavva4vgyjwf2pj24-story.html](https://www.baltimoresun.com/news/crime/bs-md-ci-cr-police-union-report-20191008-tj75tobwjjavva4vgyjwf2pj24-story.html)

- Blaming intense violence in the city on severe mismanagement of the police department
- One issue is that the department doesn&#39;t share and disseminate criminal intelligence between units or with surrounding jurisdictions
- Extremely unorganized

## Article 3: The Tragedy of Baltimore

[https://www.nytimes.com/2019/03/12/magazine/baltimore-tragedy-crime.html]

- A crackdown on crime starting in the early 2000s decreased crime rates and murders, but increased arrests. Showing inefficient use of policing
- Tony Barksdale&#39;s initiative which included meetings with CitiStat (data department) to review data on firearms prosecutions, led to arrests falling by a third from 2006-2011, and homicides going down as well
- Baltimore officers used &quot;overly aggressive tactics that unnecessarily escalate encounters, increase tensions and lead to unnecessary force&quot; stated a report on the police department in 2015

## Article 4: In Baltimore, Police Seem Everywhere and Nowhere at Once

[https://www.governing.com/archive/gov-baltimore-police-paradox.html](https://www.governing.com/archive/gov-baltimore-police-paradox.html)

- &quot;You&#39;ve got corruption, excessive force and domestic surveillance&quot; – Jeffrey Ross, criminologist at University of Baltimore
- In the four years leading up to 2015, more than 100 people who suffered broken bones, head trauma and even death in altercations with the police, won settlements


```python

```
