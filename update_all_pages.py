import os
import glob

# The exact replacements to apply across all HTML files
# These are the shared header/footer/nav blocks that are copy-pasted identically

replacements = [
    # 1. Top bar - Requesting a Call phone number
    (
        '''                        <div class="nav-content">
                            <label>Requesting a Call:</label>
                            <span>01889993282</span>
                        </div>''',
        '''                        <div class="nav-content">
                            <label>Requesting a Call:</label>
                            <span>01898805351</span><br>
                            <span>01898805359</span>
                        </div>'''
    ),
    # 2. Top bar - Feedback phone number
    (
        '''                        <div class="nav-content">
                            <label>Feedback:</label>
                            <span>01519393939</span>
                        </div>''',
        '''                        <div class="nav-content">
                            <label>Feedback:</label>
                            <span>01911-523289</span>
                        </div>'''
    ),
    # 3. Top bar - Working hours → Free Consultation
    (
        '''                    <div class="d-flex align-items-center px-3 nav-hover">
                        <div class="nav-icon-loc">
                            <i class='bx bx-alarm'></i>
                        </div>
                        <div class="nav-content">
                            <label>Saturday - Thursday :</label>
                            <span>10:00am - 6:00pm</span>
                        </div>
                    </div>''',
        '''                    <div class="d-flex align-items-center px-3 nav-hover">
                        <a href="https://www.proinfoedu.com/apply">
                            <button type="button" style="background-color:#E84C4C; color:white; cursor:pointer; padding:8px 16px; border:none; border-radius:4px; font-weight:bold;">
                                Free Consultation
                            </button>
                        </a>
                    </div>'''
    ),
    # 4. Desktop nav menu
    (
        '''                    <ul class="nav-bar d-flex justify-content-between">
                        <li class="home"><a href="index.htm" class="nav-top-border">Home</a></li>
                        <!--<li><a href="https://www.proinfoedu.com/about-us" class="nav-top-border">About us</a></li>-->
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">Destination</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li><a href="australia.html"><span class="flag-icon flag-icon-au"></span>
                                        Australia</a></li>
                                <li><a href="newzealand.html"><span class="flag-icon flag-icon-nz"></span> New
                                        Zealand</a></li>
                                <li class="pb-4"><a href="canada.html"><span class="flag-icon flag-icon-ca"></span> Canada</a></li>
                                <li><a href="uk.html"><span class="flag-icon flag-icon-gb"></span> United
                                        Kingdom</a></li>
                                <li><a href="europe.html"><span class="flag-icon flag-icon-eu"></span> Europe</a></li>
                                <li><a href="southkorea.html"><span class="flag-icon flag-icon-kr"></span> South Korea</a></li>
                                <li class="pt-4"><a href="malaysia.html"><span class="flag-icon flag-icon-my"></span> Malaysia</a></li>
                            </ul>
                        </li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">Service</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li class="pt-4"><a href="counseling.html">Education Counseling</a></li>
                                <li><a href="admission.html">Admission Process</a></li>
                                <li><a href="visa.html">Visa Application</a></li>
                                <li><a href="scholarship.html">Scholarship Facilities</a></li>
                                <li><a href="travel.html">Travel Assistance</a></li>
                                <li class="pb-4"><a href="support.html">Arrival Support</a></li>
                            </ul>
                        </li>
                        <li class=""><a href="testimonial.html" class="nav-top-border">Testimonial</a>
                        </li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">Events</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li class="pt-4"><a href="event.html">Our Events</a></li>
                                <li class="pb-4"><a href="event-gallery.html">Our Gallery</a></li>
                            </ul>
                        </li>
                        <li class=""><a href="blog.html" class="nav-top-border">Blogs</a></li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">About</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li><a href="https://www.proinfoedu.com/about-us" class="nav-top-border">About us</a></li>
                                <li><a href="https://www.proinfoedu.com/certificates" class="nav-top-border">Professional
                                        Affiliation</a></li>
                            </ul>
                        </li>
                        <li class=""><a href="https://www.proinfoedu.com/contact-us" class="nav-top-border">Contact us</a>
                        </li>
                    </ul>''',
        '''                    <ul class="nav-bar d-flex justify-content-between">
                        <li class="home"><a href="index.htm" class="nav-top-border">Home</a></li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">About</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li><a href="https://www.proinfoedu.com/about-us" class="nav-top-border">About us</a></li>
                                <li><a href="https://www.proinfoedu.com/certificates" class="nav-top-border">Professional
                                        Affiliation</a></li>
                            </ul>
                        </li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">Destination</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li><a href="australia.html"><span class="flag-icon flag-icon-au"></span>
                                        Australia</a></li>
                                <li><a href="newzealand.html"><span class="flag-icon flag-icon-nz"></span> New
                                        Zealand</a></li>
                                <li class="pb-4"><a href="canada.html"><span class="flag-icon flag-icon-ca"></span> Canada</a></li>
                                <li><a href="uk.html"><span class="flag-icon flag-icon-gb"></span> United
                                        Kingdom</a></li>
                                <li><a href="europe.html"><span class="flag-icon flag-icon-eu"></span> Europe</a></li>
                                <li><a href="southkorea.html"><span class="flag-icon flag-icon-kr"></span> South Korea</a></li>
                                <li class="pt-4"><a href="malaysia.html"><span class="flag-icon flag-icon-my"></span> Malaysia</a></li>
                            </ul>
                        </li>
                        <li class="service arrow-control">
                            <a href="#" class="nav-top-border">Service</a>
                            <i class='bx bxs-chevron-down arrow'></i>
                            <ul class="sub-menu-service">
                                <li class="pt-4"><a href="counseling.html">Education Counseling</a></li>
                                <li><a href="admission.html">Admission Process</a></li>
                                <li><a href="visa.html">Visa Assistance</a></li>
                                <li><a href="scholarship.html">Scholarship Facilities</a></li>
                                <li class="pb-4"><a href="support.html">Accommodation</a></li>
                            </ul>
                        </li>
                        <li class=""><a href="testimonial.html" class="nav-top-border">Testimonial</a>
                        </li>
                        <li class=""><a href="index.htm#testimonial" class="nav-top-border">Success Stories</a>
                        </li>
                        <li class=""><a href="blog.html" class="nav-top-border">Learning Resources</a></li>
                        <li class=""><a href="https://www.proinfoedu.com/contact-us" class="nav-top-border">Contact us</a>
                        </li>
                    </ul>'''
    ),
    # 5. Nav apply/complain button
    (
        '''                    <div class="apply-button d-flex justify-content-end">
                        <!-- <a href="https://www.proinfoedu.com/apply" class="pe-1">
                            <button type="button" class="">Apply Now <i class='bx bx-right-arrow-alt'></i></button>
                        </a> -->
                        <a href="tel:+8801519393939" class="pe-1">
                            <button type="button" class="">Complain</button>
                        </a>
                    </div>''',
        '''                    <div class="apply-button d-flex justify-content-end">
                        <a href="https://www.proinfoedu.com/apply" class="pe-1">
                            <button type="button" style="background-color:#E84C4C; color:white; cursor:pointer; padding:6px 12px; border:none; border-radius:4px; font-weight:bold;">Free Consultation</button>
                        </a>
                    </div>'''
    ),
    # 6. Mobile nav - About section
    (
        '''                    <li class="nav-item">
                        <a class="nav-link " href="index.htm">
                            <i class="bi bi-grid"></i>
                            <span>Home</span>
                        </a>
                    </li>
                    <!--<li class="nav-item">-->
                    <!--    <a class="nav-link " href="https://www.proinfoedu.com/about-us">-->
                    <!--        <i class="bi bi-node-plus"></i>-->
                    <!--        <span>About Us</span>-->
                    <!--    </a>-->
                    <!--</li>-->
                    <li class="service arrow-control">
                        <a href="#" class="nav-top-border">About</a>
                        <i class='bx bxs-chevron-down arrow'></i>
                        <ul class="sub-menu-service">
                            <li><a href="https://www.proinfoedu.com/about-us" class="nav-top-border">About us</a></li>
                            <li><a href="https://www.proinfoedu.com/certificates" class="nav-top-border">Professional
                                    Affiliation</a></li>
                        </ul>
                    </li>''',
        '''                    <li class="nav-item">
                        <a class="nav-link " href="index.htm">
                            <i class="bi bi-grid"></i>
                            <span>Home</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link collapsed" data-bs-target="#about-nav" data-bs-toggle="collapse" href="#">
                            <i class="bi bi-node-plus"></i><span>About</span><i class="bi bi-chevron-down ms-auto"></i>
                        </a>
                        <ul id="about-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                            <li>
                                <a href="https://www.proinfoedu.com/about-us">
                                    <i class="bi bi-circle"></i><span>About us</span>
                                </a>
                            </li>
                            <li>
                                <a href="https://www.proinfoedu.com/certificates">
                                    <i class="bi bi-circle"></i><span>Professional Affiliation</span>
                                </a>
                            </li>
                        </ul>
                    </li>'''
    ),
    # 7. Mobile nav - Testimonial/Events/Blogs → Testimonial/Success Stories/Learning Resources
    (
        '''                    <li class="nav-item">
                        <a class="nav-link " href="testimonial.html">
                            <i class="bi bi-body-text"></i>
                            <span>Testimonials</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link collapsed" data-bs-target="#event-nav" data-bs-toggle="collapse">
                            <i class="bi bi-alexa"></i><span>Events</span><i class="bi bi-chevron-down ms-auto"></i>
                        </a>
                        <ul id="event-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                            <li>
                                <a href="event.html">
                                    <i class="bi bi-circle"></i><span>Our Events</span>
                                </a>
                            </li>
                            <li>
                                <a href="event-gallery.html">
                                    <i class="bi bi-circle"></i><span>Our Gallery</span>
                                </a>
                            </li>
                        </ul>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link " href="blog.html">
                            <i class="bi bi-body-text"></i>
                            <span>Blogs</span>
                        </a>
                    </li>''',
        '''                    <li class="nav-item">
                        <a class="nav-link " href="testimonial.html">
                            <i class="bi bi-body-text"></i>
                            <span>Testimonial</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " href="index.htm#testimonial">
                            <i class="bi bi-alexa"></i>
                            <span>Success Stories</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " href="blog.html">
                            <i class="bi bi-body-text"></i>
                            <span>Learning Resources</span>
                        </a>
                    </li>'''
    ),
    # 8. Mobile nav - Service dropdown
    (
        '''                        <ul id="service-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                            <li>
                                <a href="counseling.html">
                                    <i class="bi bi-circle"></i><span>Education Counseling</span>
                                </a>
                            </li>
                            <li>
                                <a href="admission.html">
                                    <i class="bi bi-circle"></i><span>Admission Process</span>
                                </a>
                            </li>
                            <li>
                                <a href="visa.html">
                                    <i class="bi bi-circle"></i><span>Visa Application</span>
                                </a>
                            </li>
                            <li>
                                <a href="scholarship.html">
                                    <i class="bi bi-circle"></i><span>Scholarship Facilities</span>
                                </a>
                            </li>
                            <li>
                                <a href="travel.html">
                                    <i class="bi bi-circle"></i><span>Travel Assistance</span>
                                </a>
                            </li>
                            <li>
                                <a href="support.html">
                                    <i class="bi bi-circle"></i><span>Pre & Post - Arrival Support</span>
                                </a>
                            </li>
                        </ul>''',
        '''                        <ul id="service-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                            <li>
                                <a href="counseling.html">
                                    <i class="bi bi-circle"></i><span>Education Counseling</span>
                                </a>
                            </li>
                            <li>
                                <a href="admission.html">
                                    <i class="bi bi-circle"></i><span>Admission Process</span>
                                </a>
                            </li>
                            <li>
                                <a href="visa.html">
                                    <i class="bi bi-circle"></i><span>Visa Assistance</span>
                                </a>
                            </li>
                            <li>
                                <a href="scholarship.html">
                                    <i class="bi bi-circle"></i><span>Scholarship Facilities</span>
                                </a>
                            </li>
                            <li>
                                <a href="support.html">
                                    <i class="bi bi-circle"></i><span>Accommodation</span>
                                </a>
                            </li>
                        </ul>'''
    ),
    # 9. Mobile side-apply-button
    (
        '''                    <div class="mb-2">
                        <a href="https://www.proinfoedu.com/apply">
                            <button type="button" class="">Apply Now <i class='bx bx-right-arrow-alt'></i></button>
                        </a>
                    </div>
                    <div class="">
                        <a href="tel:+8801519393939">
                            <button type="button" class="">Complain Box</button>
                        </a>
                    </div>''',
        '''                    <div class="mb-2">
                        <a href="https://www.proinfoedu.com/apply">
                            <button type="button" style="background-color:#E84C4C; color:white; cursor:pointer; padding:8px 16px; border:none; border-radius:4px; font-weight:bold;">Free Consultation</button>
                        </a>
                    </div>'''
    ),
    # 10. Floating message buttons
    (
        '''    <a href="tel:+8801889993282" class="display-button call">
        <i class='bx bx-phone-call'></i>
    </a>
    <a href="https://m.me/proinfobd" class="display-button messenger" target="_blank">
        <i class='bx bxl-messenger'></i>
    </a>
    <a href="https://wa.me/+8801519393939" class="display-button whatsapp" target="_blank">
        <i class='bx bxl-whatsapp'></i>
    </a>''',
        '''    <a href="tel:+8801911523289" class="display-button call">
        <i class='bx bx-phone-call'></i>
    </a>
    <a href="https://m.me/proinfobd" class="display-button messenger" target="_blank">
        <i class='bx bxl-messenger'></i>
    </a>
    <a href="https://wa.me/+8801911523289" class="display-button whatsapp" target="_blank">
        <i class='bx bxl-whatsapp'></i>
    </a>'''
    ),
    # 11. Footer office section
    (
        '''            <div class="col-sm-12 col-lg-5 office">
                <p class="footer-heading fade-element fade-down">Our Office</p>
                <div class="row ">
                    <div class="col-sm-6 mb-3">
                        <p class="footer-sub-heading fade-element fade-down">Dhaka Branch (Head Office)</p>
                        <a href="">Al-Minar, House-37 (Level-3
                            & 4), Road-15, Block-D, Banani, Dhaka, Bangladesh</a>
                    </div>
                    
                    <div class="col-sm-6 mb-3">
                        <p class="footer-sub-heading fade-element fade-down">Khulna Branch</p>
                        <a href="">18/A (4th floor of Aarong Building), Eden Plaza, KDA New Market, Khulna,
                            Bangladesh.
                        </a>
                    </div>
                </div>
            </div>''',
        '''            <div class="col-sm-12 col-lg-5 office">
                <p class="footer-heading fade-element fade-down">Our Office</p>
                <div class="row ">
                    <div class="col-sm-6 mb-3">
                        <p class="footer-sub-heading fade-element fade-down">Dhaka Branch (Head Office)</p>
                        <a href="">House # 05 (1st Floor), Flat # 1B, Road # 17, Block # D, Banani, Dhaka – 1213.</a>
                        <p class="mt-2"><i class='bx bxs-phone-call'></i> +880 1911 523289<br><i class='bx bxs-phone-call'></i> +880 1829 945 424</p>
                    </div>
                    
                    <div class="col-sm-6 mb-3">
                        <p class="footer-sub-heading fade-element fade-down">Sylhet Office</p>
                        <a href="">913 (8th Floor), Al-Hamra Shopping City, Zindabazar, Sylhet-3100.</a>
                        <p class="mt-2"><i class='bx bxs-phone-call'></i> +880 1712 053 853<br><i class='bx bxs-phone-call'></i> +880 1717 811 797</p>
                    </div>
                </div>
            </div>'''
    ),
    # 12. Footer services section
    (
        '''            <div class="col-sm-6 col-lg-4 service-contact">
                <p class="footer-heading fade-element fade-down">Services</p>
                <div class="row">
                    <div class="col">
                        <div><a href="">Counselling</a></div>
                        <div><a href="">Admission</a></div>
                        <div><a href="">Visa Guidance</a></div>
                    </div>
                    <div class="col">
                        <div><a href="">Scholarship</a></div>
                        <div><a href="">Travel Assistance</a></div>
                        <div><a href="">Arrival Support</a></div>
                    </div>
                </div>
            </div>
            <div class="col-sm-6 col-lg-3">
                <p class="footer-heading fade-element fade-down">Contact Us</p>
                <ul class="footer-list service-contact">
                    <li><i class='bx bxs-phone-call'></i><a href="mailto:admin@proinfoedu.com" class="ps-3">admin@proinfoedu.com</a>
                    </li>
                    <li><i class='bx bx-envelope'></i><a href="" class="ps-3">+880 1519-393939</a>
                    </li>
                </ul>''',
        '''            <div class="col-sm-6 col-lg-4 service-contact">
                <p class="footer-heading fade-element fade-down">Services</p>
                <div class="row">
                    <div class="col">
                        <div><a href="">Education Counseling</a></div>
                        <div><a href="">Admission Process</a></div>
                        <div><a href="">Visa Assistance</a></div>
                    </div>
                    <div class="col">
                        <div><a href="">Scholarship Facilities</a></div>
                        <div><a href="">Accommodation</a></div>
                    </div>
                </div>
            </div>
            <div class="col-sm-6 col-lg-3">
                <p class="footer-heading fade-element fade-down">Contact Us</p>
                <ul class="footer-list service-contact">
                    <li><i class='bx bx-envelope'></i><a href="mailto:admin@proinfoedu.com" class="ps-3">admin@proinfoedu.com</a>
                    </li>
                    <li><i class='bx bxs-phone-call'></i><a href="tel:+8801911523289" class="ps-3">+880 1911 523289</a>
                    </li>
                    <li><i class='bx bxs-phone-call'></i><a href="tel:+8801829945424" class="ps-3">+880 1829 945 424</a>
                    </li>
                </ul>'''
    ),
    # 13. Copyright
    (
        '''                <span>Â©2024 Pro Info & Edu Consultant. All Rights Reserved.</span>''',
        '''                <span>Â©2024 European International. All Rights Reserved.</span>'''
    ),
    # 14. Title tag
    (
        '''    <title>Pro Info & Edu Consultant</title>''',
        '''    <title>European International</title>'''
    ),
]

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes.append("Applied replacement")
        else:
            changes.append("NOT FOUND (skipped)")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    return False, changes

# Find all HTML files except index.htm (already done) and redirect pages
html_files = sorted(glob.glob('*.html') + glob.glob('*.htm'))
exclude = {'index.htm', 'denmark.html', 'sweden.html', 'usa.html'}
files_to_update = [f for f in html_files if f not in exclude]

updated = []
not_changed = []

for filepath in files_to_update:
    changed, changes = update_file(filepath)
    if changed:
        updated.append(filepath)
        print(f"[OK] UPDATED: {filepath}")
    else:
        not_changed.append(filepath)
        print(f"[WARN] NO CHANGE: {filepath}")

print(f"\n{'='*50}")
print(f"Total files updated: {len(updated)}")
print(f"Total files unchanged: {len(not_changed)}")
if not_changed:
    print(f"Unchanged: {', '.join(not_changed)}")
