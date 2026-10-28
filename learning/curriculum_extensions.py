SUPPLEMENTAL_LESSONS = {
    "CYB-101": [
        (
            "Create an asset and trust-boundary map",
            "Use a fictional school enrollment service to distinguish valuable information, supporting services, people, and external dependencies. Mark where identities or records cross boundaries. Record assumptions and identify an owner for each asset before proposing safeguards.",
        ),
        (
            "Compare security controls and residual risk",
            "Compare a preventive safeguard with a detective and recovery safeguard for the same fictional risk. Explain which part of the risk each control reduces, what evidence would show it is working, and what harm could remain.",
        ),
        (
            "Develop a proportionate risk recommendation",
            "Prepare a one-page risk register for three fictional school information assets. Describe the affected asset, a plausible threat, relevant weakness, impact, current safeguards, owner, and next review date. Explain why your ranking reflects business priorities rather than technical novelty.",
        ),
        (
            "Foundations module portfolio assessment",
            "Review your glossary, asset map, and risk register as one portfolio. Check that facts, assumptions, and recommendations are clearly separated, that each proposed control has an accountable owner, and that your examples protect personal information. Write a short reflection on one security trade-off.",
        ),
    ],
    "CYB-102": [
        (
            "Trace the workstation boot and application lifecycle",
            "Create a conceptual diagram of a fictional workstation from power-on through operating-system services to an approved business application. Label storage, memory, identity, and service dependencies without inspecting or changing a real computer.",
        ),
        (
            "Plan a least-privilege endpoint configuration",
            "Given three fictional users and their job duties, create an access matrix for routine work and approved maintenance. Identify where a standard account is sufficient and where time-limited, documented administration is justified.",
        ),
        (
            "Design endpoint maintenance and recovery records",
            "Build a sample device record that includes an owner, business role, support status, update contact, backup responsibility, and recovery priority. Use a tabletop scenario to explain how staff should confirm an update and communicate a failed validation.",
        ),
        (
            "Systems module portfolio assessment",
            "Present your workstation lifecycle diagram, access matrix, and maintenance record as a proposed endpoint baseline. Identify two assumptions that need system-owner confirmation and define a safe, documented review before any production change.",
        ),
    ],
    "CYB-103": [
        (
            "Map a fictional campus network",
            "Draw a high-level map for a fictional campus with student, staff, learning, and administrative services. Identify network boundaries, service owners, approved communication needs, and important dependencies; do not use or probe a real network.",
        ),
        (
            "Build a normal-traffic reference table",
            "Create a synthetic table showing an approved source, destination, business purpose, service owner, and time window for five fictional communications. Explain what additional context an analyst would need before interpreting an unfamiliar event.",
        ),
        (
            "Evaluate network segmentation decisions",
            "For a paper case, compare two ways to separate administrative records from student learning services. Record the intended security benefit, operational dependencies, monitoring requirement, and change owner. Do not configure devices or create traffic.",
        ),
        (
            "Networking module portfolio assessment",
            "Submit your campus network diagram, normal-traffic table, and segmentation rationale together. A reviewer should be able to trace one approved business flow and see where an alert must be checked with an asset owner before action.",
        ),
    ],
    "CYB-104": [
        (
            "Review a sample user and group inventory",
            "Use a fictional account list to map each user to a role, approved group, manager, and review date. Identify shared, inactive, or unusually privileged entries as questions for the owner, not as permission to modify a real system.",
        ),
        (
            "Evaluate services against a change baseline",
            "Compare a paper example of a workstation's intended services with a fictional change record. Document the expected service owner, user impact, validation evidence, and rollback contact before recommending a review.",
        ),
        (
            "Draft a safe maintenance and logging plan",
            "Prepare a tabletop maintenance plan identifying the authorized administrator, maintenance window, user notice, backup or recovery check, relevant audit records, and post-change validation. Explain how access to the records should be controlled.",
        ),
        (
            "Administration module portfolio assessment",
            "Combine your access review, baseline comparison, and maintenance plan into an endpoint-administration handover. Separate verified sample facts from open questions and show how an approved change would be documented and reviewed.",
        ),
    ],
    "CYB-105": [
        (
            "Translate a security question into an algorithm",
            "Write pseudocode for checking a supplied list of synthetic training records for missing owners. Define input, expected output, edge cases, and a harmless test dataset. Review the logic with a peer before considering an implementation.",
        ),
        (
            "Validate and summarize a synthetic dataset",
            "Using instructor-provided sample rows, identify field meanings, missing values, duplicates, and inconsistent categories. Describe each cleaning decision and retain a short record explaining how it may affect the final summary.",
        ),
        (
            "Review automation for predictable behavior",
            "Create a small review checklist covering scope, input validation, error handling, privacy, output destination, logging, and peer review. Apply it to a fictional reporting script description; do not run it against live systems or real records.",
        ),
        (
            "Programming module portfolio assessment",
            "Submit your algorithm, data-quality observations, synthetic test cases, and review checklist. Demonstrate that another learner can reproduce your reasoning from the sample data and that no real personal information is required.",
        ),
    ],
    "CYB-106": [
        (
            "Document authorization and assessment scope",
            "Draft a mock authorization record for a supervised classroom exercise. Include the approving owner, written learning purpose, isolated assets, allowed dates, exclusions, contact, and stop procedure. Treat anything omitted from the scope as not authorized.",
        ),
        (
            "Apply privacy and data-minimization principles",
            "Sort fictional case details into information needed for a security decision and information that should not be collected or shared. Record the purpose, approved audience, storage location, and escalation route for any real privacy question.",
        ),
        (
            "Write a professional security report",
            "Turn a fictional observation into a concise report that separates evidence from inference, states the scope and limitations, avoids unnecessary personal details, and gives the accountable owner a clear next step.",
        ),
        (
            "Ethics and professional practice portfolio",
            "Review your mock authorization, privacy notes, and report using a peer checklist. Explain what you would do if permission changed, evidence was sensitive, or a request conflicted with an approved procedure. Refer legal questions to current official Kenyan sources and qualified advisers.",
        ),
    ],
    "CYB-201": [
        (
            "Build an accountability and policy map",
            "Map fictional board, risk-owner, system-owner, and operational responsibilities for one information service. Link policy requirements to a responsible role, approval path, review date, and communication method.",
        ),
        (
            "Practice consistent risk analysis",
            "Use a fictional business service to identify assets, plausible scenarios, safeguards, uncertainties, and business impact. Write assumptions explicitly and compare two treatment options with their owners and practical consequences.",
        ),
        (
            "Design a proportionate control-evidence plan",
            "For three fictional safeguards, specify what evidence would support their operation, its source, permitted access, sampling period, reviewer, and limitations. Do not collect actual employee or system records for the exercise.",
        ),
        (
            "Governance and assurance portfolio assessment",
            "Present a risk decision to a mock management audience with an accountable owner, treatment choice, evidence plan, and review date. Identify what the available evidence cannot prove and which decision remains with management.",
        ),
    ],
    "CYB-202": [
        (
            "Choose a cryptographic service for a use case",
            "For fictional scenarios, decide whether the need is confidentiality, integrity checking, proof of origin, or some combination. Explain what encryption, a hash, and a signature can and cannot establish.",
        ),
        (
            "Review a certificate and trust scenario",
            "Use a supplied fictional certificate summary to check its subject, issuer, validity period, intended use, and trust context. Record which details require confirmation through an approved trusted source.",
        ),
        (
            "Create a key-management lifecycle",
            "Diagram the approval, issue, access, rotation, backup, recovery, revocation, and retirement responsibilities for a fictional application key. Identify separation of duties and a secure route for reporting exposure.",
        ),
        (
            "Cryptography module portfolio assessment",
            "Recommend controls for a fictional record-sharing service. Match each security need to an appropriate cryptographic service and key owner, explain recovery constraints, and list assumptions that must be validated by the service team.",
        ),
    ],
    "CYB-203": [
        (
            "Map the joiner, mover, and leaver lifecycle",
            "Create a process map for a fictional staff member joining, changing teams, and leaving. Show who requests, approves, provisions, reviews, and removes access, including escalation when an approval or system owner is unavailable.",
        ),
        (
            "Conduct a role and entitlement review",
            "Review a synthetic access matrix against five fictional job descriptions. Flag unexplained access for owner review; document the business question, risk, and proposed next approver rather than changing entitlements.",
        ),
        (
            "Plan stronger authentication and account recovery",
            "Compare fictional user journeys for staff, administrators, and help-desk recovery. Document approved authentication requirements, accessible recovery, identity verification, and the warning that one-time codes must not be shared.",
        ),
        (
            "Identity module portfolio assessment",
            "Present an identity lifecycle and access-review plan with least-privilege roles, privileged-access safeguards, named decision owners, and a process for reviewing overdue exceptions.",
        ),
    ],
    "CYB-204": [
        (
            "Produce an approved network-flow specification",
            "For a fictional service, identify the initiating system, destination owner, business purpose, sensitivity, required service, monitoring contact, and review date. Mark unapproved or unclear paths for an authorized owner to resolve.",
        ),
        (
            "Review remote-access responsibilities",
            "Use a tabletop support case to map who requests remote access, which manager approves it, what approved gateway and identity requirements apply, when access expires, and who reviews the record.",
        ),
        (
            "Plan a reversible network change",
            "Draft a change request containing its purpose, affected services, business owner, impact assessment, approval, maintenance communication, rollback responsibility, and post-change validation. Do not apply configurations or interact with live equipment.",
        ),
        (
            "Network architecture portfolio assessment",
            "Submit an architecture diagram, flow specification, and change proposal. Show how a reviewer can trace each connection to an accountable service owner and identify the rollback and monitoring responsibilities.",
        ),
    ],
    "CYB-205": [
        (
            "Build an asset and baseline comparison",
            "Use a synthetic inventory and configuration statement to record asset owner, product, support status, approved baseline, observed difference, evidence source, and review date.",
        ),
        (
            "Prioritize a fictional vulnerability advisory",
            "Compare a supplied advisory with a synthetic asset record. Explain affected-product confidence, exposure, business importance, existing safeguards, vendor guidance, and the additional facts needed before assigning a priority.",
        ),
        (
            "Plan remediation, exception, and verification",
            "Create a paper change plan with an accountable service owner, approved window, user impact, recovery option, validation evidence, and exception expiry. Make clear that the learner has not changed or tested an actual device.",
        ),
        (
            "Vulnerability-management portfolio assessment",
            "Present a prioritized remediation queue and a sample decision record. Include owners, rationale, verification evidence, documented exceptions, and dates for reassessing changes in exposure.",
        ),
    ],
    "CYB-206": [
        (
            "Classify a fictional dataset",
            "Assign sample record groups a proposed classification, business purpose, owner, approved audience, retention consideration, and handling rule. Explain which classification decisions need confirmation from a privacy or records specialist.",
        ),
        (
            "Create a database access responsibility matrix",
            "Map fictional application, analyst, and administrator roles to the minimum data operations each needs. Identify an owner and approval for each role and record how sensitive access would be reviewed.",
        ),
        (
            "Plan protected retention and recovery",
            "Draft a paper schedule for a synthetic database including retention, backup responsibility, access restrictions, recovery objective, restoration approver, and deletion review. Do not use real records or initiate a restoration.",
        ),
        (
            "Database and data-protection portfolio assessment",
            "Present a data-flow diagram, classification register, and recovery outline. Describe which safeguards protect confidentiality, integrity, availability, and privacy throughout the record lifecycle.",
        ),
    ],
    "CYB-301": [
        (
            "Map a defensive logging coverage plan",
            "For a fictional service, list relevant identity, endpoint, application, and administrative event sources, their owner, approved retention, time-synchronization dependency, and known monitoring gap.",
        ),
        (
            "Triage a synthetic alert without overclaiming",
            "Review a provided fictional alert timeline and separate reported event fields, corroborated facts, hypotheses, and missing evidence. Identify appropriate next owners and a proportionate escalation path.",
        ),
        (
            "Improve alert quality and analyst handover",
            "Use mock case examples to propose clearer alert context, ownership, severity rationale, and an approved review date. Create a shift-handover note that records status, evidence location, open questions, and next action.",
        ),
        (
            "Security operations module assessment",
            "Complete a tabletop case from alert receipt through handover. Submit the triage record, evidence list, uncertainty statement, escalation rationale, and suggested monitoring improvement using fictional events only.",
        ),
    ],
    "CYB-302": [
        (
            "Write an incident declaration and contact tree",
            "For a fictional organization, map the incident lead, service owner, security contact, privacy adviser, communications contact, and management decision-maker. Define what evidence supports escalation and which roles may declare an incident.",
        ),
        (
            "Compare containment choices with business impact",
            "Use a tabletop service disruption to compare two documented containment options. Identify decision authority, user impact, evidence concerns, communication needs, and the condition that would trigger escalation.",
        ),
        (
            "Design an incident timeline and recovery checklist",
            "Record fictional observations with time zone, source, confidence, decision owner, and follow-up. Propose recovery verification and an after-action review with measurable improvement owners.",
        ),
        (
            "Incident response tabletop assessment",
            "Facilitate a paper exercise from initial report to review. Submit roles, decision log, communication timeline, recovery checks, and three assigned improvements. Do not perform containment actions on real systems.",
        ),
    ],
    "CYB-303": [
        (
            "Establish forensic readiness responsibilities",
            "Map fictional authority, scope, custodian, records retention, approved collection role, privacy review, and escalation contacts. Identify what a responder should do when instructions or authority are incomplete.",
        ),
        (
            "Review a synthetic custody record",
            "Inspect an instructor-provided paper chain-of-custody form. Identify missing identifiers, dates, transfer reasons, signatures, storage location, and unresolved gaps without handling actual devices or evidence.",
        ),
        (
            "Build a time-aware evidence timeline",
            "Place fictional observations on a timeline with source, recorded time zone, reliability, and corroboration status. Explain how clock differences or missing records affect interpretation.",
        ),
        (
            "Digital-forensics report assessment",
            "Prepare an evidence-handling summary that states authorization, sample limitations, confirmed facts, hypotheses, custody gaps, and appropriate next owner. Avoid claiming a fictional artifact proves more than it shows.",
        ),
    ],
    "CYB-304": [
        (
            "Create secure software requirements",
            "For a fictional learning portal, write testable requirements for identity, authorization, privacy, audit, data retention, error handling, and recovery. Trace each requirement to a named business or security owner.",
        ),
        (
            "Run a paper threat-model review",
            "Draw a high-level data-flow diagram for a fictional application, identify trust boundaries and important assets, and record plausible abuse cases with proportionate safeguards. This is a design discussion, not a test of a deployed service.",
        ),
        (
            "Plan dependency and release assurance",
            "Build a mock dependency ownership table, approved update path, review gate, release approver, and recovery plan. Define what the team should do if a test detects a problem after a release.",
        ),
        (
            "Secure-development portfolio assessment",
            "Present a traceable design package with requirements, threat assumptions, review responsibilities, dependency process, safe test plan, and maintenance ownership. Clearly distinguish proposed controls from verified implementation.",
        ),
    ],
    "CYB-305": [
        (
            "Map a fictional web-application trust boundary",
            "Diagram a browser, application service, identity provider, and data store. Mark where identity and data cross boundaries, who owns each component, and what assumptions require review.",
        ),
        (
            "Review an API authorization matrix",
            "For fictional API roles and records, document which named role may perform each business action and access each data category. Identify overbroad access as a design question for the owner, not a request to test a live endpoint.",
        ),
        (
            "Plan privacy-aware error and logging behavior",
            "Compare sample generic user-facing errors with a protected diagnostic record. Specify which support information is useful, who may view it, how long it is retained, and what sensitive details must not be logged.",
        ),
        (
            "Application-security design assessment",
            "Review a fictional design using trust boundaries, role-to-action mapping, sensitive-data handling, and accountable error logging. Submit prioritized recommendations with owners and approval checkpoints before release.",
        ),
    ],
    "CYB-306": [
        (
            "Build a shared-responsibility matrix",
            "For fictional infrastructure, platform, and software services, list which provider or customer role owns each security activity. Mark contract and service documentation that must be consulted before assigning responsibility.",
        ),
        (
            "Review cloud identity and ownership records",
            "Use a synthetic cloud-account inventory to associate workload, environment, named owner, access approver, logging contact, backup responsibility, and retirement date. Flag unclear access for the accountable owner.",
        ),
        (
            "Plan a controlled workload lifecycle",
            "Create a non-executable lifecycle plan for a fictional virtual workload: approved base image, dependency ownership, review, deployment approval, monitoring, recovery, update responsibility, and retirement.",
        ),
        (
            "Cloud and platform portfolio assessment",
            "Present a shared-responsibility matrix and fictional workload diagram. Explain where identity, configuration, logs, recovery, and supplier dependencies require accountable owners and evidence.",
        ),
    ],
    "CYB-401": [
        (
            "Evaluate threat-report source quality",
            "Compare two fictional intelligence notes by source, collection date, confidence, evidence, relevance, sharing restrictions, and known gaps. Explain whether each supports a decision or requires corroboration.",
        ),
        (
            "Plan safe suspicious-file reporting",
            "Create a reporting checklist for an unexpected file: preserve the message context, avoid opening or forwarding it, identify the approved channel, and record the affected owner without transferring the file to personal tools.",
        ),
        (
            "Translate intelligence into defensive decisions",
            "For a fictional advisory, identify who should validate whether the organization is affected, what information is permitted to share, how uncertainty should be reported, and which owner may approve a protective change.",
        ),
        (
            "Threat-intelligence portfolio assessment",
            "Prepare an intelligence brief from fictional sources. Include confidence and age, organizational relevance, handling restrictions, defensive recommendation, evidence gap, and a review date.",
        ),
    ],
    "CYB-402": [
        (
            "Write authorization and rules of engagement",
            "Draft written boundaries for an isolated training assessment: named approving owner, authorized assets, exclusions, dates, safety constraints, permitted data, contact, and stop conditions. Never substitute assumed permission for written authorization.",
        ),
        (
            "Design a safe evidence and reporting workflow",
            "Plan who records assessment observations, how evidence is minimized and protected, who receives findings, and how the team distinguishes reproducible observations from assumptions.",
        ),
        (
            "Prioritize remediation and retesting decisions",
            "For fictional findings, document scope, business impact, priority rationale, owner, remediation evidence, and conditions for authorized follow-up. A retest needs explicit approval and an agreed scope.",
        ),
        (
            "Authorized-assessment tabletop",
            "Review a paper engagement where scope, schedule, and safety instructions are available. Decide how to handle an unlisted asset, paused approval, and sensitive observation. Submit the decision log and escalation record; do not test a real system.",
        ),
    ],
    "CYB-403": [
        (
            "Plan an objective assurance engagement",
            "Write a fictional scope statement covering purpose, criteria, period, owners, exclusions, approval, confidentiality, and reporting dates. Identify which questions require agreement before evidence collection.",
        ),
        (
            "Assess evidence quality and sample limits",
            "Compare synthetic interview notes, one policy, and a small dated sample. Record relevance, source, coverage, reliability, corroboration, and what cannot be inferred from that sample.",
        ),
        (
            "Write a fair finding and action plan",
            "Translate a fictional control gap into criterion, condition, evidence, business impact, and corrective action. Confirm facts with an owner, preserve independent assessment, and set a validation date.",
        ),
        (
            "Assurance reporting portfolio assessment",
            "Present a concise fictional report with criteria, evidence limits, appropriately qualified conclusions, and traceable actions. Distinguish an improvement opportunity from a proven nonconformity.",
        ),
    ],
    "CYB-404": [
        (
            "Complete a fictional business-impact analysis",
            "For a fictional school registration service, identify critical processes, service owners, dependencies, outage consequences, seasonal demand, and recovery priorities. Ask owners to validate assumptions.",
        ),
        (
            "Design a recovery dependency map",
            "Map staff, facilities, approved providers, identity, records, connectivity, and communication dependencies for a fictional essential service. Identify which must recover first and who can approve the decision.",
        ),
        (
            "Create a tabletop exercise and evaluation",
            "Design a paper exercise with clear objectives, participants, injects, safety boundaries, decision records, observer notes, and actions. Do not interrupt a real service or test production recovery.",
        ),
        (
            "Resilience portfolio assessment",
            "Present an impact analysis, recovery dependency map, role list, exercise evaluation criteria, and improvement plan. Explain how owners will verify recovery objectives through an approved non-production exercise.",
        ),
    ],
    "CYB-405": [
        (
            "Create an IoT asset and supplier register",
            "Use fictional connected devices to record owner, purpose, location, support status, update contact, network dependency, privacy considerations, and safe retirement plan.",
        ),
        (
            "Review mobile management and privacy choices",
            "Compare fictional managed-device cases and document the work need, employee notice, authorized administrator, data separation, approval, recovery path, and potential impact of a remote action.",
        ),
        (
            "Coordinate a safety-aware operational change",
            "Plan a tabletop discussion among facilities, engineering, safety, IT, supplier, and security owners. Identify hazard review, authorized change window, rollback authority, and continuity procedures.",
        ),
        (
            "Connected-technology portfolio assessment",
            "Submit an asset register and a cross-team risk proposal for a fictional unsupported device. Compare replacement, documented isolation, and monitoring options with service owner and safety review.",
        ),
    ],
    "CYB-406": [
        (
            "Agree on a scoped capstone proposal",
            "Write a one-page proposal stating the defensive learning question, supervisor, learning outcomes, synthetic sources, explicit exclusions, approval checkpoints, milestones, and safe stop conditions.",
        ),
        (
            "Develop a traceable project evidence pack",
            "Create a project record that links approved sources to observations, assumptions, requirements, decisions, owners, and review dates. Protect source material and exclude personal data from the learning environment.",
        ),
        (
            "Practice a peer and supervisor review",
            "Ask a reviewer to challenge the project's scope, evidence, privacy choices, accessibility, assumptions, and recommended safeguards. Record feedback, decisions, and changes with dates and owners.",
        ),
        (
            "Present and reflect on a defensive capstone",
            "Deliver a concise portfolio presentation explaining the approved problem, evidence, design choices, limitations, proposed safeguards, validation plan, and remaining questions. Include a reflection on professional boundaries and next learning goals.",
        ),
    ],
}
