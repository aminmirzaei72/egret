# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 05:06:27 2024

@author: Mohammad Amin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 04:41:28 2024

@author: Mohammad Amin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:19:27 2024

@author: Mohammad Amin
"""

# Imports
from prescient.simulator import Prescient

# Set some options
prescient_options = {
    "data_path": r"C:\Desktop\MFOPF\data\texas7k\SourceData",
    "input_format": "rts-gmlc",
    "simulate_out_of_sample":True,
    "run_sced_with_persistent_forecast_errors":True,
    "output_directory": r"C:\Desktop\7k bus system",
    "start_date":"01-01-2018",
    "num_days": 7,
    "sced_horizon": 1,
    "ruc_mipgap": 0.01,
    "reserve_factor": 0.1,
    "deterministic_ruc_solver": "gurobi",
    "sced_solver": "gurobi",
    "sced_frequency_minutes": 5,
    "ruc_horizon": 36,
    "compute_market_settlements": True,
    "price_threshold": 1000,
    "contingency_price_threshold": 100,
    "reserve_price_threshold": 5,
    # Uncommented and set to default "btheta" for completeness
    #"ruc_network_type": "btheta",
    #"sced_network_type": "btheta",
      "monitor_all_contingencies":True,
      "output_solver_logs":False,
}

# Run the simulator
Prescient().simulate(**prescient_options)
