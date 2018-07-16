from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import textobject, canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, TableStyle, SimpleDocTemplate, PageBreak, Spacer
import json


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def fill_page_with_image(x,y,draw_width,draw_height,path, canvas):
    from PIL import Image

    page_width, page_height = canvas._pagesize
    image = Image.open(path)
    image_width, image_height = image.size
    # draw_width, draw_height = page_width, page_height

    # if hasattr(image, '_getexif'):
    #     orientation = image._getexif().get(274, 1)  # 274 = Orientation
    # else:
    #     orientation = 1
    #
    # # These are the possible values for the Orientation EXIF attribute:
    # ORIENTATIONS = {
    #     1: "Horizontal (normal)",
    #     2: "Mirrored horizontal",
    #     3: "Rotated 180",
    #     4: "Mirrored vertical",
    #     5: "Mirrored horizontal then rotated 90 CCW",
    #     6: "Rotated 90 CW",
    #     7: "Mirrored horizontal then rotated 90 CW",
    #     8: "Rotated 90 CCW",
    # }
    # draw_width, draw_height = page_width, page_height
    # if orientation == 1:
    #     canvas.setPageRotation(0)
    # elif orientation == 3:
    #     canvas.setPageRotation(180)
    # elif orientation == 6:
    #     image_width, image_height = image_height, image_width
    #     draw_width, draw_height = page_height, page_width
    #     canvas.setPageRotation(90)
    # elif orientation == 8:
    #     image_width, image_height = image_height, image_width
    #     draw_width, draw_height = page_height, page_width
    #     canvas.setPageRotation(270)
    # else:
    #     raise ValueError("Unsupported image orientation '%s'."
    #                      % ORIENTATIONS[orientation])

    # if image_width > image_height:
    #     page_width, page_height = page_height, page_width  # flip width/height
    #     draw_width, draw_height = draw_height, draw_width
    #     canvas.setPageSize((page_width, page_height))

    canvas.drawImage(path, x, y, width=draw_width, height=draw_height,
                     preserveAspectRatio=False)
# c=canvas.Canvas("vishal.pdf",letter)
# fill_page_with_image(0,0,432,842,"frame1.png",c)
# fill_page_with_image(432,0,595-410,842,"frame2.jpg",c)





#opening my json file data for some use

with open("./extras/resumeStructure.json") as json_data:
    resume_data = json.load(json_data)
