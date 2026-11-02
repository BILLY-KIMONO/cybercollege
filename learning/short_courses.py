SPECIALIST_COURSES = [
    {
        "title": "Practical Phishing and Email Security",
        "slug": "practical-phishing-email-security",
        "category": "Email security",
        "summary": "Recognize suspicious requests and respond to email threats safely.",
        "description": (
            "Build practical habits for checking unexpected messages, verifying "
            "requests through trusted channels, reporting concerns, and limiting "
            "the impact of a suspected email incident."
        ),
        "level": "Beginner",
        "duration": "4 hours",
        "icon": "✉",
        "featured": False,
        "lessons": [
            {
                "title": "How social engineering creates urgency",
                "notes": (
                    "Social engineering uses communication and context to influence a "
                    "decision. A message may imitate a manager, supplier, school, or "
                    "service and pressure its recipient with urgency, secrecy, fear, or "
                    "a reward. These signals are reasons to pause, not proof by "
                    "themselves that a message is malicious. A familiar display name "
                    "does not establish who controls the sending account. A message can "
                    "also be unexpected without being fraudulent, so compare it with "
                    "known business processes and ask the responsible person when "
                    "something does not fit."
                ),
                "guided": (
                    "Review a fictional set of messages and highlight the requested "
                    "action, the claimed sender, the deadline, and any request to keep "
                    "the matter secret. Separate observable facts from assumptions."
                ),
                "independent": (
                    "Write a short checklist of the questions you would ask before "
                    "acting on an unexpected request involving money, credentials, or "
                    "personal information."
                ),
                "check": (
                    "Why is urgency a useful signal to investigate but not enough to "
                    "classify a message? Which independent source could confirm a "
                    "request?"
                ),
                "review": (
                    "A strong review records the exact request, checks it against "
                    "normal processes, and avoids making a judgment based only on "
                    "spelling, branding, or a display name."
                ),
            },
            {
                "title": "Verify links, attachments, and payment requests",
                "notes": (
                    "Before opening an unexpected attachment or following a link, "
                    "consider whether the message and action are expected. Read the "
                    "complete destination carefully using the organization's approved "
                    "safe-preview method; a familiar logo or a short visible label "
                    "does not verify a destination. Do not enter a password or "
                    "one-time code after following an unsolicited link. Verify "
                    "sensitive requests, especially bank-detail changes and urgent "
                    "payments, through a previously established phone number or "
                    "another trusted channel—not contact details supplied in the "
                    "message. Follow local policy for handling attachments; do not "
                    "forward suspicious material to colleagues for informal review."
                ),
                "guided": (
                    "For a fictional supplier message, list the claimed change, the "
                    "evidence available in the message, and the trusted contact "
                    "already held in the supplier record. Decide what must be "
                    "confirmed before an authorized employee acts."
                ),
                "independent": (
                    "Draft a two-sentence verification message that does not repeat "
                    "the suspicious link or expose account information."
                ),
                "check": (
                    "Why should a payment change be verified using contact details "
                    "already on record? What should you do if those details are "
                    "out of date?"
                ),
                "review": (
                    "Verification should use an independent, known channel and the "
                    "organization's approval process. If no trusted route is "
                    "available, pause and ask the responsible manager or security "
                    "team."
                ),
            },
            {
                "title": "Report a suspicious message and protect accounts",
                "notes": (
                    "Prompt reporting gives a security or IT team a chance to assess "
                    "similar messages and advise affected people. Use the approved "
                    "report button or help-desk route and include useful context, "
                    "such as when the message arrived and whether you interacted "
                    "with it. Do not delete evidence or distribute the message "
                    "unless the response team instructs you to do so. If you entered "
                    "a password, approved an unexpected sign-in, or shared a code, "
                    "report that fact immediately using a separate trusted channel. "
                    "Follow the response team's instructions to protect the account; "
                    "do not attempt your own investigation or contact the suspected "
                    "sender."
                ),
                "guided": (
                    "Complete a fictional report form with the time received, "
                    "recipient, action taken, and a concise description. Leave "
                    "unknown details clearly marked rather than guessing."
                ),
                "independent": (
                    "Create a short personal response card listing your "
                    "organization's approved reporting route and an alternative "
                    "contact method if email is unavailable."
                ),
                "check": (
                    "What details make a report useful? Why should someone who "
                    "entered a password report that action promptly?"
                ),
                "review": (
                    "A useful report is timely, factual, and sent through an "
                    "approved route. Responders—not the recipient acting alone—"
                    "decide containment and evidence-handling steps."
                ),
            },
            {
                "title": "Scenario lab: handle an unexpected account alert",
                "lesson_type": "lab",
                "notes": (
                    "Unexpected sign-in alerts should be evaluated without clicking "
                    "links in the alert itself. Use a known route to reach the "
                    "organization's identity or support team, and report whether "
                    "you recognize the activity. Do not share a one-time code with "
                    "someone who contacts you, even if they claim to be support. "
                    "The responder can compare the alert with account records and "
                    "decide whether protective action is needed. This exercise is "
                    "a fixed fictional scenario and does not connect to an account "
                    "or email system."
                ),
                "guided": (
                    "Read the scenario, identify what is known and unknown, and "
                    "select the trusted reporting route before taking action."
                ),
                "independent": (
                    "Explain how you would record the alert time and your own "
                    "actions without copying codes or other sensitive information."
                ),
                "check": (
                    "What is the safest way to verify an unexpected sign-in alert? "
                    "Which information should never be shared with a caller?"
                ),
                "review": (
                    "The response should use a known support route, avoid the "
                    "message's links, and never disclose authentication codes."
                ),
                "challenge_prompt": (
                    "An unexpected sign-in alert asks you to use its link and then "
                    "read a verification code to a caller claiming to be support. "
                    "What should you do first?"
                ),
                "expected_answer": (
                    "Do not use the link or share the code; report the alert through "
                    "the organization's known support channel"
                ),
            },
        ],
    },
    {
        "title": "Secure Coding Essentials",
        "slug": "secure-coding-essentials",
        "category": "Application security",
        "summary": "Apply secure design, access control, and dependency hygiene.",
        "description": (
            "Learn developer-focused practices for handling input and sensitive "
            "data, enforcing authorization, protecting secrets, and reviewing "
            "software changes in an authorized development environment."
        ),
        "level": "Intermediate",
        "duration": "4 hours",
        "icon": "⌘",
        "featured": False,
        "lessons": [
            {
                "title": "Design for security and validate data",
                "notes": (
                    "Secure development begins by identifying the data a feature "
                    "handles, the people and services that use it, and the expected "
                    "trust boundaries. Define acceptable input at the point it "
                    "enters the application: expected type, length, format, and "
                    "allowed values. Reject invalid data with a clear, safe error "
                    "rather than trying to guess what the user intended. Validation "
                    "does not replace context-appropriate output handling or safe "
                    "database access. Use established framework features and "
                    "parameterized data operations instead of constructing "
                    "executable queries from untrusted text. Record design "
                    "assumptions so reviewers can challenge them."
                ),
                "guided": (
                    "For a fictional profile form, list each field's purpose, "
                    "permitted format, length limit, and handling of missing or "
                    "invalid values. Mark which fields contain personal data."
                ),
                "independent": (
                    "Write three safe test cases for the form: an ordinary valid "
                    "value, a boundary value, and an invalid value. Describe the "
                    "expected result without using a live service."
                ),
                "check": (
                    "Why should validation be based on an explicit expected format? "
                    "What additional protection is needed when data is stored or "
                    "displayed?"
                ),
                "review": (
                    "Reviewers should be able to trace a field from its business "
                    "purpose to validation, storage, and display, with sensitive "
                    "data minimized at each step."
                ),
            },
            {
                "title": "Enforce identity and authorization consistently",
                "notes": (
                    "Authentication establishes which identity is using an "
                    "application; authorization decides what that identity may do "
                    "to a particular resource. Every sensitive operation should "
                    "check authorization on the server using the current identity "
                    "and the specific object being requested. Hiding a button in "
                    "the interface improves usability but is not an access "
                    "control. Deny access by default, grant only the actions "
                    "required for a role, and keep administrative actions separate "
                    "from ordinary workflows. Apply the same rules to alternate "
                    "entry points such as background jobs and APIs. Log security-"
                    "relevant decisions without recording passwords, tokens, or "
                    "unnecessary personal data."
                ),
                "guided": (
                    "Create a role-and-action matrix for a fictional course "
                    "portal. Include learner, instructor, and administrator roles "
                    "and note which owner approves each privileged action."
                ),
                "independent": (
                    "Choose one sensitive action in the fictional portal and "
                    "describe how its server-side authorization decision should "
                    "be tested for both an allowed and a denied user."
                ),
                "check": (
                    "What is the difference between authentication and "
                    "authorization? Why is hiding a page control not sufficient?"
                ),
                "review": (
                    "A sound design identifies the resource owner, checks access "
                    "for every request, defaults to denial, and records only "
                    "necessary audit details."
                ),
            },
            {
                "title": "Protect secrets and manage dependencies",
                "notes": (
                    "Credentials, signing keys, and service tokens are secrets: "
                    "they should not be embedded in source code, examples, logs, "
                    "or client-side application files. Use the organization's "
                    "approved secrets-management process, limit which service "
                    "identities can retrieve each value, and rotate exposed "
                    "credentials through an authorized response. Third-party "
                    "libraries also affect the application's security and "
                    "maintenance. Record direct dependencies, use trusted "
                    "repositories and supported versions, review update notices, "
                    "and test upgrades before release. A scanner can help "
                    "identify known issues but cannot establish that a component "
                    "is safe for every use. Assign an owner to assess findings "
                    "and document accepted risk."
                ),
                "guided": (
                    "Review a fictional release checklist and mark where a "
                    "secret might be exposed, who owns dependency updates, and "
                    "what validation is required before deployment."
                ),
                "independent": (
                    "Draft a response checklist for a developer who accidentally "
                    "commits a test credential, including notification, "
                    "revocation through an approved owner, and history review."
                ),
                "check": (
                    "Why is deleting a secret from the current file not enough "
                    "after exposure? What should a dependency finding include "
                    "before it is prioritized?"
                ),
                "review": (
                    "A complete process has an accountable owner, a way to "
                    "revoke exposed values, and a documented method to test "
                    "dependency updates."
                ),
            },
            {
                "title": "Scenario lab: review a software release",
                "lesson_type": "lab",
                "notes": (
                    "A release review considers the change's purpose, affected "
                    "data, access decisions, dependencies, and rollback plan. "
                    "Reviewers should look for evidence that required checks "
                    "passed and that an accountable owner accepted any remaining "
                    "risk. A finding should be described with enough context to "
                    "reproduce the review in the authorized test environment, "
                    "without publishing secrets or personal data. This exercise "
                    "uses a fictional checklist only; it does not execute or scan "
                    "software."
                ),
                "guided": (
                    "Use the fictional release notes to identify the missing "
                    "approval and the evidence the release owner should provide."
                ),
                "independent": (
                    "Write a brief review comment that states the concern, "
                    "impact, evidence needed, and responsible owner without "
                    "including a secret."
                ),
                "check": (
                    "Which facts should be confirmed before a release proceeds? "
                    "How should an unresolved security concern be documented?"
                ),
                "review": (
                    "A reviewer communicates a specific, evidence-based concern "
                    "and follows the agreed release and escalation process."
                ),
                "challenge_prompt": (
                    "A release checklist shows a committed service token and an "
                    "unreviewed dependency update. What should happen before "
                    "deployment?"
                ),
                "expected_answer": (
                    "Pause deployment and notify the release owner to revoke the "
                    "exposed token and review the dependency through the approved process"
                ),
            },
        ],
    },
    {
        "title": "Cloud Security Fundamentals",
        "slug": "cloud-security-fundamentals",
        "category": "Cloud security",
        "summary": "Understand cloud responsibilities, identity, data, and monitoring.",
        "description": (
            "Study shared responsibility, cloud identity and access, data "
            "protection, logging, and incident response through practical "
            "defensive scenarios that do not access live cloud services."
        ),
        "level": "Intermediate",
        "duration": "4 hours",
        "icon": "☁",
        "featured": False,
        "lessons": [
            {
                "title": "Shared responsibility and cloud service models",
                "notes": (
                    "Cloud services provide computing resources through a "
                    "provider, but moving a workload does not transfer every "
                    "security duty. Responsibility depends on the service "
                    "model, contract, and configuration. A provider may operate "
                    "physical facilities while a customer remains responsible "
                    "for account access, information classification, and many "
                    "workload settings. In managed services, the provider may "
                    "operate more of the platform, but the customer still needs "
                    "to understand access, data use, retention, and recovery. "
                    "Document the service owner, provider commitments, customer "
                    "tasks, dependencies, and escalation contacts. Revisit the "
                    "shared-responsibility record when a service or business "
                    "purpose changes."
                ),
                "guided": (
                    "Use a fictional hosted learning service to sort five "
                    "responsibilities between provider, customer, and shared "
                    "ownership. Mark any item that needs contract confirmation."
                ),
                "independent": (
                    "Draw a one-page service diagram showing the provider, "
                    "customer administrators, users, data, and support contacts."
                ),
                "check": (
                    "Why does responsibility vary between service models? Which "
                    "source should confirm a provider's commitment?"
                ),
                "review": (
                    "A useful responsibility map names an owner for each "
                    "security task and distinguishes confirmed commitments "
                    "from assumptions."
                ),
            },
            {
                "title": "Secure cloud identities and administrative access",
                "notes": (
                    "Cloud control planes can create, change, and expose "
                    "important resources, so administrative identities need "
                    "strong protection. Give each person a unique account, "
                    "enable organization-approved multifactor authentication, "
                    "and use roles that grant only the actions required for a "
                    "defined task. Separate routine work from privileged "
                    "administration and review access with resource owners on "
                    "a schedule. Service identities should have named owners, "
                    "limited permissions, and a managed credential lifecycle. "
                    "Avoid shared accounts and credentials in scripts or "
                    "documents. Emergency access should be documented, "
                    "restricted, monitored, and tested through an approved "
                    "process."
                ),
                "guided": (
                    "Review a fictional access table and identify shared "
                    "accounts, unnecessary permissions, missing owners, and "
                    "access that needs review."
                ),
                "independent": (
                    "Create a quarterly access-review checklist that includes "
                    "business owner approval, role justification, and a record "
                    "of changes made by authorized administrators."
                ),
                "check": (
                    "Why should service identities have owners? How does "
                    "multifactor authentication reduce account risk without "
                    "replacing least privilege?"
                ),
                "review": (
                    "Every identity should be attributable, limited to a "
                    "defined purpose, and reviewed by an accountable owner."
                ),
            },
            {
                "title": "Protect cloud data, logs, and recovery",
                "notes": (
                    "Cloud data controls should follow the information's "
                    "classification and business purpose. Identify where data "
                    "is stored, who can access it, how it is encrypted in "
                    "transit and at rest, and how long it must be retained. "
                    "Encryption supports confidentiality but does not correct "
                    "excessive access or poor sharing decisions. Activity logs "
                    "help owners investigate changes and access; restrict who "
                    "can alter or read them and retain them according to policy. "
                    "Backups are useful only when their scope, retention, "
                    "isolation, and restoration have been tested. Record "
                    "recovery objectives with business owners and consider "
                    "provider dependencies before relying on a recovery plan."
                ),
                "guided": (
                    "For a fictional student-record service, map data "
                    "classification, authorized readers, logging owner, backup "
                    "frequency, and the person who approves a restoration test."
                ),
                "independent": (
                    "Write three questions to ask a provider about log access, "
                    "data deletion, and recovery evidence before adopting a "
                    "cloud service."
                ),
                "check": (
                    "Why does encryption not replace access control? What "
                    "evidence demonstrates that a backup can support recovery?"
                ),
                "review": (
                    "The plan should connect data classification to access, "
                    "logging, retention, and a recovery test approved by the "
                    "business owner."
                ),
            },
            {
                "title": "Scenario lab: respond to a cloud access change",
                "lesson_type": "lab",
                "notes": (
                    "An unexpected cloud configuration or access change is an "
                    "observation that needs context, not a complete incident "
                    "conclusion. Preserve the alert details through the approved "
                    "process, confirm the affected resource and change record "
                    "with its owner, and notify the cloud security or operations "
                    "team. Do not make unapproved changes to production settings "
                    "or share sensitive logs in public channels. The authorized "
                    "response team can decide whether to contain access, restore "
                    "a known configuration, or investigate further. This fixed "
                    "exercise uses no provider account or live resource."
                ),
                "guided": (
                    "Use the fictional alert and change record to identify the "
                    "resource owner, the approved escalation route, and the "
                    "facts that remain unknown."
                ),
                "independent": (
                    "Prepare a concise incident note with the alert time, "
                    "resource identifier from the fictional case, source of "
                    "verification, and next owner."
                ),
                "check": (
                    "Why should responders verify a change record before "
                    "altering a cloud resource? What makes an incident note "
                    "useful?"
                ),
                "review": (
                    "A safe first response preserves context, verifies through "
                    "an approved owner, and leaves containment decisions to "
                    "authorized responders."
                ),
                "challenge_prompt": (
                    "A fictional cloud alert reports an unfamiliar access "
                    "change, but a scheduled maintenance window may be in "
                    "progress. What should you do first?"
                ),
                "expected_answer": (
                    "Preserve the alert details and verify the change with the "
                    "resource owner through the approved incident channel"
                ),
            },
        ],
    },
]


