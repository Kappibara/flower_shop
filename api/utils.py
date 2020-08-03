

def is_int(data):
    try:
        int(data.get("offset"))
        int(data.get("limit"))
        return True
    except ValueError:
        return False


def serialize_product(product):
    return {
        "image_url": product.image_url,
        "price": float(product.price),
        "title": product.description,
        "ingredients": [f.name for f in product.ingredients],
        "categories": [c.name for c in product.categories],
    }