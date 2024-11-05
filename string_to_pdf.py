# Install the fpdf library
# !pip install fpdf

from fpdf import FPDF

def create_pdf(text, filename="output.pdf"):
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=10)
    
    # Add text to PDF
    pdf.multi_cell(0, 4, text)
    
    # Save the PDF with the given filename
    pdf.output(filename)
    print(f"PDF created successfully: {filename}")

# Usage
text = """
** Phase 3 of Awareness Integration Theory (AIT)**

Phase 3: The purpose of the Phase Three is to aid the client in discovering how she
perceives herself and her own identity. In this phase, the client is asked
about how she thinks, feels, and behaves toward herself in various life
domains. There is an opportunity for the client to be more conscious about
the assignations, such as I am not good enough or I am a failure, that
she has created about herself in each area, and how the accumulation of
these formulas and beliefs fixed in place an identity, which she operates
from automatically.
The most important beliefs are the ones about the self. These beliefs color
how we operate in the world, despite the reality of how we present out there
and who we are seen as in the eyes of others. Some clients are righteous
about who they are, and they have a very positive view of the self despite
their behavior harming others and not being able to create or maintain
relationships. On the opposite side of the spectrum are clients who, in the
eyes of the world and based on tangible results, have all that anyone might
want or need, but still think of themselves as not good enough and less than.
So, when the reality that is built as a narrative about one's self is very
different than the results that are presented to the world, living day to day,
coordinating and cooperating with others, becomes very difficult and often
leads to suffering. Bringing these two worlds of inner and outer reality
closer together creates some congruence and a sense of integrity, which will
create smoother interactions in the client's relationship with self and others,
therefore bringing about a sense of inner clarity and peace.
This phase often uncovers negative core beliefs the client has about herself,
which appear to be unshakable and have become the core of her identity.
This is the basis for the client's self-esteem. Once known, these beliefs can
be managed, challenged, dismantled, or replaced with a healthier and more
age-appropriate self-belief later in Phase Four. This phase also brings the
positive core beliefs that are the basis of the client's strength and can be
utilized as the source of their sense of self love, fulfillment, and success.

"""

create_pdf(text, "Phase_3_AIT.pdf")