# registering inconsolata font which is used in making font in resume pdf
registerFont(TTFont('Inconsolata', 'fonts/Inconsolata-Regular.ttf'));
registerFont(TTFont('InconsolataBold', 'fonts/Inconsolata-Bold.ttf'));
registerFontFamily('Inconsolata', normal='Inconsolata', bold='InconsolataBold')
#raw data
data = {
    'objective': ' '.join(['Seeking co-operative employment',
                           'in the field of software development,',
                           'preferably working in python and web backend infrastructure or distributed computing, ',
                           'to start June 2016.']),
    'summary': ' '.join(['I love to use programming to solve interesting problems.',
                         'I love working in Python (which is why I generated this resume in Python using ReportLab), but I am comfortable working in a variety of languages.',
                         'I am currently exploring the exciting world of distributed and cloud computing, and love to discuss the unique opportunities this type of computing presents.']),
    'education': '<br/>'.join(['<b>Rochester Insitute of Technology</b>',
                               '<b>B.S.</b>  Computer Science',
                               '<b>Expected Graduation</b>  2017']),
    'skills': '<br/>'.join(['<b>Languages</b> <br/> Python, Java, C#, C, MIPS Assembly, Bash, jQuery, HTML, CSS',
                            '<b>Tools</b> <br/>  Git/Mercurial, Vim, Django, Tornado, Twisted, Autobahn, ReportLab',
                            '<b>Platforms</b>  <br/> Linux (Debian, RHEL), OSX, Windows',
                            '<b>Services</b>  <br/> Microsoft Application Insights, MySQL, PostgreSQL, MongoDB, Apache/Nginx, HAProxy, Gunicorn']),
    'experience': [''.join(['<b>Microsoft</b> - Redmond, WA<br/>',
                            '<alignment=TA_RIGHT>Software Engineer Intern: May - August 2015</alignment><br/>',
                            'Designed and developed a distributed testing framework to allow for the execution of ',
                            'the principals of testing in production of Windows 10 Universal Apps across many devices.',
                            'Development done in C#, using Microsoft Application Insights as a data backend.<br/>']),
                   ''.join(['<b>Olah Healthcare</b> - Columbus, OH<br/>',
                            '<alignment=TA_RIGHT>Software Engineering Intern: May - August 2013</alignment><br/>',
                            'Developed a web application using Python and the Django framework ',
                            'to allow hospitals to easily store, search, and retrieve archived medical records. ',
                            'Primary Responsibility was the design and implementation of the metadata storage backend, and search functionality.']),
                   ''.join(['<b>Computer Science House</b> - Rochester, NY<br/>',
                            'Drink Administrator: February 2013 - Present<br/>', ]),
                   ''.join(['<b>STI-Healthcare</b> - Columbus, OH<br/>',
                            'Network & Server Administration Intern: May - August 2012<br/>', ])],
    'projects': [
        ''.join(['<b>Hangman</b> - http://github.com/nickdepinet/hangman<br/>',
                 'Implemented a command line hangman game engine and an artifical intelligence player in python.',
                 'The AI uses letter frequencies from the english dictionary and additionally word frequencies from the ',
                 'Google corpus make intelligent guesses as to the next letter.']),
        ''.join(['<b>g()(\'al\')</b> - http://github.com/eatnumber1/goal<br/>',
                 'Completed the first python solution to the g()(\'al\') programming challenge. ',
                 'The "goal" of the g()(\'al\') challenge is to enable the calling of g()(\'al\') in the source of the ',
                 'language of choice with n ()\'s, and to be returned the string "goal" with the appropriate number of "o"s.']),
        ''.join(['<b>DrinkPi</b> - http://github.com/jeid64/drinkpi/<br/>',
                 'Worked with a partner to replace a failing component in the Computer Science House drink machines. ',
                 'The software controlling the machines was previously written in java and running on Dallas TINI microcomputers. ',
                 'These TINI\'s were failing and were no longer produced, so we re-wrote the software in python to run on a ',
                 'Raspberry Pi. The software talks to the drink server over sockets using the SUNDAY protocol, and to the drink ',
                 'machine hardware using the 1-Wire protocol and a usb 1-Wire bus master.']),
        ''.join(['<b>TempMon</b> - http://github.com/nickdepinet/tempmon/<br/>',
                 'Implemented a temperature monitoring system for a server room using a Raspberry Pi. ',
                 'The system monitors temperature using a series of DSB1820 temperature sensors. ',
                 'When the temperature exceeds a set limit, an email notification is sent. ',
                 'The software, including temperature reading, threading, and email notification is written in python.']),
        ''.join(
            ['<b>Nexus Q Development</b> - http://github.com/nickdepinet/android_device_google_steelhead<br/>'])]
}
#importing paragraph style from ParagraphStyleSheet Class
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
styleB = styles['Bullet']

#creating my custom paragraph style and named as Heading
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Heading', fontName='Inconsolata', fontSize=16))

styles1 = getSampleStyleSheet()
styles1.add(ParagraphStyle(name='smallfont', fontName='Inconsolata', fontSize=10))


