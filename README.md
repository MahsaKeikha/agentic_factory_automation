# F118 | Agentic Factory Automation | L3 Gold Standard | v1.0

A governed five-agent reference architecture for factory-automation engineering across requirements analysis, controls architecture, PLC and robot integration planning, I/O and interface mapping, verification, functional-safety review, industrial-control cybersecurity, commissioning preparation, configuration traceability, and qualified human engineering approval.

F118 is engineering-support only. It can structure automation requirements, design artifacts, hazards, tests, interfaces, logic-change reviews, and commissioning evidence, but it cannot autonomously deploy control logic, write to live controllers, change PLC or robot programs, modify safety logic, bypass interlocks, change operating setpoints, or commission a production cell.

## Factory automation lifecycle

```text
Automation Need and Process Context
        -> Requirements Definition
        -> Controls Architecture
        -> I/O and Interface Mapping
        -> PLC / Robot / HMI Integration Planning
        -> Verification and Validation
        -> Functional Safety Review
        -> Industrial Cybersecurity Review
        -> Commissioning Readiness
        -> Qualified Human Engineering Approval
```

The workflow is fail closed. Incomplete requirements, unresolved safety gaps, failed verification, unsafe live-control coupling, cybersecurity risk, unreviewed control changes, traceability gaps, or unsafe operating conditions prevent release.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Requirements Agent | Captures process, machine, interface, performance, quality, safety, and operational requirements | What must the automation system do, under what conditions, and with which constraints? |
| Controls Architecture Agent | Defines controller topology, PLCs, robots, HMIs, networks, states, sequences, interlocks, and control boundaries | Is the controls architecture appropriate for the process and risk profile? |
| Integration Agent | Maps I/O, devices, communication interfaces, handshakes, subsystem dependencies, and data flows | Will the machines, controllers, robots, sensors, actuators, and supervisory systems integrate coherently? |
| Verification Agent | Develops test coverage, requirements traceability, simulation, FAT/SAT, commissioning evidence, and failure-case testing | Has the automation design been adequately verified against its requirements? |
| Safety Agent | Reviews hazards, protective functions, interlocks, safe states, cybersecurity interactions, and human approval boundaries | Are functional-safety and operational risks adequately addressed before release? |

The agents support automation engineering. They do not replace controls engineers, electrical engineers, robotics engineers, machine-safety professionals, cybersecurity specialists, operators, commissioning teams, OEMs, integrators, or authorized plant personnel.

## Repository structure

