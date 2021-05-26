#%%
import numpy as np
import pandas as pd

def model_summary(fit, params='all', quantiles=[0.05, 0.95]):
    output_df = pd.DataFrame()

    if params == 'all':
        params = [x for x in fit.param_names]

    for param in params:
        this_df = pd.DataFrame()
        this_df['param'] = [param]
        this_df['mean'] = np.mean(fit[param])
        this_df['std'] = np.std(fit[param])
        this_df[[str(100*x)+'%' for x in quantiles]] = np.quantile(fit[param], quantiles)

        output_df = pd.concat([output_df, this_df])

    return(output_df)