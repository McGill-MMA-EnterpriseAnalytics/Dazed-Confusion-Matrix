# FRAMEWORK EXPLANATIONS
---
## 1. Framing the Problem
*Define the objective in business terms*

> - “You’ve got corruption, excessive force and domestic surveillance” - Jeffrey Ross, criminologist at University of Baltimore 
>- Baltimore officers used “overly aggressive tactics that unnecessarily escalate encounters, increase tensions and lead to unnecessary force” stated a report on the police department in 2015 
>- More than 300 people have been killed every year since 2015 
>- There is a clear issue with crime and policing in Baltimore. Corruption and inefficiencies within the police department have caused an unsafe city and cost the city millions of dollars that could be used towards more crime preventative initiatives.  
>- This has caused calls for reform, the most extreme ones being defunding of the police department 
>- “The better answer is to give police departments the resources they need to implement meaningful reforms” - Joe Biden when talking about police reform 
>- The objective in this case is to better prepare officers for crime handling by predicting the nature of the crime before the officers arrive on the scene. >- We believe that officers that are more prepared for the type of incident that they will encounter, will be able to handle the incident more efficiently and without excessive use of force. 

*How will your solution be used?*

We propose that all officers in the Baltimore police department have access to our model through our dashboard. They can access it in their patrol cars, as well as at their desk. When the officer receives a call that they have to respond to, and it is vague as to what they are about to encounter, they can put the information they receive from the call (date, time, inside/outside, location, premise) and input it into the dashboard. Our model will show a prediction for which type of crime they are about to deal with (robbery, auto theft, shooting, etc). This will allow the officer to arrive on scene prepared (with correct equipment, mentally, etc), rather than being surprised by what they see upon arrival to the scene.  

*What are the current solutions/workarounds (if any)?*

Current predictive policing strategies focus on predicting when and where a crime will occur 
These tools include: 

1. Crime anticipation system (CAS) - Amsterdam   
2. PreCobs - Germany 
3. PredPol - Los Angeles 
4. Hunchlab - Philadelphia 

These tools also predict type of crime, but have very low accuracy (none above 33% accuracy) They are more so used for preventative measures, whereas our solution has the goal of increasing policing effectiveness.

*How should you frame this problem (supervised/unsupervised, online/offline, etc.)?*

This problem is supervised, we get the features and make a prediction for a target variable in real time.We have data, and want to train a model to make predictions on future data based on the patterns found in our data. 

*How should performance be measured?*

Since this is a multi-class classification problem, we will measure performance with the f1 score of our model. If this model were to be applied in the real world, and deployed by the Baltimore Police department, a good measure of success would be the rates of complaints against police in the city. If the police are better prepared because of our accurate model, the number of police related issues should decrease.
As we cannot explore the above point, we have gathered data for years following our training data, and will test the model’s performance on crime that if deployed, the model would have been responsible for predicting. 

*Is the performance measure aligned with the business objective?* 

The ideal performance metric of police complaint rates is aligned with the business objective because it captures the issue of ineffective policing. However, the pure accuracy performance of our model does not guarantee solving the business objective. This is due to the countless confounding variables that could result in the deployment of this model. These include misuse, rejection to change, an underestimation of preparedness’ effect on good policing practices.  

*What would be the minimum performance needed to reach the business objective?*

Other predictive policing methods have accuracies around 30%, showing that predictive policing has a low threshold for success.  We believe that if our model is able to accurately predict the type of crime an officer will encounter over 50% of the time, that we would be able to effectively prepare officers to act more efficiently. 

*What are comparable problems? Can you reuse experience or tools?*

- The comparable problems are the crime prevention strategies already used in predictive policing (CAS, PredPol, Hunchlab, PredCobs) 
- We can reuse the type of data that are used in these tools (time, date, location) 
- The main difference is that for crime prevention, these tools look for patterns in past data and predict when a crime occurs. Our solution, which deals with effective policing, makes predictions based on information from the notification of the police in real time 

*Is human expertise available?*

- There are crime experts that coupled with our predictions, can show police how to best prepare for different situations.
- This solution would not work in the real world if it is not coupled with emphasis on buy in and training  

## 2. Data Acquisition
*This project was developed with the purpose of beginning a research cycle into predictive policing for Baltimore. To do so, the team created an ideal situation under which data acquisition would be of a higher level so that future developments can build on our project towards this potential goal.*

