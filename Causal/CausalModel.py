import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from causallift import CausalLift
from IPython.display import display


def causal_lift_model(cm_df, treatment_name, seed=5):
    # Need to drop null for computations - could also impute these
    cm_df['treatment_name'] = cm_df['treatment_name'].dropna()
    cm_df.reset_index(inplace=True)

    # Separate treatment into two categories (below or above average)
    treatment_below_avg = cm_df['treatment_name'].mean()
    cm_df['Treatment'] = np.where(cm_df['treatment_name'] <= treatment_below_avg, 1, 0)

    # Get each outcome and loop through them testing them as binary variables
    outcome_names = set(cm_df['Description'].values)

    for outcome in outcome_names:
        print('\n{}'.format(outcome))
        cm_df['Outcome'] = np.where(cm_df['Description'] == outcome, 1, 0)
        cm_df = cm_df[['Treatment', 'Outcome',
                       'Weapon_FIREARM', 'Weapon_HANDS', 'Weapon_KNIFE', 'Weapon_NONE', 'Weapon_OTHER',
                       'Season_autumn', 'Season_spring', 'Season_summer', 'Season_winter',
                       'Holiday', 'Weekend', 'Neighborhood', 'Premise', 'Month', 'Hour', 'Year', 'Outside']]

        train_df, test_df = train_test_split(cm_df, test_size=0.3, random_state=seed, stratify=cm_df['Treatment'])

        print('\n[Estimate propensity scores for Inverse Probability Weighting.]')
        cl = CausalLift(train_df, test_df, enable_ipw=True, verbose=3)

        print(
            '\n[Create 2 models for treatment and untreatment and estimate CATE (Conditional Average Treatment Effects)]')
        train_df, test_df = cl.estimate_cate_by_2_models()

        print('\n[Estimate the effect of recommendation based on the uplift model]')
        estimated_effect_df = cl.estimate_recommendation_impact()

        print('\n[Show the estimated effect of recommendation based on the uplift model]')
        display(estimated_effect_df)

