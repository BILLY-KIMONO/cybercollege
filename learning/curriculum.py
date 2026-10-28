def article(title, content):
    return {
        "title": title,
        "lesson_type": "article",
        "content": content,
        "duration": "5 hours",
    }


def scenario(title, content, challenge_prompt, expected_answer):
    return {
        "title": title,
        "lesson_type": "lab",
        "content": content,
        "challenge_prompt": challenge_prompt,
        "expected_answer": expected_answer,
        "duration": "5 hours",
    }


DIPLOMA_MODULES = [
    {
        "module_code": "CYB-101",
        "semester": 1,
        "title": "Cybersecurity Principles and Foundations",
        "slug": "cybersecurity-principles-foundations",
        "category": "Security fundamentals",
        "summary": "Build the vocabulary and security mindset used throughout a defender's career.",
        "description": "A first module in the diploma-style pathway. Study core security objectives, assets, threats, risk, layered defense, and the responsibilities shared by people who protect information.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "◈",
        "lessons": [
            article("Security goals and the CIA triad", "Confidentiality limits information to people with a legitimate need; integrity helps ensure it remains accurate and complete; availability keeps it accessible when needed. Security decisions balance all three goals. For example, an emergency service needs both controlled access to patient records and reliable access during an incident."),
            article("Assets, threats, vulnerabilities, and risk", "An asset is something valuable to protect. A threat could cause harm; a vulnerability is a weakness that could be used or triggered; and risk describes the chance and consequences of that harm. Distinguish these terms before recommending safeguards. A risk assessment helps an organization prioritize improvements rather than react to headlines."),
            article("Layered defense and security ownership", "Effective programs combine preventive, detective, and recovery safeguards across people, processes, and technology. No single control is perfect, so layers should complement each other. Every team member has a role: follow approved procedures, protect information, and promptly report concerns to the right team."),
            scenario("Choose a first response", "A team member notices that a shared project folder contains information available to more colleagues than expected. There is no evidence yet that the information was copied.", "What is the safest first step?", "Report the access concern to the data owner or security team and preserve the existing access details"),
        ],
    },
    {
        "module_code": "CYB-102",
        "semester": 1,
        "title": "Computer Systems and Operating Systems",
        "slug": "computer-systems-operating-systems",
        "category": "Systems administration",
        "summary": "Understand endpoints, operating systems, accounts, updates, and system logs.",
        "description": "Learn how computer hardware, operating systems, users, and processes fit together. Build a safe foundation for administering and defending the computers organizations rely on.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "▣",
        "lessons": [
            article("How a computer processes information", "Processors execute instructions, memory holds working data, storage retains information, and peripherals provide input and output. Operating systems coordinate these resources and applications. Knowing these boundaries helps defenders understand where data resides, which services are essential, and why device inventories matter."),
            article("Accounts, permissions, processes, and services", "An operating system assigns identities and permissions, starts application processes, and manages background services. Each process should receive only the access it needs. Document approved administrative accounts, review unnecessary services through established procedures, and avoid using shared privileged accounts."),
            article("Updates, backups, and endpoint records", "Operating-system and application updates address known defects and improve supportability. Apply them through approved change management, validate important applications afterward, and keep recovery options current. Accurate asset records identify each device's owner, role, support status, and update responsibility."),
            scenario("Handle an overdue update", "An inventory review finds an organization-managed laptop missing an important operating-system update. The device supports a critical business task.", "What should the administrator do first?", "Confirm the device and update status, then schedule the approved update and validation with its owner"),
        ],
    },
    {
        "module_code": "CYB-103",
        "semester": 1,
        "title": "Networking Fundamentals",
        "slug": "networking-fundamentals",
        "category": "Network defense",
        "summary": "Learn network layers, addressing, name resolution, routing, and normal traffic flows.",
        "description": "Build a practical conceptual understanding of how devices communicate. Study common network services and learn why diagrams, inventories, and documented traffic expectations support defenders.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "⌁",
        "lessons": [
            article("Network models and data flow", "Network models describe how applications, transport, addressing, and physical links work together. Encapsulation wraps information in the headers needed to move it between systems. A defender who can trace a legitimate business flow can better evaluate a monitoring alert without assuming that unfamiliar traffic is malicious."),
            article("Addresses, routing, and name services", "Addresses identify endpoints on a network; routers forward traffic between networks; and name-resolution services help applications locate destinations. Network diagrams should identify approved address ranges and critical dependencies. Record changes through established procedures so monitoring teams know which activity is expected."),
            article("Common services and network visibility", "Organizations depend on services such as address assignment, name resolution, web access, and time synchronization. Firewalls and monitoring systems enforce and record approved flows. Understand what each control can and cannot tell you, and protect the integrity and access to network logs."),
            scenario("Investigate an unknown device", "A network-monitoring report shows a previously unrecorded device connected to a staff network during a scheduled office move.", "What should the network team do first?", "Check the approved device inventory and change record with the responsible network team"),
        ],
    },
    {
        "module_code": "CYB-104",
        "semester": 1,
        "title": "Linux and Windows Administration for Defenders",
        "slug": "linux-windows-administration-defenders",
        "category": "Systems administration",
        "summary": "Understand system administration, accounts, updates, services, and audit records.",
        "description": "Compare the administrative concepts found on Linux and Windows endpoints. Practice a documented, least-privilege approach to routine maintenance, configuration review, and support.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "▤",
        "lessons": [
            article("Users, groups, and least privilege", "Both Linux and Windows systems use identities and group membership to control access. Give users standard accounts for routine work and reserve documented administrative access for approved tasks. Review permissions with system owners and retain records of who approved changes."),
            article("Services, scheduled work, and configuration", "Services and scheduled tasks support routine business functions but also add maintenance responsibilities. Know who owns each service and why it runs. Compare important settings with the organization's approved configuration baseline; report unexplained differences instead of changing systems without authorization."),
            article("Audit records and safe maintenance", "System event records help administrators explain account changes, service failures, updates, and other operational events. Follow retention and access rules, use approved maintenance windows, and document who performed a change, what was changed, and how the team confirmed normal operation."),
            scenario("Review a privileged account request", "A team member requests permanent administrator access because it would make occasional software updates more convenient.", "What is the most appropriate response?", "Confirm the business need and request time-limited, approved access using the organization's procedure"),
        ],
    },
    {
        "module_code": "CYB-105",
        "semester": 1,
        "title": "Programming and Data Foundations for Cybersecurity",
        "slug": "programming-data-foundations-cybersecurity",
        "category": "Programming and analysis",
        "summary": "Build the logic and data literacy needed to work safely with defensive information.",
        "description": "Study variables, conditions, repetition, data formats, and basic query concepts using synthetic learning examples. Emphasize review, reproducibility, and safe handling of data over automating actions on live systems.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "{ }",
        "lessons": [
            article("Algorithms, variables, and control flow", "An algorithm is a finite sequence of clear steps. Variables hold values, conditions choose between cases, and repetition processes a collection of items. Learn to describe expected inputs and outputs before implementing a task, and ask another person to review logic that could affect business data."),
            article("Structured data and validation", "Tabular data consists of named fields and records; common exchange formats also represent lists and nested values. Validate assumptions about data type, missing values, encoding, and duplicates before drawing conclusions. Work on approved synthetic or sanitized examples rather than copying sensitive records into personal tools."),
            article("Reproducible, reviewable automation", "A useful defensive utility has a narrow purpose, clear inputs, predictable outputs, and documented limitations. Test it against harmless sample data, preserve the original source, and request appropriate code review. Do not execute unreviewed automation on organization systems."),
            scenario("Select a safe dataset", "A learner wants to build a simple inventory report and has access to a shared folder containing both synthetic records and real customer exports.", "Which dataset should they use for the practice exercise?", "Use the supplied synthetic records and keep customer exports in their approved protected location"),
        ],
    },
    {
        "module_code": "CYB-106",
        "semester": 1,
        "title": "Cyber Ethics, Communication, and Kenyan Legal Context",
        "slug": "cyber-ethics-communication-kenyan-legal-context",
        "category": "Law, ethics and professionalism",
        "summary": "Apply authorization, responsible communication, privacy, and professional judgment.",
        "description": "Explore consent, confidentiality, responsible disclosure, and clear incident reporting in an educational setting. Use current official Kenyan legal sources and organizational policy for legal questions; this module is educational, not legal advice.",
        "level": "Beginner",
        "duration": "40 hours",
        "icon": "§",
        "lessons": [
            article("Permission, scope, and professional boundaries", "Security knowledge does not imply permission to examine someone else's device, account, or network. A legitimate assessment requires explicit authorization, written boundaries, a named contact, an agreed schedule, and a stop procedure. When permission or scope is unclear, stop and ask the accountable owner."),
            article("Privacy, confidentiality, and Kenyan context", "Handle personal information only for an authorized purpose and share it with approved recipients. In Kenya, consult official sources such as the Kenya Law Reports and the Office of the Data Protection Commissioner for current statutes and guidance. Policies and laws can change; escalate interpretations to qualified legal or privacy professionals."),
            article("Clear reports and responsible disclosure", "A useful report separates verified observations from assumptions, gives dates and context, describes potential impact, and recommends an accountable next step. Store it in approved systems with appropriate access controls. Raise suspected weaknesses privately through an authorized reporting route rather than publishing sensitive details."),
            scenario("Pause before an unapproved test", "A student recognizes a public website in an assignment and wants to confirm whether a concern they have heard about is real.", "What should the student do?", "Do not test the public website and ask the instructor for an explicitly authorized learning environment"),
        ],
    },
    {
        "module_code": "CYB-201",
        "semester": 2,
        "title": "Security Governance, Risk, and Compliance",
        "slug": "security-governance-risk-compliance",
        "category": "Governance, risk and compliance",
        "summary": "Connect security objectives to ownership, risk decisions, policies, and evidence.",
        "description": "Learn how organizations set security direction, assign accountability, assess risks, maintain policy, and demonstrate control operation. Connect technical recommendations to business priorities and documented decisions.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "◫",
        "lessons": [
            article("Governance and security ownership", "Governance establishes who can make security decisions, how exceptions are approved, and how progress is reviewed. Policies explain required outcomes; standards and procedures make them actionable. Named owners, review dates, version history, and staff communication make documents useful in everyday work."),
            article("Risk assessment and treatment", "A risk record describes an asset, a plausible threat, relevant weaknesses, potential consequences, existing safeguards, and uncertainty. Owners can reduce, transfer, avoid, or explicitly accept risk through an accountable process. Rank recommendations by impact and practical feasibility, and revisit decisions as conditions change."),
            article("Control evidence and compliance", "A control describes a safeguard and its intended purpose. Evidence such as an approved policy, access review record, or change ticket can show how that safeguard operated during a particular period. Collect only authorized evidence, record its source and date, and do not claim that a single document proves complete compliance."),
            scenario("Escalate a risk exception", "A project manager asks a security analyst to mark an unreviewed exception as approved so a launch date will not change.", "What should the analyst do?", "Document the request and route it to the designated risk owner for a formal decision"),
        ],
    },
    {
        "module_code": "CYB-202",
        "semester": 2,
        "title": "Applied Cryptography and Public Key Infrastructure",
        "slug": "applied-cryptography-public-key-infrastructure",
        "category": "Cryptography and data protection",
        "summary": "Understand encryption, hashing, digital signatures, certificates, and key custody.",
        "description": "Learn what common cryptographic services can and cannot guarantee. Study certificate trust, encryption in transit and at rest, and the operational care needed to manage keys throughout their lifetime.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "⌑",
        "lessons": [
            article("Encryption, hashing, and signatures", "Encryption uses a key to make data unreadable to unauthorized parties; decryption restores it for an authorized recipient. A cryptographic hash is a fixed-length digest used to check data integrity, not to recover the input. Digital signatures help verify origin and integrity when keys and verification processes are trustworthy."),
            article("Certificates and trust chains", "A certificate binds a public key to an identity under an issuing authority's stated procedures. Browsers and other clients validate relevant certificates against configured trust anchors and validity conditions. A certificate does not itself prove that a website or message is honest; users must also check context and intended identity."),
            article("Key lifecycle and recovery", "Cryptographic protection depends on keys remaining available to authorized people and unavailable to others. Organizations should restrict key access, document issuance and rotation, store backups securely, and plan recovery and revocation. Test recovery procedures without exposing production secrets in training or support records."),
            scenario("Respond to an exposed test key", "A learner finds a test signing key included in a public class repository. The repository description says it is for a simulated exercise.", "What should the learner do first?", "Report the exposed key to the instructor and repository owner without reusing or sharing it"),
        ],
    },
    {
        "module_code": "CYB-203",
        "semester": 2,
        "title": "Identity and Access Management",
        "slug": "identity-and-access-management",
        "category": "Identity and access management",
        "summary": "Manage the full identity lifecycle using least privilege and accountable access.",
        "description": "Explore authentication, authorization, joiner-mover-leaver processes, multifactor authentication, privileged access, and access reviews. Put identity owners and reliable approval records at the center of access decisions.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "◎",
        "lessons": [
            article("Authentication and authorization", "Authentication asks who or what is requesting access; authorization determines what that identity may do. Access decisions should follow the person's role and business need. Strong authentication cannot compensate for excessive permissions, so teams must review both identity proofing and assigned privileges."),
            article("The identity lifecycle and account reviews", "Joiner-mover-leaver procedures provide a consistent way to request, approve, change, and remove access when someone's role changes. Application owners confirm business need; identity teams record approvals and complete changes. Periodic reviews help find stale, duplicate, or unexpectedly privileged accounts."),
            article("Multifactor and privileged access", "Multifactor authentication combines different types of evidence, such as a memorized secret and a separate possession factor. Privileged accounts need additional care: minimize their membership, protect sign-in, document use, and provide controlled recovery. Never send one-time codes to a person requesting them over an unverified channel."),
            scenario("Handle an unexpected code request", "A caller claiming to be from the help desk asks an employee to read out a multifactor authentication code to prevent an account lockout.", "What should the employee do?", "Do not share the code; verify the request through the organization's official help-desk channel"),
        ],
    },
    {
        "module_code": "CYB-204",
        "semester": 2,
        "title": "Secure Network Architecture and Administration",
        "slug": "secure-network-architecture-administration",
        "category": "Network defense",
        "summary": "Design understandable network boundaries, resilient services, and controlled changes.",
        "description": "Study segmentation, documented data flows, network-device administration, firewall rule ownership, remote access, and resilience. Emphasize approved change management and clear diagrams over ad hoc configuration.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "⌁",
        "lessons": [
            article("Segmentation and architecture", "Network architecture groups systems according to sensitivity, purpose, and required communication. Segmentation can limit unnecessary paths and make monitoring clearer, but it does not replace endpoint security or identity checks. Maintain current diagrams and confirm business dependencies before changing boundaries."),
            article("Controlled connectivity and remote access", "A documented network rule should have an owner, an operational purpose, approved endpoints or services, and a review date. Remote administration should use approved protected pathways and appropriate multifactor authentication. Remove expired access through the normal change process after verifying that owners no longer need it."),
            article("Resilience and network changes", "Reliable network services depend on tested backups, recovery plans, current device inventories, and support contacts. Plan a change's impact and rollback before implementation; monitor after approved changes and record the results. Rehearsals use a controlled practice environment instead of production traffic."),
            scenario("Review an undocumented firewall exception", "A service owner asks that a broad, temporary network exception remain in place because the application appears to work better with it.", "What is the safest next action?", "Ask the network and application owners to document the dependency and review a narrowly scoped, time-limited change"),
        ],
    },
    {
        "module_code": "CYB-205",
        "semester": 2,
        "title": "Secure Configuration and Vulnerability Management",
        "slug": "secure-configuration-vulnerability-management",
        "category": "Vulnerability and configuration management",
        "summary": "Establish baselines, prioritize disclosed issues, and verify remediation safely.",
        "description": "Learn asset inventory, secure configuration baselines, vulnerability disclosure, practical prioritization, patch coordination, exception handling, and verification. Focus on authorized sources and changes reviewed by service owners.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "◉",
        "lessons": [
            article("Assets and secure configuration baselines", "You cannot reliably protect systems you do not know exist. Record an asset's owner, purpose, location, support status, and business importance. A secure baseline documents approved settings, exceptions, and evidence so teams can compare managed devices consistently."),
            article("Understanding and prioritizing advisories", "A vulnerability advisory describes an affected product, known conditions, and sometimes mitigations. Evaluate whether the organization actually uses an affected version, what exposure and business impact exist, and which compensating controls are present. A severity score is useful context, not a complete prioritization decision."),
            article("Remediation and verification", "Plan an update or configuration change with the service owner, dependency checks, backup or recovery steps, approval, and a maintenance window where needed. Verify the approved result and update the tracking record. If a fix cannot be applied, record an accountable exception and interim safeguards with a review date."),
            scenario("Prioritize an unknown advisory", "A vendor publishes an urgent advisory, but the asset inventory does not show whether affected products are in use.", "What should the response team do first?", "Identify and validate affected assets with owners using approved inventory and vendor information"),
        ],
    },
    {
        "module_code": "CYB-206",
        "semester": 2,
        "title": "Database Security and Data Protection",
        "slug": "database-security-data-protection",
        "category": "Data protection and privacy",
        "summary": "Protect structured information with controlled access, good stewardship, and recovery.",
        "description": "Study database roles, data classification, secure handling, backups, retention, privacy, and auditability. Learn how to keep sensitive information out of test environments and make its access accountable.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "▤",
        "lessons": [
            article("Data classification and stewardship", "Classify information according to its sensitivity, legal and contractual obligations, intended use, and potential impact if lost. Assign a data owner and a custodian who applies approved safeguards. Use the organization's classification labels and handling rules consistently across approved systems."),
            article("Database access and accountable changes", "Give applications and staff only the database permissions required for their documented work. Separate duties for important administrative tasks and maintain accountable records of material changes. Protect backups and service credentials, and use approved procedures when modifying shared records."),
            article("Retention, deletion, and recovery", "Retention schedules describe how long an organization should keep information and what to do when that period ends. Backups should be protected and recovery tested against service priorities. Coordinate deletion and restoration decisions with data owners, privacy staff, and recordkeeping obligations."),
            scenario("Prepare a dataset for class", "An instructor requests real learner records to make a demonstration database look realistic.", "What is the safer alternative?", "Use synthetic sample records and keep actual learner information in its approved system"),
        ],
    },
    {
        "module_code": "CYB-301",
        "semester": 3,
        "title": "Security Operations Centre and SIEM Operations",
        "slug": "security-operations-centre-siem-operations",
        "category": "Security operations",
        "summary": "Turn approved logs and alerts into consistent, evidence-led triage decisions.",
        "description": "Explore monitoring objectives, log sources, alert queues, SIEM concepts, triage, escalation, tuning, and shift handover. Work with fictional event descriptions; do not connect exercises to live organizational logs.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "⌘",
        "lessons": [
            article("Logs, telemetry, and monitoring coverage", "A log records events observed by a system, while telemetry can also include operational measurements. Useful monitoring depends on appropriate source coverage, accurate timestamps, consistent retention, and authorized access. Draw a coverage map so analysts know what a particular alert can and cannot establish."),
            article("SIEM concepts and alert triage", "A security information and event management system collects and correlates approved event sources to support investigation. An alert is a lead to assess, not proof by itself. Analysts validate the reporting system, time period, affected asset, known business context, and supporting evidence before assigning a priority."),
            article("Escalation, documentation, and shift handover", "A useful case record links observations to their sources, distinguishes confirmed facts from hypotheses, and lists open questions and next owners. Follow escalation criteria and privacy rules. A structured handover records urgency, actions already taken, evidence locations, and the next review time."),
            scenario("Assess an unusual sign-in", "A training SIEM shows a sign-in from a new location. The exercise data does not show whether the user was traveling or using a managed service.", "What should the analyst do first?", "Validate the event with the authorized identity owner and supporting training records before escalating its severity"),
        ],
    },
    {
        "module_code": "CYB-302",
        "semester": 3,
        "title": "Incident Response and Crisis Coordination",
        "slug": "incident-response-crisis-coordination",
        "category": "Incident response",
        "summary": "Plan, document, contain, and communicate incidents using an approved playbook.",
        "description": "Practice preparation, identification, triage, escalation, containment planning, recovery, and learning reviews. Tabletop simulations teach sound decisions without changing a real device or interrupting a real service.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⌕",
        "lessons": [
            article("Preparation, roles, and incident declarations", "Preparation defines response roles, contact paths, decision authority, communication channels, and service priorities before an event occurs. Teams should have documented criteria for declaring an incident and raising its priority. Rehearse escalation so staff know how to reach a human decision-maker."),
            article("Triage, containment, and coordination", "Responders validate what happened, assess the scope and business impact, and document decisions. Containment must balance harm reduction with safety, evidence requirements, contractual duties, and service continuity. Authorized owners make disruptive decisions with appropriate specialists following the incident playbook."),
            article("Recovery and after-action learning", "Recovery returns services using approved, known-good procedures and additional monitoring as directed by responsible teams. Preserve a clear incident timeline, record communications, and capture lessons without blame. Assign each improvement an owner, due date, and a way to verify completion."),
            scenario("Protect a potentially affected endpoint", "A staff member reports unexpected files on a work laptop during a possible security incident. The laptop is still connected to an essential business service.", "What should the learner do next?", "Contact the incident lead and follow the approved containment and evidence-preservation playbook"),
        ],
    },
    {
        "module_code": "CYB-303",
        "semester": 3,
        "title": "Digital Forensics and Evidence Handling",
        "slug": "digital-forensics-evidence-handling",
        "category": "Digital forensics",
        "summary": "Protect evidence integrity through authorization, documentation, custody, and sound reasoning.",
        "description": "Study forensic readiness, scope, preservation, chain of custody, timelines, and communication of limitations. Learner activities use fictional records rather than collecting evidence from real devices.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⌕",
        "lessons": [
            article("Forensic readiness and authority", "Forensic readiness helps an organization identify who may request an examination, what may be collected, how records are protected, and whom to involve. Work within written authority, jurisdiction, privacy requirements, and retention rules. If scope is uncertain, stop and obtain direction before examining evidence."),
            article("Preservation and chain of custody", "Evidence-handling records identify what was collected, who had custody, when each transfer occurred, where an approved item was stored, and why an action was taken. Preserve context and avoid unnecessary changes. Only qualified personnel should perform examination or collection under approved procedures."),
            article("Timelines and limitations", "A defensible timeline draws from identified sources with recorded time zones and reliability limitations. Separate what the record shows from possible explanations, note gaps, and corroborate important points where authorized. Reports should explain methodology and limitations in language the intended audience can understand."),
            scenario("Document a reported device", "A responder receives an unsealed storage device with no accompanying collection record and a request to examine it immediately.", "What should the responder do first?", "Secure the item as directed by procedure and contact the evidence custodian to establish authority and document custody"),
        ],
    },
    {
        "module_code": "CYB-304",
        "semester": 3,
        "title": "Secure Software Development and DevSecOps",
        "slug": "secure-software-development-devsecops",
        "category": "Secure software development",
        "summary": "Build security into requirements, design, code review, release, and maintenance.",
        "description": "Follow a secure software development lifecycle: define requirements, review threats, protect development assets, test safely, manage dependencies, and maintain releases. Use authorized repositories and review processes throughout.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "</>",
        "lessons": [
            article("Security requirements and threat modelling", "Record security requirements alongside user and service requirements, including data classification, access boundaries, recovery, and audit needs. Threat modelling asks what matters, how information flows, what could go wrong, and which safeguards are appropriate. Record assumptions and re-evaluate them when architecture changes."),
            article("Code review, dependencies, and secrets", "Code review checks that changes match their intent and do not introduce undocumented access or data-handling behavior. Maintain a dependency inventory, track vendor advisories, and update supported versions using approved tests. Do not commit credentials; restrict, rotate, and report exposed secrets through the organization's procedure."),
            article("Build, release, and secure maintenance", "Use controlled build and release steps that establish who approved a change, which source was used, and where the result was deployed. Apply relevant review and verification gates. Keep a support path for vulnerability reports and maintain releases until planned replacement or retirement."),
            scenario("Respond to a committed credential", "A colleague notices that a test credential appeared in a source-control change visible to the development team.", "What is the safest response?", "Report it promptly to the repository owner so it can be revoked and handled under the secrets procedure"),
        ],
    },
    {
        "module_code": "CYB-305",
        "semester": 3,
        "title": "Web Application and API Security",
        "slug": "web-application-api-security",
        "category": "Application security",
        "summary": "Design safer web and API services around identity, data validation, and ownership.",
        "description": "Understand browser-server boundaries, API identities, data handling, error behavior, and application logging. Learn to translate secure design and review findings into actionable work for service owners.",
        "level": "Intermediate",
        "duration": "40 hours",
        "icon": "⌘",
        "lessons": [
            article("Web architecture and trust boundaries", "A web application may include a browser, application services, data stores, and external providers. A trust boundary identifies where identity, input, or data crosses between components. Document who owns each component and what information passes between them before deciding how to protect it."),
            article("Safer API identity and data handling", "An API should define which identity may request each action and which data it may receive. Validate requests according to documented expectations, minimize sensitive responses, and use approved transport protections. Logs should support operations without unnecessarily reproducing passwords, access tokens, or personal information."),
            article("Review, monitoring, and remediation", "Application review compares behavior and configuration with the approved design and service requirements. Record affected release, evidence, business impact, and recommended owner in a clear finding. Verify remediation through an approved staging or training workflow before a responsible owner authorizes release."),
            scenario("Review an overly detailed error", "A design review notes that a training API returns internal implementation details in a fictional error message.", "What should the developer recommend?", "Return a helpful generic error and record diagnostic details only in the approved protected server log"),
        ],
    },
    {
        "module_code": "CYB-306",
        "semester": 3,
        "title": "Cloud, Virtualization, and Container Security",
        "slug": "cloud-virtualization-container-security",
        "category": "Cloud and platform security",
        "summary": "Apply shared responsibility, identity controls, asset ownership, and recovery to cloud services.",
        "description": "Study cloud service models, shared responsibility, tenant boundaries, virtual machines, managed identities, container supply chains, logging, backups, and configuration ownership.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "☁",
        "lessons": [
            article("Service models and shared responsibility", "Cloud customers and providers share security responsibilities differently across infrastructure, platform, and software services. The contract, service design, and provider documentation determine who operates each control. Maintain a responsibility matrix rather than assuming that a provider manages every customer setting."),
            article("Cloud identities, configuration, and logs", "Cloud roles and service identities grant access across sensitive resources. Use named ownership, least privilege, approved changes, and protected audit records. Review configuration against documented organizational baselines; preserve evidence and ask the account owner before changing any live resource."),
            article("Virtual machines and container lifecycle", "Virtual machines and containers package computing environments in different ways; neither is secure by default. Keep approved base images and dependencies under responsible ownership, record where workloads are deployed, and plan their update and retirement. Use organization-approved isolated environments for teaching and development."),
            scenario("Review a cloud access change", "A fictional project request proposes granting an entire training team broad access to a shared cloud account.", "What should the cloud owner request first?", "Identify the specific tasks and approve narrowly scoped, time-limited roles for named users"),
        ],
    },
    {
        "module_code": "CYB-401",
        "semester": 4,
        "title": "Threat Intelligence and Malware Defense",
        "slug": "threat-intelligence-malware-defense",
        "category": "Threat intelligence and defense",
        "summary": "Evaluate defensive intelligence and coordinate safe responses to suspicious files.",
        "description": "Learn how to judge the source, age, confidence, relevance, and handling restrictions of threat information. Malware-related lessons focus on prevention, incident reporting, and approved isolated analysis by qualified teams.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⬡",
        "lessons": [
            article("Threat intelligence and confidence", "Threat intelligence helps defenders make decisions when its source, collection date, confidence, and relevance are understood. A label or indicator can become outdated or generate false positives. Check approved internal context and vendor sources, and explain uncertainty to decision-makers."),
            article("Malware defense and safe handling", "Suspicious files and attachments may endanger people, systems, and evidence if opened or copied casually. Follow organizational prevention and reporting procedures. File examination belongs to trained personnel in an expressly authorized, isolated analysis environment; never experiment with suspicious software on a normal device."),
            article("Sharing, privacy, and actionable reporting", "Before sharing a threat report or indicator, confirm authorization, data classification, privacy implications, source restrictions, and the intended recipients. A concise defensive report explains what is known, what remains uncertain, and what approved decision or review is being requested."),
            scenario("Handle a suspicious attachment", "A message arrives with an unexpected invoice attachment from an unverified sender. A colleague offers to open it using their work laptop to identify its contents.", "What should the colleague do?", "Do not open or forward the attachment and report the message through the approved security channel"),
        ],
    },
    {
        "module_code": "CYB-402",
        "semester": 4,
        "title": "Security Assessments and Authorized Testing",
        "slug": "security-assessments-authorized-testing",
        "category": "Security assessment",
        "summary": "Plan authorized assessments, respect written scope, and report risk responsibly.",
        "description": "Study assessment objectives, written authorization, rules of engagement, safety constraints, evidence records, reporting, and remediation. All practice is performed against fictional cases; this module does not direct learners to test third-party systems.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⌖",
        "lessons": [
            article("Assessment objectives and authorization", "A responsible assessment starts with a written purpose, an explicitly authorized environment, the named approving owner, in-scope assets, excluded assets, dates, and emergency contacts. Confirm permission and boundaries before any activity; stop if scope is missing or unclear."),
            article("Rules of engagement and safety", "Rules of engagement describe permitted methods at a high level, prohibited actions, operating hours, data-handling rules, participant responsibilities, and stop conditions. Agree on a safe test account and synthetic data when applicable. Avoid activity that could affect service availability or expose real personal information."),
            article("Evidence and finding reports", "A good finding provides an executive summary, affected in-scope asset, reproducible non-sensitive evidence, impact, limitations, and a prioritized remediation recommendation. Protect collected data, share only with named stakeholders, and verify fixes within the authorized follow-up process."),
            scenario("Stop for an out-of-scope asset", "During a supervised assessment of an isolated training network, the learner notices a device that is not listed in the written authorization.", "What must the learner do?", "Stop activity involving that device and ask the assessment lead to confirm its authorization and scope"),
        ],
    },
    {
        "module_code": "CYB-403",
        "semester": 4,
        "title": "Security Auditing, Assurance, and Standards",
        "slug": "security-auditing-assurance-standards",
        "category": "Governance, risk and compliance",
        "summary": "Evaluate documented safeguards impartially and communicate useful, evidence-based findings.",
        "description": "Learn audit independence, criteria, evidence sampling, control testing concepts, finding severity, remediation ownership, and assurance limitations. Use approved organizational and official reference material.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "◫",
        "lessons": [
            article("Audit scope, criteria, and independence", "An assurance engagement identifies its purpose, period, systems, owners, criteria, and exclusions before gathering evidence. Auditors maintain impartiality and protect confidential records. The agreed criteria should be traceable to approved organizational requirements, contracts, or applicable standards."),
            article("Evidence quality and control review", "Evidence should be relevant to the question, appropriately dated, attributable to a reliable source, and collected with permission. Interviews, documents, and observed operation answer different questions. Document the sample and any limitations so reviewers do not overstate what the evidence proves."),
            article("Findings and corrective action", "A useful finding explains the applicable criterion, condition observed, supporting evidence, business risk, and agreed corrective action. Confirm factual accuracy with the responsible owner while preserving auditor independence. Track who will act, when the action is due, and how completion will be validated."),
            scenario("Handle conflicting evidence", "An audit interview describes a quarterly access review, but the evidence provided covers only one team and one month.", "What should the auditor conclude?", "Record the evidence limitation and request the approved review records needed to assess the stated control"),
        ],
    },
    {
        "module_code": "CYB-404",
        "semester": 4,
        "title": "Business Continuity and Disaster Recovery",
        "slug": "business-continuity-disaster-recovery",
        "category": "Business continuity and resilience",
        "summary": "Plan for essential services, test recovery, and protect operational dependencies.",
        "description": "Understand business impact analysis, recovery objectives, continuity roles, backup responsibilities, disaster-recovery plans, communication, and exercise design.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "↻",
        "lessons": [
            article("Business impact and recovery priorities", "A business impact analysis identifies essential activities, their dependencies, service owners, and the harm caused by an interruption. Recovery time and recovery point objectives express business priorities that teams must agree and verify against actual capabilities."),
            article("Backups and disaster-recovery roles", "Backups need protected access, appropriate retention, verified integrity, and periodic restoration exercises. Disaster recovery coordinates people, providers, systems, communications, and business decisions in an agreed order. Assign clear roles and escalation contacts before an emergency."),
            article("Exercises, communications, and improvement", "Tabletop exercises safely evaluate whether people can locate a plan, make timely decisions, and contact the right owners. Record decisions and gaps without disrupting production services. Update the plan, assign corrective actions, and verify that critical contacts and procedures remain current."),
            scenario("Verify a recovery claim", "A service owner says their backups are reliable but cannot identify a recent restoration test or the approved recovery objective.", "What evidence should the continuity team request?", "Arrange an approved, non-production restoration exercise and document the result against the owner's recovery objective"),
        ],
    },
    {
        "module_code": "CYB-405",
        "semester": 4,
        "title": "IoT, Mobile, and Operational Technology Security",
        "slug": "iot-mobile-operational-technology-security",
        "category": "Emerging technology security",
        "summary": "Adapt protective measures to constrained devices and availability-sensitive environments.",
        "description": "Examine device ownership, update support, privacy, mobile management, industrial safety, network separation, supplier dependencies, and carefully governed change in connected environments.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "◉",
        "lessons": [
            article("Connected devices and asset ownership", "Connected devices may have long service lives, limited update options, and unclear supplier responsibilities. Record their owners, purpose, network location, support status, and physical dependencies. When a device cannot receive an update, consult its owner about a documented risk decision and protective alternative."),
            article("Mobile device management and privacy", "A managed mobile device combines organizational access with information about its user. Use published device-management policies, transparent employee guidance, approved remote actions, and separate work data where supported. Confirm authorization and impact before taking steps that could erase a person's device."),
            article("Operational technology and safety", "Operational technology monitors or controls physical processes where safety and service availability may outweigh routine update timing. Coordinate with engineers, safety owners, suppliers, and incident leaders before making a change. Use documented procedures and training environments rather than experimenting on live equipment."),
            scenario("Coordinate an unsupported device", "A facilities inventory identifies a connected sensor whose supplier no longer provides security updates. It supports a building system managed by another department.", "What is the responsible next step?", "Tell the system owner and facilities team and assess documented isolation, replacement, and continuity options together"),
        ],
    },
    {
        "module_code": "CYB-406",
        "semester": 4,
        "title": "Cybersecurity Capstone and Professional Portfolio",
        "slug": "cybersecurity-capstone-professional-portfolio",
        "category": "Capstone and professional practice",
        "summary": "Combine risk, monitoring, response, and communication in a supervised defensive project.",
        "description": "Bring together the diploma-style pathway with a supervisor-approved case study. Develop a threat-aware design, evidence-led response plan, change proposal, and clear portfolio report using synthetic data and explicitly authorized materials.",
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "✳",
        "lessons": [
            article("Define a safe, scoped project", "Select an educational problem with a supervisor, clear learning outcomes, approved synthetic information, named reviewers, and achievable milestones. Document boundaries and exclusions. Do not collect real personal data, access systems, or test a service unless its responsible owner has given explicit written authorization."),
            article("Build an evidence-led defense proposal", "Explain the business context, assets, risks, assumptions, proposed safeguards, responsible owners, and validation measures in a concise project plan. Separate observed facts from estimates. Compare options with stakeholders and include implementation, monitoring, maintenance, and recovery."),
            article("Report, present, and reflect", "A professional portfolio should be reproducible, readable, appropriately classified, and clear about its limitations. Present recommendations to their intended audience, credit sources, protect sensitive information, and record feedback. Reflect on ethical decisions and identify skills for continued development."),
            scenario("Choose a capstone dataset", "A learner has permission to prepare a presentation about incident trends but has access to both fictional training events and named staff records.", "Which material should the learner use in their portfolio?", "Use only the instructor-approved fictional events and follow the agreed scope and data-handling rules"),
        ],
    },
]


