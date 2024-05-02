# python imports
import os
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
                coordinate = os.path.splitext(os.path.basename(filename))[0]
                images.append({
                    "filename": filename,
                    "coordinates": {
                        "latitude": coordinate.split("_")[0],
                        "longitude": coordinate.split("_")[1],
                    }
                })
        logger.info(f"Returning {len(images)} images")
        return jsonify(images=images, success=True, message="")
    except Exception as e:
        logger.error(traceback.format_exc())
        return jsonify(images=images, success=False, message=str(e))
