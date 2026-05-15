import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import requests
from supabase import create_client

ODDS_API_KEY = os.environ['ODDS_API_KEY']
SUPABASE_URL = os.environ['SUPABASE_URL']
SUPABASE_KEY = os.environ['SUPABASE_SERVICE_ROLE_KEY']

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print('Starting NBA prop model run...')
print('UTC:', datetime.now(timezone.utc).isoformat())

# TODO:
# 1. Pull Odds API data
# 2. Pull NBA game logs
# 3. Build feature dataframe
# 4. Train XGBoost models
# 5. Generate edge_df
# 6. Upload to Supabase

print('Environment OK')
print('Finished NBA prop model run.')
