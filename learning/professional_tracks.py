PROFESSIONAL_TRACKS = [
    {
        "title": "Authorized Offensive Security Assessment",
        "slug": "authorized-offensive-security-assessment",
        "category": "Offensive security",
        "summary": (
            "Learn the professional assessment lifecycle, from written scope "
            "and safe planning to evidence-based findings and retesting."
        ),
        "description": (
            "An advanced, 40-hour professional study path for authorized security "
            "assessment. Practice engagement planning, scope analysis, threat "
            "modeling, controlled validation concepts, reporting, and remediation "
            "using fictional case files and instructor-provided synthetic evidence. "
            "No live targets, scanning, exploit execution, or third-party systems "
            "are used."
        ),
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⌖",
        "featured": False,
        "lessons": [
            {
                "title": "Professional ethics, authorization, and duty of care",
                "notes": (
                    "Authorized assessment is a professional service, not permission "
                    "to explore anything reachable. Before work begins, the approving "
                    "asset owner and assessment lead should agree in writing on the "
                    "purpose, named people, assets, dates, methods at a safe level, "
                    "excluded systems, data-handling rules, emergency contacts, and "
                    "stop conditions. Learners must understand the difference between "
                    "a signed scope and an informal request, and must not infer "
                    "permission from ownership of an account or network connection. "
                    "Privacy, applicable law, contracts, safety, and service continuity "
                    "constrain every decision. If approval expires, a system is "
                    "unlisted, or an instruction conflicts with the written rules, "
                    "pause and ask the named lead. Record decisions and never retain "
                    "unnecessary sensitive data."
                ),
                "guided": (
                    "Review a fictional engagement pack. Identify the approver, "
                    "purpose, in-scope training assets, exclusions, dates, emergency "
                    "contact, data restrictions, and stop conditions. Mark any "
                    "ambiguity as a blocker rather than filling it in yourself."
                ),
                "independent": (
                    "Create a one-page authorization checklist and a concise "
                    "escalation note for a hypothetical scope conflict. Distinguish "
                    "what the document says from your interpretation."
                ),
                "check": (
                    "What is the first action when an asset is not explicitly "
                    "in scope? Why is verbal permission not a substitute for the "
                    "approved written authorization?"
                ),
                "review": (
                    "A complete response identifies the missing authorization, "
                    "stops work affecting the asset, records the observation, and "
                    "asks the named assessment lead for written clarification."
                ),
            },
            {
                "title": "Scope, asset ownership, and rules of engagement",
                "notes": (
                    "A scope statement turns an assessment objective into clear "
                    "boundaries. It identifies accountable asset owners, approved "
                    "training environments, business dependencies, excluded assets, "
                    "time windows, allowed data, and who can authorize a change. "
                    "Rules of engagement state how participants communicate, how "
                    "unexpected effects are reported, who can pause activity, and "
                    "what happens if the approved environment is unavailable. "
                    "Assessors should use provided inventories and diagrams, note "
                    "their age and limitations, and ask owners to resolve conflicting "
                    "records. A scope review is also a safety review: an apparently "
                    "isolated component may support a shared service. Changes to "
                    "scope require documented approval before work resumes."
                ),
                "guided": (
                    "Build a paper scope matrix from a fictional asset register. "
                    "For each entry, record its owner, environment, inclusion or "
                    "exclusion, business dependency, approval source, and unresolved "
                    "question."
                ),
                "independent": (
                    "Write a change-control record for a hypothetical request to "
                    "add a training asset. Include the evidence and approvals needed "
                    "before the scope can be updated."
                ),
                "check": (
                    "How should an assessor handle an outdated inventory or "
                    "conflicting ownership record? Which role can approve a scope "
                    "change?"
                ),
                "review": (
                    "The assessor does not resolve uncertainty by testing. The "
                    "asset owner and engagement approver clarify and document the "
                    "boundary before activity continues."
                ),
            },
            {
                "title": "Assessment planning and threat modeling",
                "notes": (
                    "Good assessment planning starts with a business question, not "
                    "a tool. Identify the service purpose, important information, "
                    "user roles, trust boundaries, dependencies, and likely "
                    "consequences of a weakness. A lightweight threat model records "
                    "assets, actors, assumptions, misuse cases, existing safeguards, "
                    "and questions for owners. Convert approved objectives into a "
                    "test plan with a sequence, responsible reviewer, evidence "
                    "expectations, and explicit safety limits. Prioritize areas by "
                    "business impact and uncertainty rather than by novelty. The "
                    "plan must make clear that any practical validation uses only "
                    "the isolated training environment and supplied artifacts. "
                    "Review plans with the service owner before the authorized "
                    "engagement begins."
                ),
                "guided": (
                    "Create a data-flow sketch for a fictional student portal. "
                    "Mark its users, records, components, trust boundaries, "
                    "assumptions, and three paper-based misuse cases."
                ),
                "independent": (
                    "Turn one modeled risk into a proposed assessment question, "
                    "the non-sensitive evidence that could answer it, and the "
                    "owner who must approve the review."
                ),
                "check": (
                    "How does a threat model help prioritize a test plan? Why "
                    "should the service owner review assumptions before assessment?"
                ),
                "review": (
                    "A defensible plan links each objective to an asset, business "
                    "risk, approved evidence source, and reviewer, while stating "
                    "what the exercise cannot establish."
                ),
            },
            {
                "title": "Reconnaissance through approved records",
                "notes": (
                    "Professional assessors build context from sources the engagement "
                    "explicitly permits. In this learning path, the sources are "
                    "fictional inventories, architecture diagrams, change records, "
                    "and synthetic observations supplied by an instructor. Record "
                    "each source, its date, its owner, and its reliability. Do not "
                    "probe public addresses, search for real people's information, "
                    "or infer that a service is in scope because a diagram mentions "
                    "it. Reconcile inconsistencies with an authorized owner. A useful "
                    "asset profile explains purpose, sensitivity, dependencies, "
                    "exposure assumptions, and the evidence gap that remains. "
                    "Professional notes separate observations from conclusions and "
                    "avoid collecting information that is not needed for the approved "
                    "objective."
                ),
                "guided": (
                    "Compare a fictional inventory, diagram, and change record. "
                    "Prepare an asset table with source, date, owner, confidence, "
                    "and discrepancy for each relevant training asset."
                ),
                "independent": (
                    "Write a short source-quality statement explaining which "
                    "records support the assessment plan and which facts still "
                    "require confirmation."
                ),
                "check": (
                    "Why must an assessor record the source and date of an asset "
                    "claim? What should happen when a record names an unapproved "
                    "system?"
                ),
                "review": (
                    "Use only permitted records, preserve provenance, avoid "
                    "unnecessary collection, and escalate any out-of-scope "
                    "reference without interacting with it."
                ),
            },
            {
                "title": "Safe validation and evidence quality",
                "notes": (
                    "Validation asks whether a stated security condition is "
                    "supported by evidence. An assessment should use the least "
                    "intrusive method that can answer the approved question, with "
                    "a reviewer and stop criteria agreed in advance. In this course, "
                    "learners analyze synthetic screenshots, mock configuration "
                    "summaries, and fictional test results; they do not execute "
                    "exploits, send payloads, or interact with services. Record "
                    "the source, time, environment label, expected condition, "
                    "observed result, and limitations. Remove secrets and personal "
                    "data from working notes. A single ambiguous observation is "
                    "not proof of impact: seek corroboration through approved "
                    "evidence and state uncertainty honestly. Escalate unexpected "
                    "effects immediately."
                ),
                "guided": (
                    "Review a fictional set of assessment observations. Separate "
                    "direct evidence, interpretation, possible impact, and missing "
                    "context. Identify which item would require an immediate pause."
                ),
                "independent": (
                    "Draft a non-sensitive evidence note for one mock finding, "
                    "including provenance, time, scope label, limitation, and "
                    "responsible reviewer."
                ),
                "check": (
                    "What makes evidence reproducible without exposing sensitive "
                    "data? Why should validation use the least intrusive approved "
                    "method?"
                ),
                "review": (
                    "A reliable note can be reviewed by another authorized person, "
                    "states its limitations, and contains no unnecessary secret or "
                    "personal information."
                ),
            },
            {
                "title": "Application and identity assessment by design review",
                "notes": (
                    "Application assessment can identify risk through design and "
                    "evidence review before any live testing is considered. Examine "
                    "fictional role matrices, data-flow diagrams, session "
                    "requirements, and sample access decisions. Ask whether the "
                    "server applies authorization to each requested action and "
                    "resource, whether sensitive data is minimized, and whether "
                    "security-relevant decisions are auditable. A visible interface "
                    "restriction alone does not demonstrate server-side enforcement. "
                    "For every observation, identify the affected business action, "
                    "the evidence source, the expected behavior, and the review "
                    "owner. Do not attempt to access real accounts or records. "
                    "Any practical validation beyond paper artifacts requires "
                    "explicit written scope and a designated isolated environment."
                ),
                "guided": (
                    "Use a fictional role-action matrix to identify inconsistent "
                    "permissions. Describe the affected business workflow and "
                    "request confirmation from the fictional service owner."
                ),
                "independent": (
                    "Prepare a review checklist for identity, authorization, "
                    "data minimization, auditability, and error handling in a "
                    "fictional application design."
                ),
                "check": (
                    "Why is a hidden interface control not enough to prove "
                    "authorization? What evidence would support a design-review "
                    "observation?"
                ),
                "review": (
                    "Tie the observation to a documented requirement, a synthetic "
                    "example, a business consequence, and an owner who can confirm "
                    "intended behavior."
                ),
            },
            {
                "title": "Risk rating, reporting, and remediation",
                "notes": (
                    "A professional finding helps an organization make a decision. "
                    "It states the condition, affected in-scope asset, evidence, "
                    "business consequence, likelihood assumptions, limitations, and "
                    "a proportionate recommendation. A rating should reflect "
                    "context and a documented method, not just a technical label. "
                    "Separate an executive summary from technical evidence and "
                    "share the report only with named, authorized recipients. "
                    "Remediation should have an accountable owner, target date, "
                    "and evidence of completion. Retesting requires renewed "
                    "authorization, agreed scope, and an approved environment; "
                    "do not assume that a previous approval continues indefinitely. "
                    "Communicate disagreements fairly and update the record when "
                    "new evidence changes a conclusion."
                ),
                "guided": (
                    "Rank three fictional findings using a supplied risk rubric. "
                    "Explain the business context, confidence, impact, and "
                    "limitations behind each priority."
                ),
                "independent": (
                    "Write an executive summary and one finding with a clear "
                    "condition, evidence reference, impact, recommendation, "
                    "owner, and follow-up date."
                ),
                "check": (
                    "What information makes a finding actionable? Why does a "
                    "remediation retest need its own agreed scope and approval?"
                ),
                "review": (
                    "A useful report is accurate, proportionate, confidential, "
                    "traceable to evidence, and clear about who owns each action."
                ),
            },
            {
                "title": "Capstone lab: conduct an authorized tabletop assessment",
                "lesson_type": "lab",
                "notes": (
                    "The capstone is a paper-based engagement simulation. Learners "
                    "receive a fictional authorization, synthetic asset register, "
                    "rules of engagement, and mock observations. The objective is "
                    "to demonstrate professional judgment across the assessment "
                    "lifecycle, not to operate a security tool. Verify that every "
                    "asset is listed, identify missing approvals, preserve the "
                    "provided evidence references, and prepare a concise finding "
                    "and remediation handoff. If the scenario introduces a scope "
                    "conflict or pause instruction, stop and document it. The "
                    "exercise does not connect to a network, execute code, or "
                    "include real target data."
                ),
                "guided": (
                    "Review the mock authorization and case notes. Produce a "
                    "scope decision, an evidence-quality assessment, and an "
                    "escalation record for the unlisted item."
                ),
                "independent": (
                    "Complete a short assessment report that separates confirmed "
                    "facts, assumptions, limitations, risk rationale, and "
                    "owner-assigned next steps."
                ),
                "check": (
                    "Which condition requires stopping the assessment? What "
                    "evidence and approval must exist before a retest?"
                ),
                "review": (
                    "The capstone is successful when the learner honors the "
                    "written boundary, protects evidence, communicates uncertainty, "
                    "and routes decisions to authorized owners."
                ),
                "challenge_prompt": (
                    "The mock case notes mention a system that is missing from "
                    "the signed scope. What should the assessor do?"
                ),
                "expected_answer": (
                    "Stop work involving the unlisted system and ask the assessment "
                    "lead for written scope confirmation"
                ),
            },
        ],
    },
    {
        "title": "Defensive Security Operations and Incident Response",
        "slug": "defensive-security-operations-incident-response",
        "category": "Defensive security",
        "summary": (
            "Build SOC, alert triage, detection review, incident coordination, "
            "and evidence-aware response skills."
        ),
        "description": (
            "An advanced, 40-hour professional study path for defensive security "
            "operations. Practice monitoring design, synthetic-alert triage, "
            "case documentation, detection quality, incident coordination, "
            "evidence handling, and recovery planning. Exercises use fictional "
            "records and tabletop decisions; they do not access live systems."
        ),
        "level": "Advanced",
        "duration": "40 hours",
        "icon": "⌘",
        "featured": False,
        "lessons": [
            {
                "title": "SOC roles, monitoring objectives, and workflow",
                "notes": (
                    "A security operations centre translates monitoring into "
                    "accountable decisions. Teams define which business risks they "
                    "monitor, which assets and event sources are covered, who "
                    "owns each alert, and how urgent cases reach decision-makers. "
                    "Common responsibilities include intake, triage, escalation, "
                    "incident coordination, detection improvement, and shift "
                    "handover. Establish service-level expectations that reflect "
                    "business impact and available coverage rather than promising "
                    "that every alert will be resolved instantly. Protect analyst "
                    "wellbeing by reducing duplicate noise and documenting clear "
                    "decision paths. A monitoring plan should identify gaps and "
                    "dependencies so leaders understand what the SOC can and "
                    "cannot see."
                ),
                "guided": (
                    "Map a fictional SOC workflow from alert receipt through "
                    "triage, escalation, incident ownership, closure, and "
                    "improvement review. Assign an accountable role at each step."
                ),
                "independent": (
                    "Draft a one-page monitoring charter with objectives, "
                    "coverage limits, escalation contacts, privacy rules, and "
                    "handover expectations."
                ),
                "check": (
                    "Why is an alert not the same as a confirmed incident? "
                    "Which operational gaps should a monitoring charter disclose?"
                ),
                "review": (
                    "A useful charter aligns monitoring with business risk, "
                    "defines owners and escalation, and clearly documents "
                    "coverage limitations."
                ),
            },
            {
                "title": "Telemetry coverage, integrity, and context",
                "notes": (
                    "Defensive analysis depends on knowing where event data comes "
                    "from and how it can be trusted. Identity, endpoint, network, "
                    "application, and cloud records each describe different "
                    "observations; absence of a record does not prove that an "
                    "event did not occur. Maintain an inventory of approved "
                    "sources, owners, timestamps, retention, access restrictions, "
                    "and known collection gaps. Time synchronization and "
                    "consistent identifiers help correlate events, but analysts "
                    "must note clock and parsing limitations. Protect logs from "
                    "unauthorized alteration and avoid recording secrets or "
                    "unnecessary personal data. Synthetic exercises should teach "
                    "provenance and uncertainty without exposing organizational "
                    "telemetry."
                ),
                "guided": (
                    "Build a fictional log-source coverage matrix. For each "
                    "source, identify owner, event types, time basis, retention, "
                    "privacy consideration, and a known blind spot."
                ),
                "independent": (
                    "Write a data-quality note explaining how missing or "
                    "inconsistent timestamps would affect a fictional investigation."
                ),
                "check": (
                    "Why does missing telemetry not establish that an event did "
                    "not happen? What provenance should accompany an event record?"
                ),
                "review": (
                    "Analysts describe what a source can support, document "
                    "integrity and time limits, and seek corroboration before "
                    "drawing conclusions."
                ),
            },
            {
                "title": "Alert triage and evidence-led case management",
                "notes": (
                    "Triage is a structured decision process. Confirm the alert "
                    "source and time range, identify the affected asset and "
                    "business owner, check whether known maintenance or user "
                    "activity explains the event, and compare available "
                    "independent records. Assign severity using the approved "
                    "criteria and explain confidence and possible impact. Keep "
                    "confirmed facts separate from hypotheses. A case record "
                    "should include the alert reference, evidence sources, "
                    "queries or review steps at a non-sensitive summary level, "
                    "decisions, owner, next action, and review time. Do not "
                    "collect more personal information than necessary or contact "
                    "a suspected actor. Escalate when policy thresholds or "
                    "uncertainty require a specialist."
                ),
                "guided": (
                    "Triage a supplied fictional alert packet. Complete a case "
                    "record with facts, hypotheses, confidence, business impact, "
                    "next owner, and a reasoned escalation decision."
                ),
                "independent": (
                    "Write a shift handover that lets another analyst continue "
                    "the case without repeating work or mistaking an assumption "
                    "for a fact."
                ),
                "check": (
                    "Which details belong in a useful case handover? How should "
                    "an analyst communicate low confidence or missing evidence?"
                ),
                "review": (
                    "The case should be reproducible, proportionate, privacy-aware, "
                    "and explicit about who owns the next decision."
                ),
            },
            {
                "title": "Detection quality and continuous improvement",
                "notes": (
                    "A detection is useful when it identifies a meaningful "
                    "condition with enough context for an analyst to decide "
                    "what to do. Evaluate a detection against its intended risk, "
                    "approved data sources, known false positives, missed cases, "
                    "privacy impact, and operational owner. In training, review "
                    "fictional alert examples and plain-language detection "
                    "criteria; do not deploy rules or query live systems. "
                    "Measure quality with representative, authorized test cases "
                    "and analyst feedback. Tuning should be reviewed and "
                    "documented so a reduction in noise does not hide important "
                    "events. Every detection needs an owner, an update path, "
                    "a review date, and a clear statement of its limitations."
                ),
                "guided": (
                    "Compare synthetic positive and benign alert examples "
                    "against a written detection objective. Record true "
                    "matches, expected benign cases, missing context, and "
                    "possible blind spots."
                ),
                "independent": (
                    "Propose a detection-quality scorecard covering purpose, "
                    "coverage, analyst actionability, privacy, ownership, and "
                    "review frequency."
                ),
                "check": (
                    "Why can suppressing noisy alerts create a blind spot? "
                    "What evidence and approvals should support a detection change?"
                ),
                "review": (
                    "Improvements should preserve the stated security objective, "
                    "be tested on authorized examples, have an owner, and be "
                    "reviewed for unintended effects."
                ),
            },
            {
                "title": "Identity and endpoint incident coordination",
                "notes": (
                    "Reports of unusual sign-ins or endpoint behavior need prompt, "
                    "coordinated assessment. Verify the report through approved "
                    "identity and asset owners, establish what is known, and "
                    "follow the organization's incident playbook. A responder "
                    "should not reset accounts, isolate devices, or interrupt "
                    "services outside assigned authority. The incident lead "
                    "weighs containment against safety, business continuity, "
                    "evidence preservation, and privacy. Record the decision, "
                    "approver, time, affected service, and user communication. "
                    "Escalate suspected exposure of credentials or sensitive "
                    "data using a trusted channel. Reassess as evidence changes "
                    "and coordinate with support teams so protective action "
                    "does not create avoidable harm."
                ),
                "guided": (
                    "Work through a fictional sign-in and endpoint report. "
                    "Identify verification owners, the playbook decision-maker, "
                    "user-impact questions, and the safe escalation route."
                ),
                "independent": (
                    "Create a decision log for two hypothetical containment "
                    "options, including authority, impact, evidence concerns, "
                    "communications, and a review trigger."
                ),
                "check": (
                    "Who may authorize disruptive containment? What should a "
                    "responder do when credentials may have been exposed?"
                ),
                "review": (
                    "Follow the approved playbook, use a separate trusted "
                    "reporting route, preserve context, and leave disruptive "
                    "decisions with authorized incident leads."
                ),
            },
            {
                "title": "Incident command, communications, and recovery",
                "notes": (
                    "Incident response coordinates people and decisions under "
                    "uncertainty. A command structure names an incident lead, "
                    "technical owners, business decision-makers, privacy or "
                    "legal advisers, and communications contacts. Maintain a "
                    "time-stamped decision log that records the evidence "
                    "considered, the decision-maker, and follow-up. Communicate "
                    "confirmed facts and approved actions to the right audience; "
                    "do not speculate or share sensitive detail broadly. Recovery "
                    "uses authorized, known-good procedures and validation "
                    "criteria agreed with service owners. Track dependencies, "
                    "monitoring needs, and return-to-service approval. After "
                    "closure, conduct a learning review that assigns measurable "
                    "actions without blame and checks that improvements were "
                    "completed."
                ),
                "guided": (
                    "Run a paper tabletop using fictional updates. Maintain a "
                    "decision log, identify who may approve each action, and "
                    "prepare one audience-appropriate status message."
                ),
                "independent": (
                    "Draft a recovery checklist with service owner, validation "
                    "evidence, communications, monitoring period, and return "
                    "approval."
                ),
                "check": (
                    "Why should incident communications distinguish confirmed "
                    "facts from estimates? Who approves service recovery?"
                ),
                "review": (
                    "A response record should show accountable decisions, "
                    "controlled communications, validated recovery, and "
                    "assigned post-incident improvements."
                ),
            },
            {
                "title": "Evidence preservation, privacy, and lessons learned",
                "notes": (
                    "Evidence handling supports reliable decisions and possible "
                    "later review. Work only under the assigned authority and "
                    "approved procedure. Record the source, time, custodian, "
                    "transfer, storage location, and purpose of each evidence "
                    "item. Preserve originals as directed and avoid unnecessary "
                    "changes or duplicate copies. Restrict access to named "
                    "roles, protect sensitive information, and follow retention "
                    "and deletion requirements. Build timelines from identified "
                    "sources while recording time-zone and completeness limits. "
                    "A post-incident review should distinguish control gaps "
                    "from individual blame, identify contributing conditions, "
                    "and assign each improvement an owner, due date, and "
                    "verification measure. Complex collection or examination "
                    "belongs to qualified personnel."
                ),
                "guided": (
                    "Review a fictional custody form and timeline. Identify "
                    "missing provenance, access, time-zone, and retention "
                    "information without handling actual devices or records."
                ),
                "independent": (
                    "Write an after-action summary with confirmed facts, "
                    "limitations, contributing conditions, and three measurable "
                    "improvements with owners."
                ),
                "check": (
                    "What information makes a custody record reviewable? Why "
                    "should conclusions state source and time limitations?"
                ),
                "review": (
                    "Evidence is handled only with authority, minimum necessary "
                    "access, traceable custody, and clear limitations. Improvements "
                    "must be assigned and verified."
                ),
            },
            {
                "title": "Capstone lab: coordinate a defensive tabletop",
                "lesson_type": "lab",
                "notes": (
                    "The capstone uses a fictional incident packet with synthetic "
                    "alerts, a service inventory, a short timeline, and a "
                    "response playbook. Learners demonstrate alert triage, "
                    "evidence-aware communication, decision ownership, and "
                    "recovery planning. The packet intentionally omits some "
                    "details; professional practice means documenting uncertainty "
                    "and asking the correct owner, not inventing facts. Use only "
                    "the scenario material, respect privacy, and do not initiate "
                    "containment or access a real account or device. A strong "
                    "submission contains a case summary, escalation rationale, "
                    "decision log, audience-appropriate update, and prioritized "
                    "improvement plan."
                ),
                "guided": (
                    "Review the fictional alert packet, classify confirmed and "
                    "unconfirmed information, identify the incident lead, and "
                    "prepare the next safe escalation."
                ),
                "independent": (
                    "Submit a compact case file with timeline, evidence sources, "
                    "decision authority, recovery checks, communications, and "
                    "post-incident actions."
                ),
                "check": (
                    "What is the safest first response when an alert lacks "
                    "context? Which decisions require an authorized incident lead?"
                ),
                "review": (
                    "The learner succeeds by validating sources, communicating "
                    "uncertainty, following the playbook, and assigning "
                    "accountable next steps."
                ),
                "challenge_prompt": (
                    "A synthetic sign-in alert appears during a planned "
                    "maintenance window, but the case file has no confirmation "
                    "from the identity owner. What is the safest first action?"
                ),
                "expected_answer": (
                    "Preserve the alert details and verify the activity with the "
                    "identity owner through the approved incident channel"
                ),
            },
        ],
    },
]


