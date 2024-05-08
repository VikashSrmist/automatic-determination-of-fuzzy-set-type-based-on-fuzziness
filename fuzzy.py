import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Step 4: Define Fuzzy System
# Create Antecedent/Consequent objects and define fuzzy membership functions
input_feature = ctrl.Antecedent(np.arange(0, 11, 1), 'input_feature')
output_fuzzy_set = ctrl.Consequent(np.arange(0, 11, 1), 'fuzzy_set_type')

# Define fuzzy membership functions for input and output
input_feature['low'] = fuzz.trimf(input_feature.universe, [0, 0, 5])
input_feature['high'] = fuzz.trimf(input_feature.universe, [5, 10, 10])

output_fuzzy_set['low'] = fuzz.trimf(output_fuzzy_set.universe, [0, 0, 5])
output_fuzzy_set['high'] = fuzz.trimf(output_fuzzy_set.universe, [5, 10, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(input_feature['low'], output_fuzzy_set['low'])
rule2 = ctrl.Rule(input_feature['high'], output_fuzzy_set['high'])

# Step 5: Create Fuzzy Control System
fuzzy_ctrl = ctrl.ControlSystem([rule1, rule2])
fuzzy_sim = ctrl.ControlSystemSimulation(fuzzy_ctrl)

# Step 6: Use the Model
# Assuming you have input values for 'input_feature'
fuzzy_sim.input['input_feature'] = 3.5  # Example input value
fuzzy_sim.compute()

# Step 7: Access Output
output_value = fuzzy_sim.output['fuzzy_set_type']
print("Output fuzzy set type:", output_value)
