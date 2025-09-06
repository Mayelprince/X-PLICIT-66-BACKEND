import os
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME", ""),
    api_key=os.getenv("CLOUDINARY_API_KEY", ""),
    api_secret=os.getenv("CLOUDINARY_API_SECRET", ""),
    secure=True,
)

async def upload_image(file_obj) -> str:
    """
    Expects a SpooledTemporaryFile or file-like object.
    Returns the secure_url from Cloudinary.
    """
    # In an async app you may want to upload using threadpool; this is a simple wrapper.
    result = cloudinary.uploader.upload(file_obj)
    return result.get("secure_url")
