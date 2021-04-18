import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from causallift import CausalLift
from IPython.display import display


def causal_lift_model(cm_df, decoder, treatment_name, use_multi=True, seed=5):
    # Need to drop null for computations - could also impute these
    original_len = len(cm_df)
    print('Original data length {}'.format(original_len))
    cm_df[treatment_name] = cm_df[treatment_name].dropna().reset_index(drop=True)
    clean_len = len(cm_df)
    print('Clean data length {}'.format(clean_len))
    ratio_dropped = (original_len - clean_len) / clean_len

    # Separate treatment into two categories (below or above average)
    treatment_below_avg = cm_df[treatment_name].mean()
    cm_df['Treatment'] = np.where(cm_df[treatment_name] <= treatment_below_avg, 1, 0)

    # Use multiple classes as target
    if use_multi:
        cm_df['Outcome'] = cm_df['Description']
        # Use the top 10 features
        cm_df = cm_df[['Treatment', 'Outcome',
                            'Weapon_FIREARM', 'Weapon_HANDS', 'Weapon_KNIFE', 'Weapon_NONE', 'Weapon_OTHER',
                            'Neighborhood', 'Premise', 'Month', 'Hour', 'Outside']]
        train_df, test_df = train_test_split(cm_df, test_size=0.2, random_state=seed, stratify=cm_df['Treatment'])

        print('\n[Estimate propensity scores for Inverse Probability Weighting.]')
        CausalLift(train_df, test_df, enable_ipw=True, verbose=3)

    # Use each class as a binary outcome
    else:
        # Get each outcome and loop through them testing them as binary variables
        outcome_names = set(cm_df['Description'].values)
        print(outcome_names)

        for outcome in outcome_names:
            cm_df_copy = cm_df.copy()
            print('\n{}'.format(decoder[outcome]))
            cm_df_copy['Outcome'] = np.where(cm_df_copy['Description'] == outcome, 1, 0)
            print(cm_df_copy['Outcome'])
            # Use the top 10 features
            cm_df_copy = cm_df_copy[['Treatment', 'Outcome',
                           'Weapon_FIREARM', 'Weapon_HANDS', 'Weapon_KNIFE', 'Weapon_NONE', 'Weapon_OTHER',
                           'Neighborhood', 'Premise', 'Month', 'Hour', 'Outside']]

            train_df, test_df = train_test_split(cm_df_copy, test_size=0.2, random_state=seed, stratify=cm_df_copy['Treatment'])

            print('\n[Estimate propensity scores for Inverse Probability Weighting.]')
            CausalLift(train_df, test_df, enable_ipw=True, verbose=3)
