'''
Convert aws transcribe job json file to pdf format
'''
import os
import json
from fpdf import FPDF

# Function to create a PDF from transcript text
def create_pdf(text, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)

# Function to process JSON files and convert to PDF
def convert_json_to_pdf(transcripts_folder):
    for root, dirs, files in os.walk(transcripts_folder):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
            
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    transcript_text = data['results']['transcripts'][0]['transcript']
                    #job_name = data['jobName']

                    # Derive PDF file name
                    pdf_file_name = file.replace('-audio.json', '-transcript.pdf')

                    # Create the output path for the PDF
                    output_folder = root.replace('transcripts', 'pdf_transcripts')
                    os.makedirs(output_folder, exist_ok=True)
                    pdf_path = os.path.join(output_folder, pdf_file_name)

                    # Create PDF
                    create_pdf(transcript_text, pdf_path)
                    print(f"Created PDF: {pdf_path}")

if __name__ == "__main__":
    transcripts_folder = "transcripts"  # Path to the transcripts folder
    convert_json_to_pdf(transcripts_folder)
