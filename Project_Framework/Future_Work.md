# Future Work and Improvements

## Model Bias

Predictive policing practices have come under scrutiny for ethical reasons, one being algorithmic bias. Since the models are all built upon past data, it is very likely that the models are discriminatory towards low-means communities that have had histories of high crime rates and heavy policing. Our model is not immune to this issue, and we acknowledge that the use of it within a real-police department, at its current state, could be dangerous. Therefore, in the future we could look to control for the location specific variables in our model. We would want to see if we can still maintain accuracy while mitigating the risk of our model being unfairly biased. 

## Model Explainability

There is also the issue of model interpretation. Our current model is a bit of a black box, and does not show the officers why it is making predictions for certain types of crime. If they know more about how it works it and why it is predicting a crime for example to be an aggravated assault, they can be better prepared for the situation, and also trust the model more. Showing feature importances on the dashboard is a good step, so that they can see what variables are affecting the prediction, but if they do not understand the concepts and the data behind the predictions, it can create skepticism, reduce buy-in, and thus reduce the effectiveness of the solution in improving police encounters with crime. We would want to explore less complex models, and assess the tradeoff between explainability and accuracy, to hopefully create a more usable and impactful tool for the police to use. 