###### __IDEAL SITUATION__
The ideal situation is based on the orginal design of the opportunity presented by our team, under the logical hypothesis. This is also the overseeing goal of this project, to provide a basis to work towards this [logical hypothesis](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Project_Framework/Hypotheses.md) long-term. 

###### __PRACTICAL SITUATION__
The practical situation is the situation under which this project was built, according to constraints such as time and resource availability. It follows the redesign of the hypothesis into an [empirical hypothesis](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Project_Framework/Hypotheses.md). 

##### _List the data you need and how much you need_ 
---
###### __IDEAL SITUATION__

> - Complete data data on crimes in Baltimore, inclduing information on arrests and calls that were made where no crime was committed.
>- Current and up to date dataset on local crime sprees by description (arsonry, sexual assault, robberies, homicide, etc.)
>- Criminal records data on known criminals and areas of their last crimes by type of crime. 
>- Would require at least complete datasets on the last three years for all three types of data described above. 

###### __PRACTICAL SITUATION__
>- Open source dataset from Kaggle containing limited varIables, and data, on crimes in Baltimore. 
>- Information on the two years worth of crime in Baltimore.

##### _Find and document where you can get that data_ 
---
###### __IDEAL SITUATION__
>- FBI dataset would contain the advanced type of data that would be required on crimes in Baltimore, current crime sprees, criminal records and even potentially expected movement of crime from other cities & states.
>- If a release of this FBI dataset would not be avaialble thne the local police force databases in Baltimore would be able to provide local information on crime in Baltimore, limited information on expected & known crime sprees in Baltimore and known re-offending criminals. 
>- The police force databases in Baltimore can be supplemented with prison (dependent on scope of the analysis) datasets to have complete access on criminal records and status. 
 
###### __PRACTICAL SITUATION__
>- Kaggle contained an open source limited dataset on crime in Baltimore. 
 
##### _Check how much space it will take_
---
###### __IDEAL SITUATION__
>- Expected that storage will require additional considerations due to privacy issues and how big the datasets are. Therefore, would expect potentially utilizing object storage in the form OF external hard drives. 

###### __PRACTICAL SITUATION__
>- Open source and small dataset, so easily downloadable, therefore requires limited storage. 

##### _Check legal obligations and get authorization if necessary_
---
###### __IDEAL SITUATION__
>- Requires heavy legal obligations and high clearance due to the fact that this data contains private information and information belonging to the government and government entities. 
>- Authorization to attain and use this dataset is necessary

###### __PRACTICAL SITUATION__
>- There are no legal obligations or authorization required since the information is open source and it contains no sensitive information. 

##### _Get access authorizations_
---
###### __IDEAL SITUATION__
>- Authorization to attain and use this dataset is necessary.
>- The authorization would be coming from the owners of the dataset (ie, FBI, Baltimore police force, prisons, etc.)

###### __PRACTICAL SITUATION__
>- No authorization is required, open source dataset from Kaggle.

##### _Create a workspace(with enough storage space)_
---
###### __IDEAL SITUATION__
>- Workspace created would have to meet the expectations of those providing datasets due to privacy concerns. 

###### __PRACTICAL SITUATION__
>- The use of laptops was appropriate for the work being conducted for the purpose of this proejct. 

##### _Get the data_
---
###### __IDEAL SITUATION__
>- *Would have to reach out to the required parties above*

###### __PRACTICAL SITUATION__
>- The data was downloaded from Kaggle. The link to it is included in the project description. 

##### _Convert the data to a format you can easily manipulate (without changing the data itself)_
---
###### __IDEAL SITUATION__
>- Would have to determine if the datasets should be compacted into cSV files or determine another means for analysis. 

###### __PRACTICAL SITUATION__
>- Data was already in a format that could be easily manipulated, csv. 


##### _Ensure sensitive information is deleted or protected (e.g. anonymized)_
---
###### __IDEAL SITUATION__
>- Would determine standards to do this according to the contraints presented by all active parties.

###### __PRACTICAL SITUATION__
>- There was no sensitive information included in the data. 

##### _Check the size and type of the data (time series, sample, geographical, etc.)_
---
###### __IDEAL SITUATION__
>- Determined once the data is retrieved. Should be somewhat similar to the *PRACTICAL SITUATION* data type below. 

