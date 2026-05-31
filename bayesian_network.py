from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
bn = BayesianNetwork([
    ('Rain', 'Traffic'),
    ('Traffic', 'Late')
])

# CPD for Rain
rain_prob = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7],
            [0.3]]
)

# CPD for Traffic given Rain
traffic_prob = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# CPD for Late given Traffic
late_prob = TabularCPD(
    variable='Late',
    variable_card=2,
    values=[
        [0.9, 0.1],
        [0.1, 0.9]
    ],
    evidence=['Traffic'],
    evidence_card=[2]
)

# Add CPDs to the network
bn.add_cpds(rain_prob, traffic_prob, late_prob)

# Perform inference
ve = VariableElimination(bn)

query_result = ve.query(
    variables=['Late'],
    evidence={'Rain': 1}
)

print(query_result)
