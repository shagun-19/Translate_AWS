import boto3
client = boto3.client('translate', region_name="us-east-1")
text = "My Name is shagun"
result=client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="hi")
print(result)
print("Translated text is :")
print(result['TranslatedText'])