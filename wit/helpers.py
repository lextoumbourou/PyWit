def process_content_type(content_type):
    if content_type.lower().startswith('audio/'):
        content_type = content_type[6:]

    return 'audio/' + content_type
