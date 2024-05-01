# python imports
import os
import base64
import traceback

# installed imports
from flask import Blueprint, jsonify

# local imports
from app import logger


main = Blueprint("main", __name__)


@main.get("/dataset/<damage>")
def get_images(damage):
    image_folder = os.path.join("dataset", damage)
    images = []
    try:
        logger.info(f"Getting dataset from {image_folder} folder")
        # Read images from folder
        for filename in os.listdir(image_folder):
            if filename.endswith(".jpeg") or filename.endswith(".png"):
                with open(os.path.join(image_folder, filename), "rb") as f:
                    # Convert image to base64
                    base64_img = base64.b64encode(f.read()).decode("utf-8")
                    images.append({"filename": filename, "data": base64_img})
        logger.info(f"Returning {len(images)} images")
        return jsonify(images=images, success=True, message="")
    except Exception as e:
        logger.error(traceback.format_exc())
        return jsonify(images=images, success=False, message=str(e))
