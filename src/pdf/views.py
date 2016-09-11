from newspaper.models import Newspaper, Year, Issue

from django.http import HttpResponse
# from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib.enums import TA_JUSTIFY
# from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Frame, PageBreak, FrameBreak, Paragraph, Spacer  # , Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.doctemplate import NextPageTemplate, PageTemplate
# from _ctypes import alignment
# from reportlab.lib.units import inch


def generate_page(Story, page, article, title, text, styles, empty=False):
    # font = ttfonts.TTFont('Arial', 'arial.ttf')
    # pdfmetrics.registerFont(font)
    
    if empty:
        Story.append(Paragraph(str(page), styles['Normal']))

    if page == 1:
        Story.append(Paragraph(article.issue.newspaper.title, styles['Heading1']))
        Story.append(Paragraph(title, styles['Heading2']))
        Story.append(Paragraph(article.issue.newspaper.description, styles['Heading3']))
    else:
        if not empty:
            Story.append(Paragraph(str(article), styles['Normal']))
        Story.append(Paragraph(title, styles['Heading1']))
        
    Story.append(Paragraph(str(text), styles['Justify']))
    Story.append(PageBreak())


def pdf_view(request, **kwargs):
    newspaper_id = kwargs.get('np')
    year_id = kwargs.get('year')
    issue_id = kwargs.get('issue')
    newspaper = Newspaper.objects.get(slug=newspaper_id)
    year = Year.objects.get(year=year_id)
    issue = Issue.objects.get(newspaper=newspaper, year=year, issue=issue_id)
    
    print(kwargs)
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(kwargs.get('np', 'Unknown'))
    
    font = ttfonts.TTFont('Arial', 'arial.ttf')
    pdfmetrics.registerFont(font)
    # pdfmetrics.Encoding('Cp1251')
    
    #  p = canvas.Canvas(response, bottomup=True)
    doc = SimpleDocTemplate(response, title=str(issue), showBoundary=1)
    Story = []
    
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Arial'
    styles['Heading1'].fontName = 'Arial'
    styles['Heading2'].fontName = 'Arial'
    styles['Heading3'].fontName = 'Arial'
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontName='Arial'))
    
    page = 1
    for p in issue.article_set.all():
        while not page == p.page:
            generate_page(Story, page, p, "", "", styles, True)
            page += 1 
        
        generate_page(Story, page, p, p.unempty_title(), p.text(), styles)
        page += 1

    # p.drawString(50, 800, str(issue))

    # p.drawString(100, 100, "Hello World!")
    # p.showPage()
    
    # p.drawString(100, 100, "Hallo World!")
    # p.showPage()
    
    #  p.save()
    doc.build(Story)
    
    return response
    