frame_1_table_style = TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('FONT', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT')])

#story is flowable
story_frame_one = []
# story_frame_one.append(data['objective']+data['summary'])

#spacer makes space after a line ends
story_frame_one.append(Spacer(0,10))





#creating a table for underlining Experience  heading

experience_heading_data = [
    [Paragraph('<b>Experience</b>', style=styles["Heading"])]
]

style12 = TableStyle([
    ("LINEBELOW", (0, 0), (-1, -1), 1, colors.black),
    ('VALIGN', (0, 0), (0, 0), 'MIDDLE')

])
experience_heading_table = Table(experience_heading_data, rowHeights=30)
experience_heading_table.setStyle(style12)


story_frame_one.append(experience_heading_table)

#creating the table for the content under Experience


experience_data = [
    # ['OBJECTIVE', Paragraph(data['objective'], styleN)],
    # ['SUMMARY', Paragraph(data['summary'], styleB)],
    # ['EDUCATION', Paragraph(data['education'], styleB)],
    # ['SKILLS', Paragraph(data['skills'], styleN)],
    ['EXPERIENCE', [Paragraph(x, styleN) for x in data['experience']]],
]
experience_table = Table(
    experience_data,
    colWidths=[
        .8 * inch,
        5.2 * inch]
)
experience_table.setStyle(frame_1_table_style)
story_frame_one.append(experience_table)


project_heading_data = [
    [Paragraph('<b>Projects</b>', style=styles["Heading"])]
]
project_heading_table = Table(project_heading_data, rowHeights=30)
project_heading_table.setStyle(style12)
story_frame_one.append(project_heading_table)
project_data = [
    ['PROJECTS', [Paragraph(x, styleN) for x in data['projects']]]
]
project_table = Table(project_data,
                        colWidths=[
                            .8 * inch,
                            5.2 * inch]

                        )
project_table.setStyle(frame_1_table_style)
story_frame_one.append(project_table)



education_heading_data = [
    [Paragraph('<b>Education</b>', style=styles["Heading"])]
]
education_heading_table = Table(education_heading_data, rowHeights=30)
education_heading_table.setStyle(style12)
story_frame_one.append(education_heading_table)



education_data = [
    # ['EDUCATION', Paragraph(data['education'], styleB)],


    [Paragraph(resume_data["education"][0]["startDate"] + "-" + resume_data["education"][0]["endDate"], style=styles1["smallfont"]),
     Paragraph(resume_data["education"][0]["institution"], styleN)],
[Paragraph(resume_data["education"][1]["startDate"] + "-" + resume_data["education"][1]["endDate"], style=styles1["smallfont"]),
     Paragraph(resume_data["education"][1]["institution"], styleN)],
[Paragraph(resume_data["education"][2]["startDate"] + "-" + resume_data["education"][2]["endDate"], style=styles1["smallfont"]),
     Paragraph(resume_data["education"][2]["institution"], styleN)]

]
education_table = Table(education_data,
                        colWidths=[
                            .8 * inch,
                            5.2 * inch]

                        )
education_table.setStyle(frame_1_table_style)
story_frame_one.append(education_table)
# canvas.restoreState()


c = Canvas('mydoc.pdf')
fill_page_with_image(0,0,432,842,"frame1.png",c)
fill_page_with_image(432,0,595-410,842,"frame2.jpg",c)

c.setFillColorRGB(0, .159, .142)
c.rect(0, 760, 612, 200, 0, 1)
c.setFillColorRGB(1, 1, 1)
c.setFont("Helvetica", 30)
c.drawString(20, 800, "Trisha Stamm", )
c.setFont("Helvetica", 15)
c.drawString(20, 775, "Data Scientist, Microsoft Certified", )

frame_one = Frame(0, 0, 6 * inch, 760, leftPadding=6, bottomPadding=6,
           rightPadding=6, topPadding=6, id=None, showBoundary=0)

frame_one.addFromList(story_frame_one, c)



contact = {
    'name': 'Nicholas Depinet',
    'website': 'http://github.com/nickdepinet/',
    'email': 'depinetnick@gmail.com',
    'address': '3092 Nathaniel Rochester Hall, Rochester, NY 14623',
    'phone': '(614)365-1089'}
story1 = []
tempdata2 = [
    [Paragraph('<b>Personal Info</b>', style=styles["Heading"])]
]
t2 = Table(tempdata2, rowHeights=30)
t2.setStyle(style12)
story1.append(t2)
story1.append(Spacer(0, 10))
tblData1 = [
    [Paragraph('<b>Website</b>', styleN)],

    [Paragraph(contact['website'], styleN)],
    [Paragraph('<b>E-mail</b>', styleN)],

    [Paragraph(contact['email'], styleB)],
    [Paragraph('<b>Address</b>', styleN)],

    [Paragraph(contact['address'], styleB)],
    [Paragraph('<b>Phone</b>', styleN)],

    [Paragraph(contact['phone'], styleN)],
]
contentTable1 = Table(
    tblData1,
    colWidths=[
        163]
)
tblStyle1 = TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('FONT', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT')])
contentTable1.setStyle(tblStyle1)
story1.append(contentTable1)




tempdata3 = [
    [Paragraph('<b>Skills</b>', style=styles["Heading"])]
]
t3 = Table(tempdata3, rowHeights=30)
t3.setStyle(style12)
story1.append(t3)
story1.append(Spacer(0, 10))



skills_data=[
    [Paragraph(data['skills'], styleN)],
]

skills_table=Table(skills_data,colWidths=[
        163])
skills_table.setStyle(frame_1_table_style)
story1.append(skills_table)



f2 = Frame(432, 0, 163, 760, leftPadding=6, bottomPadding=6,
           rightPadding=6, topPadding=6, id=None, showBoundary=0)
f2.addFromList(story1, c)
c.save()
