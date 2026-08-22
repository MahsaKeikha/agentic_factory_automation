from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "requirements_reviewed": True,
    "controls_architecture_reviewed": True,
    "integration_reviewed": True,
    "verification_reviewed": True,
    "functional_safety_reviewed": True,
    "cybersecurity_reviewed": True,
    "change_traceability_reviewed": True,
    "qualified_engineering_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
