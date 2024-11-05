import boto3
import os
import time

# Initialize AWS clients
s3_client = boto3.client('s3')
transcribe_client = boto3.client('transcribe')

# Function to start a transcription job
def start_transcription_job(job_name, audio_file_uri, output_bucket, output_prefix):
    response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': audio_file_uri},
        MediaFormat='mp3',  # Change the format if needed (e.g., wav, mp4)
        LanguageCode='en-US',  # Change if the audio is in another language
        OutputBucketName=output_bucket,
        OutputKey=output_prefix,
    )
    return response

# Function to check the status of the transcription job
def check_transcription_job_status(job_name):
    response = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
    return response['TranscriptionJob']['TranscriptionJobStatus']

# Function to process audio files in S3
def transcribe_audio_files(source_bucket, source_prefix, destination_prefix):
    # List all objects in the source S3 folder
    objects = s3_client.list_objects_v2(Bucket=source_bucket, Prefix=source_prefix)
    
    for obj in objects.get('Contents', []):
        if obj['Key'].endswith('.mp3'):  # Change the format if needed
            audio_file_uri = f"s3://{source_bucket}/{obj['Key']}"
            
            # Create a job name by replacing slashes and dots with underscores
            job_name = os.path.basename(obj['Key']).replace('.', '_').replace('.mp3', '')
            
            # Create the output file name with the same structure, replace spaces with underscores
            output_file_name = os.path.basename(obj['Key']).replace(' ', '_').replace('.mp3', '.json')
            
            # Determine the output path in the destination folder
            output_folder = obj['Key'].replace(source_prefix, destination_prefix, 1).rsplit('/', 1)[0]
            output_prefix = f"{output_folder}/{output_file_name}"

            print(f"Starting transcription job for {obj['Key']}...")
            start_transcription_job(job_name, audio_file_uri, source_bucket, output_prefix)

            # Wait for the job to complete
            while True:
                status = check_transcription_job_status(job_name)
                if status in ['COMPLETED', 'FAILED']:
                    break
                print(f"Job {job_name} status: {status}")
                time.sleep(10)

            if status == 'COMPLETED':
                print(f"Transcription completed for {obj['Key']}.")
            else:
                print(f"Transcription failed for {obj['Key']}.")

if __name__ == "__main__":
    source_bucket = 'drfoojandocuments'
    source_prefix = 'ai-videos-2024/Tip_of_the_day_-_English/'
    destination_prefix = 'ai-videos-2024/transcribtionresultsaug2024/Tip_of_the_day_-_English/'

    transcribe_audio_files(source_bucket, source_prefix, destination_prefix)