###### __PRACTICAL SITUATION__
>- It is 39.27 MB in size and the data can be considered time series and geographical, as the crime is divided by area and is occurring with the passing of time.
>

### Data Augmentation - Demographic Data
In the second part of the project, we wanted to add to our dataset to make better predictions, and also understand the inherent bias of our model. Because our model is based on past data, and includes neighborhood as a predictor, it is very possible that the model would be biased towards neighborhoods with certain characteristics. Therefore, we decided to gather the following variables for each neighborhood in each year in our original dataset: 
- 	Median household income 
-	Median price of homes sold 
-	Percent of family households living below the poverty line 
-	Percent of population 18-24 
-	Percent of population 25-64 
-	Percent of population 65+ 
-	Percent of Asian residents 
-	Percent of African-American residents 
-	Percent of Hispanic residents 
-	Percent of White residents 
-	Racial diversity index 
-	Total number of households 

Baltimore collects this data by what they call a Community Statistical Area (CSA). Each CSA is composed of a few neighborhoods, and often times it is hard to determinne which CSA a neighborhood belongs to solely based off name. Therefore, we had to manually match each neighborhood to its corresponding CSA. The matching file can be found here: _[neighborhoods.csv](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/data/neighborhoods.csv)_

#### Ethical AI - Merging the Data
One of the main issues with the demographic data was that there was a ton of missing information. On one hand, there were some neighborhoods in our data that were not associated with a CSA. On the other hand, not all data was collected every year, so we had some years where we were missing all information. Imputing demographic data can come with its own ethical issues, because you don't want to improperly impute and thus mask or augment some of the bias in the model. Therefore, for the missing years, we imputed the data with the median value for the same CSA in the years we had the data for. The cleaning, matching, and merging of the demographic data for the training data can be found in this _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/V2_Demographic_Data_Cleaning_Merging.ipynb)_. The same process was used for the test data and can be found in this _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/Test_data_demo_merging.ipynb)_.




## _[3. Data Exploration](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Model_Development/Visualization.ipynb)_
- 	Create a copy of the data for exploration (sampling it down to a manageable size if necessary)
- 	Create a Jupyter notebook to keep a record of your data exploration
- How do you profile your data?
- Download a dataset and provide: Missing Data (%), Quantile Statistics, Descriptive Statistics, Correlations
- Study each attribute and its characteristics
- Name Type (categorical, int/float, bounded/unbounded,text,structured, etc.)
- % of missing values
- Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
- Possibly useful for the task?
- Type of distribution (Gaussian, uniform, logarithmic, etc.)
- For supervised learning tasks, identify the target attributes
- 	Visualize the data
- 	Study the correlations between attributes
- 	Study how you would solve the problem manually
- 	Identify the promising transformations you may want to apply
- 	Identify extra data that would be useful (go back to “Get the Data”)
- 	Document what you have learned

## _[4. Data Preparation](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/Cleaning)_

### Data Re-cleaning

After attempting to train some new models with augmented demographic data, it was noticed that many categories in the "Premise" feature could be recategorized together, greatly reducing the number of categories, especially those with very few records. For example, "APT/CONDO" and "APT. LOCKE" were simplying merged into a single "APARTMENT" category. This _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/Recleaning.ipynb)_ contains all of the changes, while this _[text file](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/Data_transformations.txt)_ contains a record of all the modifications that were made for future iterations of this cleaning.

### Weekend and Holidays

Two features were added to the original data, binary variables denoting if a crime occurred on a weekend, and if it occurred on a holiday. The same _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/Recleaning.ipynb)_ as above contains the modifications, beginning at cell 106, and this code was again stored in the _[text file](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/Data_transformations.txt)_ for easier access, should this transformation need to be done on other data.

### Test Data Re-cleaning

One glaring issue was made apparent with the test data. Because we procured this data directly from the Baltimore PD website, it was in a slightly different format than the training data we had procured from kaggle. Apart from the transformations that we did already for the first part of the course, it was noticed that many of the fields in the test data were complete phrases/words, while our training data had many of them truncated. For example, the training data had a premise listed as "SINGLE HOU", while the test data listed it as "SINGLE HOUSE". This was the reason for the original mismatches in the label encoder that we faced in the first course, and these were all painfully changed manually one by one. To see the extent of what had to be done, please see this _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Cleaning/V2_test_data_cleaning.ipynb)_. 

### Missing Data