def build_diploma_lesson(module, lesson, order):
    title = lesson["title"]
    content = lesson["content"]
    practical_activity = lesson.get("practical_activity", "")
    challenge_prompt = lesson.get("challenge_prompt", "")
    assessment_prompt = challenge_prompt or (
        f"Explain how you would apply {title.casefold()} to an approved "
        "organizational scenario, what evidence would support your decision, "
        "and what limitation or risk you would communicate."
    )
    activity_steps = [
        "Work only with the fictional case and approved study materials; record the case assumptions before making a recommendation.",
        f"Produce a clearly labelled {practical_activity or f'study worksheet for {title.casefold()}'} that relates the lesson notes to the module outcome.",
        "Support your recommendation with a stated reason, an accountable owner, and evidence that could be reviewed.",
        "Add one alternative explanation, one limitation, and the next safe question for a subject-matter owner.",
    ]
    content = "\n\n".join(
        [
            f"LESSON {order:02d} · FIVE HOURS · DIPLOMA-STYLE STUDY PLAN",
            "LEARNING OUTCOMES\n"
            f"By the end of this lesson, you should be able to explain {title.casefold()}, "
            f"apply it to the module focus of {module['summary'].rstrip('.').casefold()}, "
            "identify which facts still need confirmation, and communicate a proportionate "
            "recommendation to its accountable owner.",
            f"CORE LESSON NOTES\n{content}",
            f"WORKED EXAMPLE\nConsider a fictional organization reviewing {title.casefold()}. "
            f"The team first identifies the relevant assets and owners, then compares the "
            f"available evidence with its stated objective. Use this example to explain how "
            f"{title.casefold()} affects a real business decision; do not assume that one "
            "unfamiliar event proves wrongdoing or that a technical safeguard eliminates risk.",
            "GUIDED PRACTICE · 90 MINUTES\n"
            + "\n".join(f"{step}. {instruction}" for step, instruction in enumerate(activity_steps, 1)),
            "INDEPENDENT STUDY · 60 MINUTES\nUse the course notes and any instructor-approved "
            "references to prepare a one-page study record. Define three important terms, "
            "summarize the decision or process involved, cite the source of each factual "
            "claim, and mark assumptions separately from confirmed information. Use "
            "synthetic examples; do not copy private organizational, learner, or customer data.",
            "KNOWLEDGE CHECK · 45 MINUTES\n"
            f"1. Explain the central concept in {title.casefold()} in your own words.\n"
            "2. Which fact would most change your recommendation, and how would you verify it "
            "through an approved source?\n"
            "3. Who should own the next decision, and what is one limitation you would report?",
            "ASSESSMENT AND REVIEW\n"
            f"Assessment question: {assessment_prompt}\n"
            "Review your answer against four criteria: accurate use of lesson concepts; "
            "a traceable reason and evidence source; appropriate authorization, privacy, "
            "and safety; and a clear next step with a responsible owner. Correct any "
            "unsupported conclusion before adding the work to your learning portfolio.",
            "FIVE-HOUR TIME ALLOCATION\n"
            "15 minutes: review outcomes and prepare the fictional materials. "
            "45 minutes: read the core notes and write a glossary. "
            "30 minutes: analyze the worked example. "
            "90 minutes: complete and document the guided practice. "
            "60 minutes: complete independent study. "
            "45 minutes: answer and review the knowledge check. "
            "15 minutes: write a reflection and note one question for your instructor. "
            "Total: 300 minutes (5 hours).",
            "REFLECTION · 15 MINUTES\nWhich assumption in your work would you most want a "
            "reviewer to challenge? State what evidence could answer that question and "
            "which approved owner or instructor you would consult.",
        ]
    )
    return {
        **lesson,
        "duration": "5 hours",
        "content": content,
    }
