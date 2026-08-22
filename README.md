# F118 | Agentic Factory Automation | L3 Gold Standard | v1.0

A reference implementation of a governed multi-agent factory-automation architecture for requirements analysis, controls architecture, integration planning, verification, functional-safety review, cybersecurity review, and engineering release governance.

This repository is part of the Agentic AI Library, a collection of domain-specific multi-agent reference architectures intended for education, research, engineering practice, and adaptation into larger systems.

## Five-agent architecture

- Requirements Agent
- Controls Architecture Agent
- Integration Agent
- Verification Agent
- Safety Agent

## Reference architecture focus

F118 demonstrates a separation between engineering analysis and operational authority. The multi-agent workflow can assemble and review an automation engineering package, but operational control remains outside the autonomous scope of the reference implementation.

The architecture emphasizes requirements traceability, controller and integration design, verification evidence, functional safety, industrial-control cybersecurity, configuration management, and qualified-human approval.

## Gold-standard engineering governance

F118 is fail closed. Engineering-package release requires reviewed requirements, controls architecture, integration, verification, functional safety, cybersecurity, change traceability, and explicit qualified-engineering approval.

Release is blocked for incomplete or inconsistent requirements, unresolved safety-interlock gaps, failed or incomplete verification, unsafe coupling to live control, industrial-control cybersecurity risks, unreviewed PLC/robot/HMI/control-logic changes, traceability gaps, or unresolved unsafe operating conditions.

The reference implementation cannot autonomously deploy control logic, write to live controllers, change PLC or robot programs, alter safety logic, bypass interlocks, change operating setpoints, or commission a production cell.

## Verification strategy

The repository includes direct governance tests plus held-out scenarios that validate both successful release conditions and fail-closed behavior under missing approval, safety, verification, cybersecurity, control-change, and traceability failures.

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

## Intended use

Use this repository as a reference for designing governed multi-agent automation systems, teaching agent decomposition and orchestration patterns, evaluating human-approval boundaries, or adapting the architecture to a larger industrial engineering stack.

It is intentionally structured so that analysis, verification, and governance can be studied independently from live operational control.
