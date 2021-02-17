# 5.1 Framing the Problem 

##### _Define the objective in business terms_ 
---

> - “You’ve got corruption, excessive force and domestic surveillance” - Jeffrey Ross, criminologist at University of Baltimore 
>- Baltimore officers used “overly aggressive tactics that unnecessarily escalate encounters, increase tensions and lead to unnecessary force” stated a report on the police department in 2015 
>- More than 300 people have been killed every year since 2015 
>- There is a clear issue with crime and policing in Baltimore. Corruption and inefficiencies within the police department have caused an unsafe city and cost the city millions of dollars that could be used towards more crime preventative initiatives.  
>- This has caused calls for reform, the most extreme ones being defunding of the police department 
>- “The better answer is to give police departments the resources they need to implement meaningful reforms” - Joe Biden when talking about police reform 
>- The objective in this case is to better prepare officers for crime handling by predicting the nature of the crime before the officers arrive on the scene. >- We believe that officers that are more prepared for the type of incident that they will encounter, will be able to handle the incident more efficiently and without excessive use of force. 

 

##### _How will your solution be used?_ 
---
 

We propose that all officers in the Baltimore police department have access to our model through our dashboard. They can access it in their patrol cars, as well as at their desk. When the officer receives a call that they have to respond to, and it is vague as to what they are about to encounter, they can put the information they receive from the call (date, time, inside/outside, location, premise) and input it into the dashboard. Our model will show a prediction for which type of crime they are about to deal with (robbery, auto theft, shooting, etc). This will allow the officer to arrive on scene prepared (with correct equipment, mentally, etc), rather than being surprised by what they see upon arrival to the scene.  

 

##### _What are the current solutions/workarounds (if any)?_
---

Current predictive policing strategies focus on predicting when and where a crime will occur 
These tools include: 

1. Crime anticipation system (CAS) - Amsterdam   
2. PreCobs - Germany 
3. PredPol - Los Angeles 
4. Hunchlab - Philadelphia 

These tools also predict type of crime, but have very low accuracy (none above 33% accuracy) They are more so used for preventative measures, whereas our solution has the goal of increasing policing effectiveness.

##### _How should you frame this problem (supervised/unsupervised, online/offline, etc.)?_
---
This problem is supervised, we get the features and make a prediction for a target variable in real time.We have data, and want to train a model to make predictions on future data based on the patterns found in our data. 

##### _How should performance be measured?_
---
Since this is a multi-class classification problem, we will measure performance with the f1 score of our model. If this model were to be applied in the real world, and deployed by the Baltimore Police department, a good measure of success would be the rates of complaints against police in the city. If the police are better prepared because of our accurate model, the number of police related issues should decrease.
As we cannot explore the above point, we have gathered data for years following our training data, and will test the model’s performance on crime that if deployed, the model would have been responsible for predicting. 

 

##### _Is the performance measure aligned with the business objective?_
---

 

The ideal performance metric of police complaint rates is aligned with the business objective because it captures the issue of ineffective policing. However, the pure accuracy performance of our model does not guarantee solving the business objective. This is due to the countless confounding variables that could result in the deployment of this model. These include misuse, rejection to change, an underestimation of preparedness’ effect on good policing practices.  

 

##### _What would be the minimum performance needed to reach the business objective?_
---

 

Other predictive policing methods have accuracies around 30%, showing that predictive policing has a low threshold for success.  We believe that if our model is able to accurately predict the type of crime an officer will encounter over 50% of the time, that we would be able to effectively prepare officers to act more efficiently. 

 

##### _What are comparable problems? Can you reuse experience or tools?_
---
- The comparable problems are the crime prevention strategies already used in predictive policing (CAS, PredPol, Hunchlab, PredCobs) 
- We can reuse the type of data that are used in these tools (time, date, location) 
- The main difference is that for crime prevention, these tools look for patterns in past data and predict when a crime occurs. Our solution, which deals with effective policing, makes predictions based on information from the notification of the police in real time 

 

##### _Is human expertise available?_
---
- There are crime experts that coupled with our predictions, can show police how to best prepare for different situations.
- This solution would not work in the real world if it is not coupled with emphasis on buy in and training  