def build_specialist_lesson(lesson):
    duration_minutes = 60
    content = "\n\n".join(
        [
            "LEARNING OUTCOMES\n"
            f"By the end of this lesson, you should be able to explain "
            f"{lesson['title'].casefold()}, apply its guidance to a fictional "
            "case, and identify when to ask an authorized owner for help.",
            f"CORE LESSON NOTES\n{lesson['notes']}",
            "GUIDED PRACTICE · 20 MINUTES\n"
            f"{lesson['guided']} Work only with the fictional materials "
            "provided; do not use real accounts, personal data, or systems.",
            "INDEPENDENT PRACTICE · 15 MINUTES\n"
            f"{lesson['independent']} Record assumptions separately from "
            "confirmed facts and use the organization's approved policy as "
            "the authority for real-world decisions.",
            "KNOWLEDGE CHECK · 10 MINUTES\n"
            f"{lesson['check']}",
            "ASSESSMENT AND REVIEW · 10 MINUTES\n"
            f"{lesson['review']} Assessment: submit your written practice "
            "with a clear reason, evidence, and next step. Review it for "
            "accuracy, privacy, authorization, and clarity.",
            "TIME ALLOCATION\n"
            "5 minutes: review the outcomes. 20 minutes: study the lesson "
            "notes and worked concepts. 20 minutes: complete guided practice. "
            "15 minutes: independent practice and knowledge check. "
            f"Total: {duration_minutes} minutes (1 hour).",
        ]
    )
    return {
        "title": lesson["title"],
        "lesson_type": lesson.get("lesson_type", "article"),
        "duration": "1 hour",
        "content": content,
        "challenge_prompt": lesson.get("challenge_prompt", ""),
        "expected_answer": lesson.get("expected_answer", ""),
    }


def build_specialist_course(course):
    return {
        **{key: value for key, value in course.items() if key != "lessons"},
        "lessons": [
            build_specialist_lesson(lesson) for lesson in course["lessons"]
        ],
    }