Unlike the original data where it was a bit questionable to impute features such as the premise of a crime, this was not the case with the demographic data. The demographic features are much more reliant on other features present in the original dataset such as the district, as well as longitude and latitude. The _[miceforest](https://github.com/AnotherSamWilson/miceforest)_ package was used to impute the missing demographic data after it was merged with the original dataset. Miceforest uses employs Multiple Imputation by Chained Equations, filling in missing data through an iterative series of models, in this case random forests. It uses something called predictive mean matching, where N original values closest to the predicted missing sample are chosen as candidates, from which a value is chosen at random. In this way the missing demographic data was filled in. The issue with imputing demographic data in this fashion is that it is measured by a constant by neighborhood, whereas the imputation is continuous. To account for this, the mean of the imputed values was calculated per neighborhood to mimic a neighborhood level imputation. This imputation model was then saved to be used on the test data. Though this model is far too large to store on github, the imputation process can be seen in this _[notebook](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/dev/Model_Development/Demographic_imputation_MICE.ipynb)_. 

## _[5. Modeling](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/Model_Development)_
- 	Train many quick and dirty models from different categories (e.g.,linear, naïve Bayes, SVM, Random Forests, neural net, etc.) using standard parameters
- 	Measure and compare performance:
- For each model, use N-fold cross-validation and compute the mean and standard deviation of the performance measure on the N folds.
- 	Analyze the most significant variables for each algorithm
- 	Analyse the types of errors the models make
-  What data would a human have used to avoid these errors?
- 	Have a quick round of feature selection and engineering
- 	Have one or two more quick iterations of the five previous steps.
- 	Short-list the top three to five most promising models, preferring models that make different types of errors.

## _[6. Model Evaluation](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/Model_Development)_
	SOTA Supervised Learning SECTION

## _[7. Model Selection](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/Model_Development)_

- 	Evaluation metrics
- 	Simplicity
- 	Explainability and interpretability
- 	Offline vs. online
- 	Batch vs. Real-time
-
## _[8. Model Fine-Tuning](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/Model_Development)_
- 	Fine-tune the hyperparameters using cross-validation
- Treat your data transformation choices as hyperparameters, especially when you are not sure about them (e.g., should I replace missing values with zero or with the median value? Or just drop the rows?)
- Unless there are very few hyperparameter values to explore, prefer random search over grid search. If training is very long, you may prefer a Bayesian optimization approach(e.g.,using Gaussian process priors, as described by Jasper Snoek, Hugo Larochelle, and Ryan Adams).
- 	Try Ensemble methods. Combining your best models will often perform better than running them individually
- 	Once you are confident about your final model, measure its performance on the test set to estimate the generalization error

## _[9. Solution Presentation](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/ppt)_
- 	Document what you have done
- Context
--   Context should present your understanding of the business problem
--  You should frame the problem such that is understandable for different stakeholders
-- It should cover a bried resume of 5.1.Framing the problem
-- It should give statistics about the current situation
-- It should present objectives and benefits
- [Hypothesis](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Project_Framework/Hypotheses.md)
- Document and communicate the hypotheses in terms of 
--What can be predicted/optimized
-- What are the actions can be taken
-- What are the possible outcomes
-- Communicate your hypothesis testing strategy to the right audience
--Null hypothesis
--Outcomes and types of errors
-- P-values and confidence intervals			
--Multiple testing and p-hacking
- Data
- Model	- Modeling Approach & Model Evaluation
- Results
-- 	Explainability of Results
- 	[Threats to Validity](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Project_Framework/Threats_to_Validity.md)
- 	Conclusion
- 	[Lessons Learned and Next Steps](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/blob/master/Project_Framework/Future_Work.md)

## _[10. Launching, Monitoring and Maintenance](https://github.com/McGill-MMA-EnterpriseAnalytics/Dazed-Confusion-Matrix/tree/master/ppt)_
- Get your solution ready for production (plug into production data inputs, write unit tests, etc.)
- W- te monitoring code to check your system’s live performance at regular intervals and trigger alerts when it drops.
- Beware of slow degradation too: models tend to “rot” as data evolves
- Measuring performance may require a human pipeline (e.g. via a crowdsourcing service)
- Also monitor your inputs’ quality (e.g., a malfunctioning sensor sending random values, or another team’s output becoming stale). This is particularly important for online learning systems
- Retrain your models on a regular basis on fresh data
