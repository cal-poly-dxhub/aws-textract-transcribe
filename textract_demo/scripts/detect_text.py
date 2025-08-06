import boto3

textract = boto3.client('textract')
document_path = 'agenda.pdf'

with open(document_path, 'rb') as doc_file:
    img_bytes = doc_file.read()

response = textract.detect_document_text(
    Document={'Bytes': img_bytes}
)

for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])
