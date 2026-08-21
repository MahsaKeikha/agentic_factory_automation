from AGENTS.requirements_agent import run as a1
from AGENTS.controls_architecture_agent import run as a2
from AGENTS.integration_agent import run as a3
from AGENTS.verification_agent import run as a4
from AGENTS.safety_agent import run as a5
def orchestrate(c): return [a(c) for a in (a1,a2,a3,a4,a5)]