```text
AGENTS/
├── requirements_agent.py
├── controls_architecture_agent.py
├── integration_agent.py
├── verification_agent.py
└── safety_agent.py

SKILLS/
├── requirements_reasoning.py
├── controls_reasoning.py
├── integration_reasoning.py
├── verification_reasoning.py
└── safety_reasoning.py

TOOLS/
├── io_map.py
├── interface_register.py
├── hazard_register.py
├── test_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates engineering reasoning from deterministic I/O maps, interface registers, hazard registers, test records, governance gates, evaluation, and observability.

## Automation requirements

The safety policy requires `requirements_reviewed`.

A governed requirement set can include:

```text
process_function
machine_function
operating_modes
cycle_time
throughput
quality_requirements
sequence_requirements
manual_mode
automatic_mode
maintenance_mode
fault_recovery
safety_requirements
interlocks
alarms
operator_interface
network_interfaces
data_logging
traceability
cybersecurity
commissioning_requirements
```

`requirements_gap` blocks release when material requirements remain incomplete or inconsistent.

The system should expose missing requirements rather than silently inventing process behavior, safe states, timing, device capabilities, or operator responsibilities.

## Requirement quality

Good automation requirements should be sufficiently:

- clear
- testable
- traceable
- bounded
- internally consistent
- versioned
- owned

Ambiguous requirements should be escalated rather than translated directly into control logic.

## Functional decomposition

Automation scope can be decomposed into:

```text
cell -> machine -> station -> subsystem -> device -> I/O point
```

Functional decomposition helps preserve traceability between process intent and implementation details.

## Operating modes

Control systems frequently support multiple modes such as:

- automatic
- manual
- setup
- maintenance
- jog
- recovery
- faulted
- safe state

Mode behavior should be explicit. A command that is permissible in maintenance mode may be unsafe in automatic production.

## State-machine and sequence design

Automation logic often depends on ordered states and transitions.

A governed state design can preserve:

```text
state
entry_conditions
actions
exit_conditions
transition_guards
timeouts
fault_paths
safe_state
recovery_logic
```

F118 should identify unreachable states, uncontrolled transitions, ambiguous recovery paths, or conflicting sequence assumptions.

## Controls architecture

`SKILLS/controls_reasoning.py` supports control-system architecture review.

Architecture can include:

- PLCs
- safety PLCs
- robot controllers
- motion controllers
- drives
- remote I/O
- HMIs
- SCADA
- MES interfaces
- vision systems
- sensors
- actuators
- industrial networks
- gateways
- historians

The safety policy requires `controls_architecture_reviewed`.

The architecture should distinguish standard control from safety control and should preserve authority boundaries between supervisory and machine-level systems.

## PLC architecture

PLC review can consider:

- processor selection
- redundancy
- scan-time constraints
- memory
- I/O capacity
- communication load
- safety separation
- program organization
- fault behavior
- diagnostics
- maintainability

F118 can review candidate architecture but cannot autonomously deploy PLC logic.

## Robot integration

Robot integration can involve:

- robot states
- safe zones
- handshakes
- part-present signals
- tooling state
- motion complete
- fault status
- safety interfaces
- vision coordination
- conveyor tracking
- recovery sequences

The system should preserve the distinction between production sequencing and robot safety functions.

## HMI design

HMI review can consider:

- operating status
- alarms
- controls
- mode indication
- permissives
- interlocks
- diagnostics
- maintenance information
- reset behavior
- role-based access

The HMI should not expose dangerous commands without appropriate safeguards, permissions, or mode restrictions.

## I/O mapping

`TOOLS/io_map.py` provides a deterministic surface for mapping signals.

An I/O record can include:

```text
tag
address
device
signal_type
direction
units
normal_state
safe_state
source
destination
interlock_relationship
alarm_relationship
version
```

I/O maps should remain synchronized with electrical drawings, control logic, devices, and commissioning records.

## Interface register

`TOOLS/interface_register.py` tracks subsystem and system interfaces.

Interfaces can include:

- PLC to PLC
- PLC to robot
- PLC to drive
- PLC to HMI
- PLC to MES
- PLC to SCADA
- robot to vision
- machine to conveyor
- equipment to safety system
- equipment to utility systems

An interface record can preserve protocol, message or signal definition, ownership, timing, error handling, and version.

## Handshake design

Machine-to-machine and controller-to-controller handshakes should explicitly define:

```text
request
acknowledge
ready
busy
complete
fault
timeout
reset
```

Ambiguous handshakes can create race conditions, deadlocks, repeated actions, lost parts, or unsafe recovery behavior.

## Network architecture

Industrial networks can include Ethernet-based and fieldbus technologies, wireless links, gateways, and segmented control zones.

Review can consider:

- topology
- bandwidth
- determinism
- redundancy
- addressing
- segmentation
- device identity
- diagnostics
- failure behavior
- cybersecurity

Network design should not assume enterprise IT patterns are automatically appropriate for real-time or safety-relevant control.

## Timing and determinism

Automation performance may depend on:

- PLC scan time
- network update rate
- robot cycle time
- drive update rate
- sensor response
- HMI latency
- sequence timeout
- process dynamics

Timing requirements should be traceable and verified rather than assumed.

## Motion control

Motion systems can introduce additional risks involving speed, position, torque, coordinated axes, safe motion, and mechanical limits.

F118 can review motion-control requirements and evidence but cannot write live motion setpoints or bypass motion safety functions.

## Interlocks

Interlocks can prevent invalid or unsafe actions.

Interlock review should preserve:

```text
condition
protected action
normal state
safe state
reset behavior
failure response
bypass policy
verification test
```

`safety_interlock_gap` blocks release when a safety interlock or protective-function gap remains unresolved.

## Permissives and inhibits

The system should distinguish permissives, inhibits, alarms, and safety trips.

A normal process permissive should not be presented as equivalent to a safety-rated protective function unless the architecture actually supports that claim.

## Safe states

Safe states should be identified according to the process hazard and machine design.

A safe state may involve:

- de-energized motion
- controlled stop
- maintained pressure
- isolated energy
- safe torque off
- guarded position
- ventilation maintained

The correct safe state is context dependent and must not be inferred generically.

## Functional safety

The safety policy requires `functional_safety_reviewed`.

Functional-safety review can include:

- hazard identification
- risk estimation
- required protective functions
- safety architecture
- diagnostic coverage
- fault reaction
- safe-state definition
- validation evidence
- reset behavior
- bypass management
- proof or functional testing

F118 is not a certification authority and does not independently assign or certify safety integrity levels or performance levels.

## Hazard register

`TOOLS/hazard_register.py` provides structured hazard tracking.

A hazard record can include:

```text
hazard_id
hazard
cause
consequence
exposure
existing_controls
required_controls
safe_state
verification
owner
status
```

Hazards should remain open until qualified review establishes that controls are adequate.

## Hierarchy of controls

Automation risk reduction should not rely only on software warnings when higher-order controls are feasible.

Relevant control categories can include:

- inherent design measures
- guards and physical barriers
- engineered safety functions
- administrative procedures
- warnings and training

The system should not recommend removal of a physical safeguard merely because software detection exists.

## Safety logic boundary

`change_safety_logic` is protected.

F118 can analyze proposed safety-logic changes and associated evidence, but it cannot autonomously modify or approve live safety logic.

## Interlock bypass boundary

`bypass_interlock` is permanently protected.

The system cannot autonomously bypass safety interlocks, guards, trips, permissives, emergency stops, or other protective functions.

## Standard control logic

Control logic can include:

- sequencing
- timers
- counters
- state machines
- recipes
- mode handling
- alarms
- diagnostics
- fault recovery
- device abstraction

Even standard logic changes can affect safety and must be reviewed for unintended interactions.

## PLC logic boundary

`change_plc_logic` is protected.

The system may draft logic specifications, pseudocode, or review notes, but it cannot autonomously write or release PLC program changes into a live controller.

## Robot program boundary

`change_robot_program` is protected.

Robot motion and program changes can create collision, reach, speed, tooling, and human-safety hazards. Final changes require qualified engineering and operational approval.

## Live-controller boundary

`write_live_controller` is protected.

F118 should separate offline engineering artifacts from any pathway capable of writing to a physical PLC, robot, drive, HMI, or controller.

## Deployment boundary

`deploy_control` is protected.

A validated engineering package does not authorize autonomous deployment into production equipment.

## Setpoint boundary

`change_operating_setpoint` is protected.

F118 can analyze candidate setpoints or process constraints but cannot autonomously write machine, drive, motion, process, or safety setpoints.

## Integration review

`SKILLS/integration_reasoning.py` supports multi-system integration analysis.

The safety policy requires `integration_reviewed`.

Integration review can consider:

- signal ownership
- data types
- units
- protocol
- timing
- sequencing
- handshake behavior
- startup order
- shutdown order
- fault propagation
- reset behavior
- network failure
- partial availability

Complex failures often emerge at interfaces rather than inside individual components.

## Startup and shutdown sequences

Controlled startup and shutdown should define prerequisites, sequencing, safe intermediate states, failure handling, and restart conditions.

The system should not assume that reversing the startup sequence is automatically a safe shutdown strategy.

## Fault handling

Fault design can include:

- fault detection
- latching
- alarm generation
- automatic recovery
- manual recovery
- escalation
- safe response
- diagnostic information

Automatic recovery should be limited where unexpected restart could create risk.

## Restart prevention

After emergency stop, safety trip, loss of power, communication failure, or certain faults, automatic restart may be unsafe.

F118 should explicitly review restart behavior and human-reset requirements.

## Alarm management

Alarm design can consider:

- priority
- cause
- consequence
- operator action
- nuisance alarms
- shelving
- latching
- acknowledgment
- history

Too many low-quality alarms can mask important conditions and create alarm fatigue.

## Verification

`SKILLS/verification_reasoning.py` and `TOOLS/test_register.py` support requirements-based verification.

The policy requires `verification_reviewed`.

`verification_failure` blocks release when verification or commissioning evidence is incomplete or failed.

## Test register

A test record can include:

```text
test_id
requirement
preconditions
procedure
expected_result
actual_result
pass_fail
evidence
software_version
hardware_configuration
reviewer
```

Tests should be traceable to the requirements they verify.

## Verification coverage

Coverage can include:

- normal operation
- manual mode
- automatic mode
- maintenance mode
- boundary conditions
- fault conditions
- communication loss
- sensor failure
- actuator failure
- safety trips
- reset behavior
- startup and shutdown
- recovery

A successful nominal-cycle test is not sufficient evidence for robust automation behavior.

## Simulation and emulation

Offline simulation, PLC emulation, robot simulation, and virtual commissioning can identify defects before physical commissioning.

Simulation results should remain distinguishable from tests performed on the actual production system.

## FAT and SAT

Factory acceptance testing and site acceptance testing can validate different aspects of system readiness.

F118 can organize FAT and SAT evidence but should not represent one as a substitute for the other when site-specific interfaces, utilities, process behavior, or safety conditions remain untested.

## Commissioning preparation

Commissioning preparation can include:

- approved drawings
- current software versions
- I/O checkout plan
- loop checks
- device configuration
- network configuration
- safety validation plan
- controlled test procedures
- rollback plan
- backups
- change authorization
- qualified personnel

`commission_cell` is protected. F118 cannot autonomously commission a production cell.

## Dry-run and reduced-risk modes

Early commissioning may use reduced-speed, no-load, simulation, manual, or restricted-access modes.

Such modes still require qualified safety review. Reduced speed or manual control does not automatically make a hazardous machine safe.

## Change management

Automation changes can affect process, quality, safety, cybersecurity, maintenance, and production.

`unreviewed_logic_change` blocks release when PLC, robot, HMI, or control logic has changed without appropriate review.

A controlled change record should preserve:

```text
change_id
reason
baseline_version
new_version
affected_requirements
affected_logic
affected_interfaces
affected_safety_functions
affected_tests
reviewers
approval
```

## Traceability

The policy requires `change_traceability_reviewed`.

`traceability_gap` blocks release when requirements, logic, tests, or configuration cannot be linked reliably.

Useful traceability can connect:

```text
requirement -> design -> logic -> I/O -> interface -> test -> version -> approval
```

This is central to debugging, maintenance, auditability, and safe change control.

## Configuration management

Configuration should preserve versions of:

- PLC code
- robot programs
- HMI application
- safety code
- drive parameters
- network configuration
- I/O maps
- recipes
- device firmware
- electrical drawings
- test evidence

The physical machine configuration should match the reviewed software and documentation baseline.

## Backup and restore

Automation systems should maintain controlled backups of critical programs and configurations.

Restore procedures should prevent accidental deployment of obsolete or unsafe versions.

## Industrial-control cybersecurity

The policy requires `cybersecurity_reviewed`.

`cybersecurity_risk` blocks release when industrial-control cybersecurity risk remains unresolved.

Review can include:

- asset inventory
- network segmentation
- remote access
- least privilege
- authentication
- engineering workstation security
- controller access
- firmware integrity
- software supply chain
- backups
- logging
- patch governance
- removable media
- vendor access

Cybersecurity failures can become physical safety or production risks in industrial systems.

## IT and OT boundaries

Factory automation should preserve the distinction between enterprise IT and operational technology.

OT systems can have stricter requirements for determinism, uptime, safety, maintenance windows, and compatibility. Security controls should be adapted to operational constraints rather than copied blindly from enterprise environments.

## Remote access

Remote engineering access can create significant risk.

A governed design should consider:

- authorized users
- multi-factor authentication
- session logging
- time-bounded access
- jump hosts
- least privilege
- vendor access
- change approval

F118 cannot grant access or make live changes autonomously.

## Unsafe operating conditions

`unsafe_operating_condition` is a hard blocker.

Potential examples include:

- defeated guard
- unresolved exposed motion
- unsafe robot reach
- uncontrolled stored energy
- failed safety device
- unexpected restart
- unsafe process condition
- missing protective function

The system should escalate rather than normalize these conditions.

## Energy isolation and maintenance

Factory automation intersects with lockout, tagout, stored-energy control, and maintenance procedures.

F118 can map control-system implications but cannot substitute software states for physical energy-isolation requirements where those are required.

## Human-machine interaction

Automation design should consider operator visibility, workload, error recovery, access, maintenance, training, and understandable alarms.

The system should not assume that eliminating manual steps is automatically safer or more usable.

## Ergonomics and accessibility

Operator interfaces and workstations should consider ergonomic and accessibility needs where applicable.

Automation performance should not be improved by transferring unreasonable physical or cognitive burden to workers.

## Quality integration

Automation can control process parameters, inspection, traceability, reject handling, and error-proofing.

Quality-relevant controls should be traceable and should not be removed or bypassed solely to improve throughput.

## Recipe and parameter management

Recipes and process parameters can affect product quality and machine safety.

A governed implementation should preserve authorization, versioning, allowable ranges, source, and traceability of parameter changes.

## MES and enterprise interfaces

Factory automation can exchange data with MES, ERP, historians, quality systems, and analytics platforms.

Supervisory requests should not automatically become executable control commands without validation and authority checks.

## Machine vision

Vision systems may support inspection, identification, localization, or robot guidance.

F118 should preserve confidence, failure handling, lighting assumptions, calibration, and fallback behavior. A vision model failure should not silently create unsafe robot motion or quality release.

## Barcode and traceability systems

Identification systems can support lot, serial, material, and process traceability.

The automation should define behavior for unreadable, duplicate, missing, or conflicting identifiers.

## Conveyor and material handling

Material-handling systems require coordination across sensors, zones, motors, accumulation logic, routing, and downstream readiness.

Review should consider jams, blocked sensors, lost parts, downstream faults, and safe recovery.

## Robotics safety boundary

Robot applications can introduce hazards from motion, tooling, payloads, collaborative operation, and shared workspaces.

F118 can organize robot safety requirements and verification evidence but does not certify the safety of a robot cell.

## Collaborative robotics

Collaborative applications require specific risk assessment and engineered protective measures.

The label collaborative does not mean inherently safe. Speed, force, tooling, workpiece hazards, and foreseeable misuse must still be reviewed.

## Safety-rated versus standard signals

The system should distinguish safety-rated signals and architectures from standard control signals.

A standard PLC bit that mirrors a safety state is not itself a safety function unless the complete architecture supports that claim.

## Fail-safe behavior

Failure behavior should be explicit for:

- loss of power
- loss of air
- sensor failure
- communication loss
- controller fault
- drive fault
- safety-system fault

The desired fail-safe behavior depends on the process and should not be generalized without engineering review.

## Diagnostics and maintainability

A good automation system should support efficient troubleshooting without encouraging unsafe bypasses.

Diagnostics can include:

- device status
- interlock state
- permissive state
- sequence step
- alarm cause
- network status
- I/O status
- version information

## Observability

The `observability/` layer supports traceability of the agent workflow.

Useful telemetry includes:

- requirements status
- architecture review status
- integration status
- safety hazards
- verification coverage
- failed tests
- cybersecurity findings
- logic-change status
- traceability gaps
- qualified approval
- governance blockers
- protected-action attempts

Observability supports engineering accountability but does not create operational authority.

## Memory and state

The `memory/` layer can preserve structured workflow context across agent stages.

State should distinguish requirements, design decisions, deterministic mappings, test evidence, hazards, model-generated recommendations, and qualified-human decisions.

Stale engineering state should not override the current machine configuration.

## Required reviews

The implemented safety policy requires all eight conditions:

```text
requirements_reviewed
controls_architecture_reviewed
integration_reviewed
verification_reviewed
functional_safety_reviewed
cybersecurity_reviewed
change_traceability_reviewed
qualified_engineering_approval
```

Missing any required review fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- automation requirements remain incomplete or inconsistent
- a safety interlock or protective-function gap remains unresolved
- verification or commissioning evidence is incomplete or failed
- unsafe coupling to live control remains unresolved
- industrial-control cybersecurity risk remains unresolved
- a PLC, robot, HMI, or control-logic change is unreviewed
- requirements, logic, test, or configuration traceability is incomplete
- an unsafe operating condition or process hazard remains unresolved
- any required review is missing
- qualified engineering approval is missing

The system should surface blockers rather than manufacturing production readiness.

## Protected actions

The safety policy permanently protects:

```text
deploy_control
change_safety_logic
write_live_controller
bypass_interlock
commission_cell
change_plc_logic
change_robot_program
change_operating_setpoint
```

These actions remain outside autonomous authority even when every review flag is satisfied.

## Human authority boundaries

F118 must not autonomously:

- deploy live control logic
- write to PLCs, robots, drives, HMIs, or safety controllers
- change safety logic
- bypass interlocks
- commission production equipment
- change PLC programs
- change robot programs
- change operating setpoints
- authorize equipment startup
- declare a cell safe for production
- accept failed verification evidence
- conceal unresolved hazards or cybersecurity risk

Final design, deployment, commissioning, safety, and operational authority remains with qualified engineers and authorized plant personnel.

## Qualified engineering approval

The final engineering package should be reviewed by personnel competent for the system and change being considered.

Depending on the application, this can include controls, electrical, robotics, process, mechanical, safety, cybersecurity, quality, manufacturing, maintenance, and operations expertise.

## Explicit failure states

Useful explicit states include:

```text
AUTOMATION REQUIREMENTS INCOMPLETE
CONTROLS ARCHITECTURE REVIEW INCOMPLETE
INTEGRATION REVIEW INCOMPLETE
SAFETY INTERLOCK GAP
VERIFICATION FAILED
COMMISSIONING EVIDENCE INCOMPLETE
LIVE CONTROL COUPLING RISK
INDUSTRIAL CYBERSECURITY RISK
CONTROL LOGIC CHANGE UNREVIEWED
TRACEABILITY GAP
UNSAFE OPERATING CONDITION
QUALIFIED ENGINEERING APPROVAL REQUIRED
CONTROL DEPLOYMENT PROHIBITED
SAFETY LOGIC CHANGE PROHIBITED
LIVE CONTROLLER WRITE PROHIBITED
INTERLOCK BYPASS PROHIBITED
CELL COMMISSIONING PROHIBITED
PLC LOGIC CHANGE PROHIBITED
ROBOT PROGRAM CHANGE PROHIBITED
OPERATING SETPOINT CHANGE PROHIBITED
```

F118 must never fabricate test results, I/O states, safety validation, controller versions, commissioning evidence, device capabilities, or human approvals.

## End-to-end reference workflow

A typical F118 workflow follows this sequence:

1. Define process, machine, performance, quality, operational, and safety requirements.
2. Review operating modes, states, sequences, alarms, fault handling, and recovery.
3. Define controls architecture and authority boundaries.
4. Build I/O and interface maps.
5. Review PLC, robot, HMI, drive, vision, MES, and subsystem integration.
6. Identify hazards, safe states, protective functions, and interlocks.
7. Develop requirement-based verification and commissioning tests.
8. Exercise fault conditions, restart behavior, communication loss, and safety trips.
9. Review industrial cybersecurity and access-control architecture.
10. Verify software, hardware, drawings, I/O, tests, and configuration traceability.
11. Assess all logic or configuration changes against the reviewed baseline.
12. Perform independent engineering readiness review.
13. Apply fail-closed governance gates.
14. Require explicit qualified-human engineering approval.
15. Keep deployment, live writes, safety changes, interlock bypasses, commissioning, PLC changes, robot changes, and setpoint changes outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test both engineering usefulness and governance behavior, including:

- requirements completeness
- controls architecture consistency
- I/O and interface traceability
- safety-interlock enforcement
- verification failure handling
- commissioning evidence
- live-control coupling risk
- industrial cybersecurity escalation
- unreviewed logic-change detection
- traceability enforcement
- qualified-human approval enforcement
- protected-action enforcement

The behavioral verification layer includes direct governance tests and a 10-scenario held-out factory-automation governance suite.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance behavior, held-out factory-automation scenarios, and execution of the governed reference workflow.

## Reproducibility

Install development dependencies:

```bash
python -m pip install -e .
```

Then run:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

Reproducibility also depends on preserving program, controller, robot, HMI, network, device, drawing, and test versions.

## Extension points

Organization-specific implementations can add governed integrations for:

- PLC development environments
- robot simulation environments
- HMI platforms
- SCADA systems
- MES systems
- industrial historians
- electrical CAD systems
- device configuration databases
- safety validation repositories
- CMMS systems
- asset registries
- virtual commissioning tools
- industrial cybersecurity platforms

Write-capable live-control integrations require additional safety, authorization, cybersecurity, rollback, validation, and change-control architecture beyond this reference implementation.

## Example applications

Potential governed uses include:

- automated machine cells
- robotic assembly
- packaging lines
- material-handling systems
- process skids
- automated inspection stations
- conveyor systems
- machine tending
- PLC/HMI modernization planning
- brownfield controls upgrades
- virtual commissioning preparation
- automation engineering training and simulation

F118 is not an autonomous plant controller, machine-safety authority, commissioning authority, production release system, or substitute for qualified controls and safety engineering judgment.

## Design principles

F118 follows these principles:

1. Define testable requirements before implementing automation logic.
2. Separate standard control from safety control and preserve authority boundaries.
3. Make I/O, interfaces, states, handshakes, and failure behavior explicit.
4. Verify both nominal and fault behavior against requirements.
5. Treat functional safety and industrial cybersecurity as first-class engineering concerns.
6. Preserve complete requirements, logic, configuration, and test traceability.
7. Re-review every material control, robot, HMI, or safety change.
8. Fail closed when verification, safety, cybersecurity, or traceability is incomplete.
9. Keep live-control writes, commissioning, safety changes, and physical authority under qualified human control.

## Scope statement

F118 demonstrates a governed multi-agent architecture for factory-automation engineering support. It combines specialized agents, deterministic I/O, interface, hazard, and test tools, functional-safety review, cybersecurity review, observability, evaluation, and fail-closed governance while maintaining strict separation between engineering analysis and operational control.

It is a reference implementation for governed factory-automation engineering, not a substitute for qualified controls, robotics, functional-safety, cybersecurity, commissioning, or operations judgment.