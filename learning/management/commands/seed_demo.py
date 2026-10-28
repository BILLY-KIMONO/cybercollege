from django.core.management.base import BaseCommand

from learning.curriculum import DIPLOMA_MODULES, build_diploma_lesson
from learning.curriculum_extensions import SUPPLEMENTAL_LESSONS
from learning.models import Course, Lesson


FOUNDATION_COURSES = [
    {
        "title": "Cybersecurity Foundations",
        "slug": "cybersecurity-foundations",
        "category": "Security fundamentals",
        "summary": "Build a strong foundation in digital safety and security thinking.",
        "description": "Explore core security principles, common terminology, and practical habits for protecting people and systems.",
        "level": "Beginner",
        "duration": "2 hours",
        "icon": "◈",
        "featured": True,
        "lessons": [
            ("The CIA triad", "article", "Understand confidentiality, integrity, and availability: three goals that help teams reason about security.", "", "", ""),
            ("Spot the phishing clues", "lab", "A colleague receives an unexpected message asking them to verify a payroll account. The sender address is unfamiliar and the link destination does not match the organization.", "What should they do first? Choose the safest action.", "Report the message through the organization’s phishing-reporting process without opening the link", ""),
            ("Build a safer passphrase", "article", "Learn why unique, long passphrases and a password manager help protect accounts.", "", "", ""),
        ],
    },
    {
        "title": "Network Defense Essentials",
        "slug": "network-defense-essentials",
        "category": "Network defense",
        "summary": "Learn how defenders monitor traffic and strengthen network boundaries.",
        "description": "Get to know network concepts, segmentation, defensive monitoring, and incident triage through safe scenarios.",
        "level": "Beginner",
        "duration": "3 hours",
        "icon": "⌁",
        "featured": True,
        "lessons": [
            ("Networks in plain language", "article", "A network connects devices so they can exchange information. Defenders map those connections to understand what normal activity looks like.", "", "", ""),
            ("Triage a network alert", "lab", "A monitoring alert reports an unfamiliar device on a staff network. No other details are available yet.", "What is the best first step? Choose the safest action.", "Verify the device and alert context with the network inventory and responsible team before taking containment action", ""),
            ("The value of segmentation", "article", "Network segmentation limits unnecessary communication between systems and can reduce the impact of an incident.", "", "", ""),
        ],
    },
    {
        "title": "Digital Forensics & Incident Response",
        "slug": "digital-forensics-incident-response",
        "category": "Incident response",
        "summary": "Practice calm, evidence-aware decisions during a security incident.",
        "description": "Follow a simple incident-response lifecycle and learn why careful documentation and evidence preservation matter.",
        "level": "Intermediate",
        "duration": "4 hours",
        "icon": "⌕",
        "featured": True,
        "lessons": [
            ("Prepare and identify", "article", "Preparation gives responders clear roles and escalation paths. Identification means validating and scoping a suspected incident.", "", "", ""),
            ("Preserve the evidence", "lab", "A workstation may be involved in a security incident. Your team has not yet documented its current state.", "What should the responder do before changing the device? Choose the safest action.", "Record the device details and follow the approved evidence-preservation and incident-response procedure", ""),
            ("Write a useful timeline", "article", "A concise timeline connects observations, timestamps, and actions so other responders can understand the investigation.", "", "", ""),
        ],
    },
    {
        "title": "Security Awareness in Practice",
        "slug": "security-awareness-in-practice",
        "category": "Security fundamentals",
        "summary": "Turn everyday security decisions into confident, repeatable habits.",
        "description": "Explore account security, safe handling of data, and how to report concerns at work or school.",
        "level": "Beginner",
        "duration": "90 minutes",
        "icon": "✳",
        "featured": False,
        "lessons": [
            ("Think before you share", "article", "Check who needs access to a document and use approved sharing settings before sending it.", "", "", ""),
            ("Respond to a lost device", "lab", "A staff member cannot find a work phone that may contain organizational email.", "What should happen next? Choose the safest action.", "Report the loss promptly through the approved IT or security channel so the organization can protect the account and device", ""),
            ("Keep accounts recoverable", "article", "Use an organization-approved recovery method and keep recovery information up to date.", "", "", ""),
        ],
    },
]


class Command(BaseCommand):
    help = "Create foundation courses and a four-semester safe cybersecurity curriculum."

    def handle(self, *args, **options):
        for item in [*FOUNDATION_COURSES, *DIPLOMA_MODULES]:
            lessons = list(item["lessons"])
            if item.get("module_code"):
                lessons.extend(
                    {
                        "title": title,
                        "lesson_type": "article",
                        "content": content,
                    }
                    for title, content in SUPPLEMENTAL_LESSONS[item["module_code"]]
                )
            course_defaults = {key: value for key, value in item.items() if key != "lessons"}
            course, _ = Course.objects.update_or_create(
                slug=item["slug"], defaults=course_defaults
            )
            for order, lesson_data in enumerate(lessons, start=1):
                if isinstance(lesson_data, dict):
                    lesson_fields = lesson_data
                    title = lesson_data["title"]
                else:
                    (
                        title,
                        lesson_type,
                        content,
                        challenge_prompt,
                        expected_answer,
                        video_url,
                    ) = lesson_data
                    lesson_fields = {
                        "lesson_type": lesson_type,
                        "content": content,
                        "challenge_prompt": challenge_prompt,
                        "expected_answer": expected_answer,
                        "video_url": video_url,
                    }
                if item.get("module_code"):
                    lesson_fields = build_diploma_lesson(item, lesson_fields, order)
                Lesson.objects.update_or_create(
                    course=course,
                    title=title,
                    defaults={
                        "order": order,
                        **lesson_fields,
                    },
                )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Seeded {item.get('module_code', course.title)} - {course.title}"
                )
            )
