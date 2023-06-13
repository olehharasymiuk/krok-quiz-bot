# from database.models import User, Progress


def create_message_link(username, thread_id, message_id, comment_id=None, media_timestamp=None):
    base_url = "https://t.me"

    url = f"{base_url}/{username}/{thread_id}/{message_id}?single"
    if comment_id:
        url += f"&comment={comment_id}"
    if media_timestamp:
        url += f"&t={media_timestamp}"

    return url