def build_professional_lesson(module, lesson, order):
    content = "\n\n".join(
        [
            f"LESSON {order:02d} · FIVE HOURS · PROFESSIONAL STUDY PLAN",
            "LEARNING OUTCOMES\n"
            f"By the end of this lesson, you should be able to explain "
            f"{lesson['title'].casefold()}, apply its process to the fictional "
            f"{module['category'].casefold()} case, identify missing authority "
            "or evidence, and communicate a proportionate next step.",
            f"CORE LESSON NOTES\n{lesson['notes']}",
            f"WORKED EXAMPLE\nConsider the fictional case used in "
            f"{lesson['title'].casefold()}. Identify the relevant owner, the "
            "approved source of evidence, the business impact, and the limit "
            "of what can be concluded. Record one safe next question before "
            "recommending action. Never treat an assumption as authorization "
            "or a single unexplained event as proof.",
            "GUIDED PRACTICE · 90 MINUTES\n"
            f"{lesson['guided']} Record the assumptions, evidence source, "
            "decision owner, and safety checks in your worksheet.",
            "INDEPENDENT STUDY · 60 MINUTES\n"
            f"{lesson['independent']} Use only the fictional case and "
            "instructor-approved references. Cite sources for factual claims, "
            "separate confirmed details from assumptions, and do not include "
            "real credentials, personal information, or system identifiers.",
            "KNOWLEDGE CHECK · 45 MINUTES\n"
            f"1. {lesson['check']}\n"
            "2. Which missing fact could change your recommendation, and how "
            "would an authorized owner confirm it?\n"
            "3. What safety, privacy, or scope limitation belongs in your "
            "written handover?",
            "ASSESSMENT AND REVIEW\n"
            f"Assessment: {lesson['review']} Submit a concise worksheet "
            "showing the objective, supporting evidence, limitations, "
            "responsible owner, and next step. Review it for accuracy, "
            "authorization, privacy, traceability, and clear communication.",
            "FIVE-HOUR TIME ALLOCATION\n"
            "15 minutes: review outcomes and prepare fictional materials. "
            "45 minutes: study the notes and create a glossary. "
            "30 minutes: analyze the worked example. "
            "90 minutes: complete and document guided practice. "
            "60 minutes: complete independent study. "
            "45 minutes: answer and review the knowledge check. "
            "15 minutes: write a reflection and note one question for an "
            "instructor. Total: 300 minutes (5 hours).",
            "REFLECTION · 15 MINUTES\n"
            "Which assumption or decision in your work most needs review? "
            "State the evidence that could resolve it, the authorized owner "
            "to consult, and the condition that would make you pause.",
        ]
    )
    return {
        "title": lesson["title"],
        "lesson_type": lesson.get("lesson_type", "article"),
        "duration": "5 hours",
        "content": content,
        "challenge_prompt": lesson.get("challenge_prompt", ""),
        "expected_answer": lesson.get("expected_answer", ""),
    }


def build_professional_track(track):
    return {
        **{key: value for key, value in track.items() if key != "lessons"},
        "lessons": [
            build_professional_lesson(track, lesson, order)
            for order, lesson in enumerate(track["lessons"], start=1)
        ],
    }
