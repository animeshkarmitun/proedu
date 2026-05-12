import os
import glob

# Service page specific replacements

# 1. visa.html - Visa Application → Visa Assistance
visa_replacements = [
    ('<h2 class="text-light">Visa Application</h2>', '<h2 class="text-light">Visa Assistance</h2>'),
    ('<p>Welcome to learn more about Visa Application.</p>', '<p>Welcome to learn more about Visa Assistance.</p>'),
    ('<p><span>Visa Application</span> - Secure Your Study Abroad Journey', '<p><span>Visa Assistance</span> - Secure Your Study Abroad Journey'),
    ('<p><span>Visa Application</span> Services Include:</p>', '<p><span>Visa Assistance</span> Services Include:</p>'),
    ('Our <strong class="fw-bold">Visa Application Service</strong>', 'Our <strong class="fw-bold">Visa Assistance Service</strong>'),
    ('<strong class="fw-bold"> â\x80\x9c+880 1889993282â\x80\x9d</strong>', '<strong class="fw-bold"> â\x80\x9c+880 1911 523289â\x80\x9d</strong>'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant,</strong>', 'At <strong class="fw-bold">European International,</strong>'),
]

# 2. travel.html - Travel Assistance → Accommodation
travel_replacements = [
    ('<h2 class="text-light">Travel Assistance</h2>', '<h2 class="text-light">Accommodation</h2>'),
    ('<p>Welcome to learn more about Travel Assistance.</p>', '<p>Welcome to learn more about Accommodation.</p>'),
    ('<p>Our <span>Travel Assistance</span> Services Include:</p>', '<p>Our <span>Accommodation</span> Services Include:</p>'),
    ('Our <strong class="fw-bold">Travel Assistance</strong> service', 'Our <strong class="fw-bold">Accommodation</strong> service'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, we understand that moving\n                                abroad for studies is an exciting yet challenging experience. Our <strong class="fw-bold">Travel Assistance</strong> service is designed to ensure that your\n                                transition from home to your study destination is smooth and hassle-free. From booking\n                                flights to arranging transportation upon arrival, weâ\x80\x99re here to help you every step of the\n                                way.\n                                With over 15 years of experience in guiding students to top destinations, we offer expert\n                                advice and support to make sure your journey is as seamless as possible.\n                            </p>',
     'At <strong class="fw-bold">European International</strong>, we support students in seeking safe, comfortable, and affordable housing options in their study destination countries. We assist in arranging university dormitories, shared apartments, and private rentals based on studentsâ\x80\x99 preferences and budgets. Our team ensures that students get suitable accommodation options close to their universities for a secure and convenient living experience abroad.\n                            </p>'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, weâ\x80\x99re dedicated to making sure\n                                your travel experience is smooth, safe, and enjoyable, so you can focus on what matters your\n                                studies.</p>',
     'At <strong class="fw-bold">European International</strong>, weâ\x80\x99re dedicated to making sure\n                                your accommodation is safe, comfortable, and convenient, so you can focus on what matters â\x80\x94 your\n                                studies.</p>'),
]

# 3. support.html - Arrival Support → Accommodation
support_replacements = [
    ('<h2 class="text-light">Arrival Support</h2>', '<h2 class="text-light">Accommodation</h2>'),
    ('<p>Welcome to learn more about Arrival Support.</p>', '<p>Welcome to learn more about Accommodation.</p>'),
    ('Your First Steps Abroad, Made Easy', 'Safe and Comfortable Housing for Students'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, we believe that your journey\n                                doesnâ\x80\x99t end when you land in a new countryâ\x80\x94itâ\x80\x99s just the beginning. Our <strong class="fw-bold">Arrival Support</strong> service is here to ensure that your first days\n                                abroad are smooth and stress-free, so you can settle into your new life with confidence.\n                            </p>',
     'At <strong class="fw-bold">European International</strong>, we support students in seeking safe, comfortable, and affordable housing options in their study destination countries. We assist in arranging university dormitories, shared apartments, and private rentals based on studentsâ\x80\x99 preferences and budgets.\n                            </p>'),
    (' Moving to a different country for studies can be overwhelming, but with our expert support,\n                                youâ\x80\x99ll have everything you need to feel at home from the moment you arrive. We offer\n                                personalized assistance to help you navigate the challenges of adapting to a new environment\n                                and ensure you have the resources and support required to get started on the right foot.</p>',
     ' Our team ensures that students get suitable accommodation options close to their universities for a secure and convenient living experience abroad.</p>'),
    ('<strong class="fw-bold">Settling in with Confidence</strong> Our arrival support is designed\n                                to make sure you feel comfortable and secure during your first few days abroad. From\n                                navigating local systems to providing practical advice, we take care of the details so you\n                                can focus on starting your academic journey on the right note.</p>',
     '<strong class="fw-bold">Comfortable Living Options</strong> We assist in arranging university dormitories, shared apartments, and private rentals based on your preferences and budget, so you can focus on your academic journey.</p>'),
    ('<strong class="fw-bold">How to Get Started</strong> Need arrival support? Book an\n                                appointment with us by filling out our online form, calling <strong class="fw-bold">â\x80\x9c+880\n                                    1889993282â\x80\x9d</strong>, or visiting one of our offices. Our <strong class="fw-bold">arrival support services are free</strong>, providing you with peace of\n                                mind as you embark on your educational journey.\n                            </p>',
     '<strong class="fw-bold">How to Get Started</strong> Need accommodation support? Book an\n                                appointment with us by filling out our online form, calling <strong class="fw-bold">â\x80\x9c+880\n                                    1911 523289â\x80\x9d</strong>, or visiting one of our offices. Our <strong class="fw-bold">accommodation support services are free</strong>, providing you with peace of\n                                mind as you embark on your educational journey.\n                            </p>'),
]

# 4. Common replacements for all service pages (excluding testimonial.html)
common_replacements = [
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, we understand that the', 'At <strong class="fw-bold">European International</strong>, we understand that the'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, weâ\x80\x99re committed to making your', 'At <strong class="fw-bold">European International</strong>, weâ\x80\x99re committed to making your'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, we believe that the right', 'At <strong class="fw-bold">European International</strong>, we believe that the right'),
    ('Scholarships can significantly reduce the cost of studying abroad, and at <strong class="fw-bold">Pro Info & Edu Consultant</strong>, weâ\x80\x99re committed to helping you find',
     'Scholarships can significantly reduce the cost of studying abroad, and at <strong class="fw-bold">European International</strong>, weâ\x80\x99re committed to helping you find'),
    ('At<strong class="fw-bold">Pro Info & Edu Consultant</strong>, weâ\x80\x99re committed to helping you',
     'At<strong class="fw-bold">European International</strong>, weâ\x80\x99re committed to helping you'),
    ('At <strong class="fw-bold">Pro Info & Edu Consultant</strong>, we believe that your journey',
     'At <strong class="fw-bold">European International</strong>, we believe that your journey'),
    ('Learn more about Pro Info & Edu Consultant Event.', 'Learn more about European International Event.'),
    ('â\x80\x9c+8801889993282â\x80\x9d', 'â\x80\x9c+880 1911 523289â\x80\x9d'),
    ('â\x80\x9c+880 1889993282â\x80\x9d', 'â\x80\x9c+880 1911 523289â\x80\x9d'),
]

def apply_replacements(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes += 1
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return 0

# Files to update with common replacements (exclude testimonial.html)
all_html = sorted(glob.glob('*.html') + glob.glob('*.htm'))
exclude = {'index.htm', 'denmark.html', 'sweden.html', 'usa.html', 'testimonial.html'}
service_files = [f for f in all_html if f not in exclude]

print("=== Applying common replacements ===")
for filepath in service_files:
    changes = apply_replacements(filepath, common_replacements)
    if changes > 0:
        print(f"[OK] {filepath}: {changes} common replacements applied")
    else:
        print(f"[--] {filepath}: no common replacements")

print("\n=== Applying page-specific replacements ===")

# visa.html
if os.path.exists('visa.html'):
    changes = apply_replacements('visa.html', visa_replacements)
    print(f"[OK] visa.html: {changes} visa-specific replacements applied")

# travel.html
if os.path.exists('travel.html'):
    changes = apply_replacements('travel.html', travel_replacements)
    print(f"[OK] travel.html: {changes} travel-specific replacements applied")

# support.html
if os.path.exists('support.html'):
    changes = apply_replacements('support.html', support_replacements)
    print(f"[OK] support.html: {changes} support-specific replacements applied")

print("\nDone!")
